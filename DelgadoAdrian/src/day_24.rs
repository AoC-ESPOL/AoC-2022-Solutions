use rustc_hash::FxHashMap;
use std::{
    cmp::Reverse,
    collections::{hash_map::Entry, BinaryHeap},
    slice,
};

fn solve<const TAKE: usize>(input: &str) -> u32 {
    let valley = parse_valley(input);

    // A* adapted from https://docs.rs/petgraph/latest/src/petgraph/algo/astar.rs.html
    let mut visit_next = BinaryHeap::new();
    let mut scores = FxHashMap::default(); // g-values, cost to reach the node
    let mut estimate_scores = FxHashMap::default(); // f-values, cost to reach + estimate cost to goal

    let mut next_starting_state = (Location::Start, 0);

    for end_goal in [Location::End, Location::Start, Location::End]
        .into_iter()
        .take(TAKE)
    {
        scores.insert(next_starting_state, 0);
        visit_next.push(Reverse((
            estimate_cost(next_starting_state.0, &valley, end_goal == Location::Start),
            next_starting_state,
        )));

        while let Some(Reverse((estimate_score, node))) = visit_next.pop() {
            if node.0 == end_goal {
                let cost = scores[&node];
                next_starting_state = (end_goal, cost + next_starting_state.1);
                break;
            }

            // This lookup can be unwrapped without fear of panic since the node was necessarily scored
            // before adding it to `visit_next`.
            let node_score = scores[&node];

            match estimate_scores.entry(node) {
                Entry::Occupied(mut entry) => {
                    // If the node has already been visited with an equal or lower score than now, then
                    // we do not need to re-visit it.
                    if *entry.get() <= estimate_score {
                        continue;
                    }
                    entry.insert(estimate_score);
                }
                Entry::Vacant(entry) => {
                    entry.insert(estimate_score);
                }
            }

            for next in valley.neighbors(node) {
                let next_score = node_score + 1;

                match scores.entry(next) {
                    Entry::Occupied(mut entry) => {
                        // No need to add neighbors that we have already reached through a shorter path
                        // than now.
                        if *entry.get() <= next_score {
                            continue;
                        }
                        entry.insert(next_score);
                    }
                    Entry::Vacant(entry) => {
                        entry.insert(next_score);
                    }
                }

                let next_estimate_score =
                    next_score + estimate_cost(next.0, &valley, end_goal == Location::Start);
                visit_next.push(Reverse((next_estimate_score, next)));
            }
        }

        visit_next.clear();
        scores.clear();
        estimate_scores.clear();
    }

    next_starting_state.1
}

fn estimate_cost(location: Location, valley: &Valley, going_back: bool) -> u32 {
    let sum = u32::from(valley.height) + u32::from(valley.width);
    let not_going_back = u32::from(!going_back);
    match location {
        Location::Start => sum * not_going_back,
        Location::End => sum * (1 - not_going_back),
        Location::Inside([row, col]) => {
            let (row, col) = (u32::from(row), u32::from(col));
            sum * not_going_back + (row + col + 1) - not_going_back * 2 * (row + col + 1)
        }
    }
}

pub fn part1(input: &str) -> u32 {
    solve::<1>(input)
}

pub fn part2(input: &str) -> u32 {
    solve::<3>(input)
}

fn parse_valley(input: &str) -> Valley {
    let width: u8 = input.find('\n').unwrap().try_into().unwrap();
    let height: u8 = input.lines().count().try_into().unwrap();
    let (width, height) = (width - 2, height - 2); // remove walls

    assert!(width <= 128, "we use a u128 as a bitmap");
    assert!(height <= 128, "we use a u128 as a bitmap");

    let blizzards = input
        .lines()
        .skip(1)
        .map(|line| {
            line.as_bytes()
                .iter()
                .skip(1)
                .zip(0..)
                .filter_map(|(&chr, col)| {
                    Some(match chr {
                        b'>' => [1 << col, 0, 0, 0],
                        b'<' => [0, 1 << col, 0, 0],
                        b'v' => [0, 0, 1 << col, 0],
                        b'^' => [0, 0, 0, 1 << col],
                        _ => return None,
                    })
                })
                .fold([0; 4], |[a_0, a_1, a_2, a_3], [b_0, b_1, b_2, b_3]| {
                    [a_0 | b_0, a_1 | b_1, a_2 | b_2, a_3 | b_3]
                })
        })
        .map(|[east, west, south, north]| BlizzardRow {
            east,
            west,
            south,
            north,
        })
        .collect();

    Valley {
        blizzards,
        width,
        height,
    }
}

struct Valley {
    blizzards: Vec<BlizzardRow>,
    width: u8,
    height: u8,
}

impl Valley {
    fn neighbors(&self, (curr_location, curr_time): (Location, u32)) -> Neighbors {
        let next_time = curr_time + 1;

        let variant = match curr_location {
            Location::Inside(curr_location) => NeighborsVariant::Inside {
                valley: self,
                curr_location,
                deltas: [(0, 1), (1, 0), (0, 0), (0, -1), (-1, 0)].iter(),
            },
            Location::Start => {
                if self.is_available([0, 0], next_time) {
                    NeighborsVariant::Start2
                } else {
                    NeighborsVariant::Start1
                }
            }
            Location::End => {
                let end = [self.height - 1, self.width - 1];
                if self.is_available(end, next_time) {
                    NeighborsVariant::End2(end)
                } else {
                    NeighborsVariant::End1
                }
            }
        };

        Neighbors { next_time, variant }
    }

    fn is_available(&self, [row, col]: [u8; 2], time: u32) -> bool {
        let width = u32::from(self.width);
        let height = u32::from(self.height);
        let col_32 = u32::from(col);
        let row_32 = u32::from(row);

        let w_col: u8 = ((col_32 + time) % width).try_into().unwrap();
        let e_col: u8 = ((col_32 + width - time % width) % width)
            .try_into()
            .unwrap();
        let n_row: usize = ((row_32 + time) % height).try_into().unwrap();
        let s_row: usize = ((row_32 + height - time % height) % height)
            .try_into()
            .unwrap();

        let col_mask = 1 << col;
        let west_mask = 1 << w_col;
        let east_mask = 1 << e_col;

        !(self.blizzards[row as usize].west & west_mask == west_mask
            || self.blizzards[row as usize].east & east_mask == east_mask
            || self.blizzards[n_row].north & col_mask == col_mask
            || self.blizzards[s_row].south & col_mask == col_mask)
    }
}

enum NeighborsVariant<'a> {
    NoNeighbors,
    Start1,
    Start2,
    End1,
    End2([u8; 2]),
    Inside {
        valley: &'a Valley,
        curr_location: [u8; 2],
        deltas: slice::Iter<'static, (i8, i8)>,
    },
}

struct Neighbors<'a> {
    next_time: u32,
    variant: NeighborsVariant<'a>,
}

impl<'a> Iterator for Neighbors<'a> {
    type Item = (Location, u32);

    fn next(&mut self) -> Option<Self::Item> {
        let next_time = self.next_time;

        match &mut self.variant {
            NeighborsVariant::Inside {
                valley,
                curr_location,
                deltas,
            } => {
                let [row, col] = curr_location;

                for &(d_row, d_col) in deltas {
                    match (
                        row.overflowing_add_signed(d_row),
                        col.overflowing_add_signed(d_col),
                    ) {
                        ((n_row, false), (n_col, false))
                            if n_row < valley.height && n_col < valley.width =>
                        {
                            if valley.is_available([n_row, n_col], next_time) {
                                return Some((Location::Inside([n_row, n_col]), next_time));
                            }
                        }
                        ((_, true), (0, false)) => return Some((Location::Start, next_time)),
                        ((n_row, false), (n_col, false))
                            if (n_row, n_col) == (valley.height, valley.width - 1) =>
                        {
                            return Some((Location::End, next_time))
                        }
                        _ => (),
                    };
                }
                None
            }
            NeighborsVariant::NoNeighbors => None,
            NeighborsVariant::Start1 => {
                self.variant = NeighborsVariant::NoNeighbors;
                Some((Location::Start, next_time))
            }
            NeighborsVariant::Start2 => {
                self.variant = NeighborsVariant::Start1;
                Some((Location::Inside([0, 0]), next_time))
            }
            NeighborsVariant::End1 => {
                self.variant = NeighborsVariant::NoNeighbors;
                Some((Location::End, next_time))
            }
            NeighborsVariant::End2(end) => {
                let end = *end;
                self.variant = NeighborsVariant::End1;
                Some((Location::Inside(end), next_time))
            }
        }
    }
}

struct BlizzardRow {
    east: u128,
    west: u128,
    south: u128,
    north: u128,
}

#[derive(Debug, Hash, PartialEq, Eq, Clone, Copy, PartialOrd, Ord)]
enum Location {
    Start,
    End,
    Inside([u8; 2]),
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 18;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 54;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

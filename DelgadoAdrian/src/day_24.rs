use std::{
    collections::{HashSet, VecDeque},
    slice,
};

pub fn part1(input: &str) -> u32 {
    let valley = parse_valley(input);

    // BFS
    let mut queue = VecDeque::new();
    let mut visited = HashSet::new();

    queue.push_back((Location::Start, 0));

    while let Some((curr_location, curr_time)) = queue.pop_front() {
        if matches!(curr_location, Location::End) {
            return curr_time;
        }

        for neigh in valley.neighbors(curr_location, curr_time) {
            if visited.insert(neigh) {
                queue.push_back(neigh);
            }
        }
    }

    unreachable!()
}

pub fn part2(input: &str) -> u32 {
    let valley = parse_valley(input);

    // BFS
    let mut queue = VecDeque::new();
    let mut visited = HashSet::new();

    let mut next_starting_state = (Location::Start, 0);

    for end_goal in [Location::End, Location::Start, Location::End] {
        queue.push_back(next_starting_state);

        while let Some((curr_location, curr_time)) = queue.pop_front() {
            if curr_location == end_goal {
                next_starting_state = (curr_location, curr_time);
                break;
            }

            for neigh in valley.neighbors(curr_location, curr_time) {
                if visited.insert(neigh) {
                    queue.push_back(neigh);
                }
            }
        }

        queue.clear();
        visited.clear();
    }

    next_starting_state.1
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
            let [east, west, south, north] = line
                .as_bytes()
                .iter()
                .skip(1)
                .zip(0..)
                .filter_map(|(&chr, col)| {
                    //east west south north
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
                });

            BlizzardRow {
                east,
                west,
                south,
                north,
            }
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
    fn neighbors(&self, curr_location: Location, curr_time: u32) -> Neighbors {
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
        let n_row: usize = ((time + row_32) % height).try_into().unwrap();
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
                        ((row, false), (col, false))
                            if row < valley.height && col < valley.width =>
                        {
                            if valley.is_available([row, col], next_time) {
                                return Some((Location::Inside([row, col]), next_time));
                            }
                        }
                        ((u8::MAX, true), (0, false)) => return Some((Location::Start, next_time)),
                        ((row, false), (col, false))
                            if (row, col) == (valley.height, valley.width - 1) =>
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

#[derive(Debug, Hash, PartialEq, Eq, Clone, Copy)]
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

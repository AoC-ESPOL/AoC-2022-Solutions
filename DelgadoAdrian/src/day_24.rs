use std::collections::{HashSet, VecDeque};

pub fn part1(input: &str) -> u32 {
    let width = input.find('\n').unwrap() as u32 - 2;
    let height = input.lines().count() as u32 - 2;
    let dimensions = (height, width);
    let mut labr = parse_labr(input);

    let mut global_minutes = 5;

    for _ in 0..global_minutes {
        for blz in &mut labr {
            blz.advance(dimensions);
        }
    }

    let mut queue = VecDeque::new();
    let mut visited = HashSet::new();

    queue.push_back(([0, 0], global_minutes));

    while let Some((curr_pos, curr_time)) = queue.pop_front() {
        if curr_pos == [height - 1, width - 1] {
            return curr_time + 1;
        }

        if curr_time != global_minutes {
            global_minutes += 1;
            for blz in &mut labr {
                blz.advance(dimensions);
            }
        }

        let [curr_x, curr_y] = curr_pos;

        for neigh in [[0, 1], [1, 0], [0, -1], [-1, 0], [0, 0]]
            .into_iter()
            .filter_map(|[dx, dy]: [i32; 2]| {
                let x = dx.checked_add_unsigned(curr_x)?.try_into().ok()?;
                let y = dy.checked_add_unsigned(curr_y)?.try_into().ok()?;
                (x < height && y < width).then_some([x, y])
            })
            .filter(|&pos| {
                Blizz::all_around_pos(dimensions, pos)
                    .into_iter()
                    .all(|near_blz| !labr.contains(&near_blz))
            })
            .map(|next_pos| (next_pos, curr_time + 1))
        {
            if visited.insert(neigh) {
                queue.push_back(neigh);
            }
        }
    }

    unreachable!()
}

pub fn part2(input: &str) -> u32 {
    let width = input.find('\n').unwrap() as u32 - 2;
    let height = input.lines().count() as u32 - 2;
    let dimensions = (height, width);
    let mut labr = parse_labr(input);

    let mut global_minutes = 5;

    for _ in 0..global_minutes {
        for blz in &mut labr {
            blz.advance(dimensions);
        }
    }

    let mut queue = VecDeque::new();
    let mut visited = HashSet::new();

    queue.push_back(([0, 0], global_minutes));

    while let Some((curr_pos, curr_time)) = queue.pop_front() {
        if curr_pos == [height - 1, width - 1] {
            global_minutes += 1;
            break;
        }

        if curr_time != global_minutes {
            global_minutes += 1;
            for blz in &mut labr {
                blz.advance(dimensions);
            }
        }

        let [curr_x, curr_y] = curr_pos;

        for neigh in [[0, 1], [1, 0], [0, -1], [-1, 0], [0, 0]]
            .into_iter()
            .filter_map(|[dx, dy]: [i32; 2]| {
                let x = dx.checked_add_unsigned(curr_x)?.try_into().ok()?;
                let y = dy.checked_add_unsigned(curr_y)?.try_into().ok()?;
                (x < height && y < width).then_some([x, y])
            })
            .filter(|&pos| {
                Blizz::all_around_pos(dimensions, pos)
                    .into_iter()
                    .all(|near_blz| !labr.contains(&near_blz))
            })
            .map(|next_pos| (next_pos, curr_time + 1))
        {
            if visited.insert(neigh) {
                queue.push_back(neigh);
            }
        }
    }

    let skip = 6;
    for _ in 0..=skip {
        for blz in &mut labr {
            blz.advance(dimensions);
        }
    }
    global_minutes += skip;

    let mut queue = VecDeque::new();
    let mut visited = HashSet::new();

    queue.push_back(([height - 1, width - 1], global_minutes));

    while let Some((curr_pos, curr_time)) = queue.pop_front() {
        if curr_pos == [0, 0] {
            global_minutes += 1;
            break;
        }

        if curr_time != global_minutes {
            global_minutes += 1;
            for blz in &mut labr {
                blz.advance(dimensions);
            }
        }

        let [curr_x, curr_y] = curr_pos;

        for neigh in [[0, 1], [1, 0], [0, -1], [-1, 0], [0, 0]]
            .into_iter()
            .filter_map(|[dx, dy]: [i32; 2]| {
                let x = dx.checked_add_unsigned(curr_x)?.try_into().ok()?;
                let y = dy.checked_add_unsigned(curr_y)?.try_into().ok()?;
                (x < height && y < width).then_some([x, y])
            })
            .filter(|&pos| {
                Blizz::all_around_pos(dimensions, pos)
                    .into_iter()
                    .all(|near_blz| !labr.contains(&near_blz))
            })
            .map(|next_pos| (next_pos, curr_time + 1))
        {
            if visited.insert(neigh) {
                queue.push_back(neigh);
            }
        }
    }

    let skip = 1;
    for _ in 0..=skip {
        for blz in &mut labr {
            blz.advance(dimensions);
        }
    }
    global_minutes += skip;

    let mut queue = VecDeque::new();
    let mut visited = HashSet::new();

    queue.push_back(([0, 0], global_minutes));

    while let Some((curr_pos, curr_time)) = queue.pop_front() {
        if curr_pos == [height - 1, width - 1] {
            return curr_time + 1;
        }

        if curr_time != global_minutes {
            global_minutes += 1;
            for blz in &mut labr {
                blz.advance(dimensions);
            }
        }

        let [curr_x, curr_y] = curr_pos;

        for neigh in [[0, 1], [1, 0], [0, -1], [-1, 0], [0, 0]]
            .into_iter()
            .filter_map(|[dx, dy]: [i32; 2]| {
                let x = dx.checked_add_unsigned(curr_x)?.try_into().ok()?;
                let y = dy.checked_add_unsigned(curr_y)?.try_into().ok()?;
                (x < height && y < width).then_some([x, y])
            })
            .filter(|&pos| {
                Blizz::all_around_pos(dimensions, pos)
                    .into_iter()
                    .all(|near_blz| !labr.contains(&near_blz))
            })
            .map(|next_pos| (next_pos, curr_time + 1))
        {
            if visited.insert(neigh) {
                queue.push_back(neigh);
            }
        }
    }

    unreachable!()
}

fn parse_labr(input: &str) -> Vec<Blizz> {
    let mut labr = Vec::new();

    for (x, row) in input.lines().skip(1).enumerate() {
        for (y, chr) in row.as_bytes().iter().skip(1).enumerate() {
            let dir = match chr {
                b'>' => Dir::E,
                b'v' => Dir::S,
                b'<' => Dir::W,
                b'^' => Dir::N,
                _ => continue,
            };

            labr.push(Blizz {
                coords: [x as u32, y as u32],
                direction: dir,
            });
        }
    }

    labr
}

#[derive(Debug, Clone, Hash, PartialEq, Eq)]
struct Blizz {
    coords: [u32; 2],
    direction: Dir,
}

impl Blizz {
    fn advance(&mut self, dimensions: (u32, u32)) {
        let [x, y] = self.coords;
        let (mod_x, mod_y) = dimensions;
        self.coords = match self.direction {
            Dir::N => [(x + mod_x - 1) % mod_x, y],
            Dir::S => [(x + 1) % mod_x, y],
            Dir::E => [x, (y + 1) % mod_y],
            Dir::W => [x, (y + mod_y - 1) % mod_y],
        }
    }

    fn all_around_pos(dimensions: (u32, u32), pos: [u32; 2]) -> [Blizz; 4] {
        let [x, y] = pos;
        let (mod_x, mod_y) = dimensions;
        let north = Blizz {
            coords: [(x + mod_x - 1) % mod_x, y],
            direction: Dir::S,
        };
        let south = Blizz {
            coords: [(x + 1) % mod_x, y],
            direction: Dir::N,
        };
        let east = Blizz {
            coords: [x, (y + 1) % mod_y],
            direction: Dir::W,
        };
        let west = Blizz {
            coords: [x, (y + mod_y - 1) % mod_y],
            direction: Dir::E,
        };

        [north, south, east, west]
    }
}

#[derive(Debug, Clone, Copy, Hash, PartialEq, Eq)]
enum Dir {
    N,
    S,
    E,
    W,
}

// #[cfg(test)]
// mod tests {
//     use super::{part1, part2};

//     const TEST_INPUT: &str = "\
// #.######
// #>>.<^<#
// #.<..<<#
// #>v.><>#
// #<^v^^>#
// ######.#";

//     #[test]
//     #[ignore]
//     fn part1_works() {
//         let output = 18;

//         assert_eq!(part1(TEST_INPUT), output);
//     }

//     // #[test]
//     // fn part2_works() {
//     //     let output = 54;

//     //     assert_eq!(part2(TEST_INPUT), output);
//     // }
// }

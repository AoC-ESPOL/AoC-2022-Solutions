use std::collections::{HashMap, HashSet};

use itertools::Itertools;

#[derive(Debug, Clone, Copy)]
enum Stream {
    Left,
    Right,
}

#[derive(Debug, Clone)]
enum RockType {
    Row,
    Plus,
    InvertedL,
    Line,
    Square,
}

// 7 units wide

impl RockType {
    fn advance_simulation(
        &self,
        chamber: &mut HashSet<(u64, u64)>,
        stream: Stream,
        (mut x, y): (u64, u64),
    ) -> Option<(u64, u64)> {
        match self {
            // #
            // #
            // #
            // #
            RockType::Line => {
                // move accord to stream
                match stream {
                    Stream::Left => {
                        if x != 0
                            && !chamber.contains(&(x - 1, y))
                            && !chamber.contains(&(x - 1, y + 1))
                            && !chamber.contains(&(x - 1, y + 2))
                            && !chamber.contains(&(x - 1, y + 3))
                        {
                            x -= 1;
                        }
                    }
                    Stream::Right => {
                        if x != 6
                            && !chamber.contains(&(x + 1, y))
                            && !chamber.contains(&(x + 1, y + 1))
                            && !chamber.contains(&(x + 1, y + 2))
                            && !chamber.contains(&(x + 1, y + 3))
                        {
                            x += 1;
                        }
                    }
                }

                // falls
                // return new pos
                if y != 0 && !chamber.contains(&(x, y - 1)) {
                    return Some((x, y - 1));
                }
                chamber.extend([(x, y), (x, y + 1), (x, y + 2), (x, y + 3)]);
            }
            // ..#
            // ..#
            // ###
            RockType::InvertedL => {
                // move accord to stream
                match stream {
                    Stream::Left => {
                        if x != 0
                            && !chamber.contains(&(x - 1, y))
                            && !chamber.contains(&(x + 1, y + 1))
                            && !chamber.contains(&(x + 1, y + 2))
                        {
                            x -= 1;
                        }
                    }
                    Stream::Right => {
                        if x != 4
                            && !chamber.contains(&(x + 3, y))
                            && !chamber.contains(&(x + 3, y + 1))
                            && !chamber.contains(&(x + 3, y + 2))
                        {
                            x += 1;
                        }
                    }
                }

                // falls
                // return new pos
                if !chamber.contains(&(x, y - 1))
                    && !chamber.contains(&(x + 1, y - 1))
                    && !chamber.contains(&(x + 2, y - 1))
                {
                    return Some((x, y - 1));
                }
                chamber.extend([
                    (x, y),
                    (x + 1, y),
                    (x + 2, y),
                    (x + 2, y + 1),
                    (x + 2, y + 2),
                ]);
            }
            // .#.
            // ###
            // .#.
            RockType::Plus => {
                // move accord to stream
                match stream {
                    Stream::Left => {
                        if x != 0
                            && !chamber.contains(&(x - 1, y + 1))
                            && !chamber.contains(&(x, y))
                            && !chamber.contains(&(x, y + 2))
                        {
                            x -= 1;
                        }
                    }
                    Stream::Right => {
                        if x != 4
                            && !chamber.contains(&(x + 2, y))
                            && !chamber.contains(&(x + 2, y + 2))
                            && !chamber.contains(&(x + 3, y + 1))
                        {
                            x += 1;
                        }
                    }
                }

                // falls
                // return new pos
                if y != 0
                    && !chamber.contains(&(x, y))
                    && !chamber.contains(&(x + 1, y - 1))
                    && !chamber.contains(&(x + 2, y))
                {
                    return Some((x, y - 1));
                }
                chamber.extend([
                    (x, y + 1),
                    (x + 1, y),
                    (x + 1, y + 1),
                    (x + 1, y + 2),
                    (x + 2, y + 1),
                ]);
            }
            // ##
            // ##
            RockType::Square => {
                // move accord to stream
                match stream {
                    Stream::Left => {
                        if x != 0
                            && !chamber.contains(&(x - 1, y))
                            && !chamber.contains(&(x - 1, y + 1))
                        {
                            x -= 1;
                        }
                    }
                    Stream::Right => {
                        if x != 5
                            && !chamber.contains(&(x + 2, y))
                            && !chamber.contains(&(x + 2, y + 1))
                        {
                            x += 1;
                        }
                    }
                }

                // falls
                // return new pos
                if y != 0 && !chamber.contains(&(x, y - 1)) && !chamber.contains(&(x + 1, y - 1)) {
                    return Some((x, y - 1));
                }
                chamber.extend([(x, y), (x, y + 1), (x + 1, y), (x + 1, y + 1)]);
            }
            // ####
            RockType::Row => {
                // move accord to stream
                match stream {
                    Stream::Left => {
                        if x != 0 && !chamber.contains(&(x - 1, y)) {
                            x -= 1;
                        }
                    }
                    Stream::Right => {
                        if x != 3 && !chamber.contains(&(x + 4, y)) {
                            x += 1;
                        }
                    }
                }

                // falls
                // return new pos
                if y != 0
                    && !chamber.contains(&(x, y - 1))
                    && !chamber.contains(&(x + 1, y - 1))
                    && !chamber.contains(&(x + 2, y - 1))
                    && !chamber.contains(&(x + 3, y - 1))
                {
                    return Some((x, y - 1));
                }
                chamber.extend([(x, y), (x + 1, y), (x + 2, y), (x + 3, y)]);
            }
        }

        None
    }
}

const ROCKS: [RockType; 5] = [
    RockType::Row,
    RockType::Plus,
    RockType::InvertedL,
    RockType::Line,
    RockType::Square,
];

pub fn part1(input: &str) -> u64 {
    let mut stoped_rocks = 0;

    let mut chamber: HashSet<(u64, u64)> = HashSet::new();

    let mut stream_directions = input
        .trim_end()
        .as_bytes()
        .iter()
        .map(|ch| match ch {
            b'<' => Stream::Left,
            b'>' => Stream::Right,
            _ => unreachable!(),
        })
        .cycle();

    'outer: for rock in ROCKS.into_iter().cycle() {
        let highest_y_coord = chamber.iter().map(|(_, y)| *y).max();
        let mut curr_rock_location = match highest_y_coord {
            Some(y) => (2, y + 4),
            None => (2, 3),
        };

        for stream in &mut stream_directions {
            if stoped_rocks == 2022 {
                break 'outer;
            }

            if let Some(new_location) =
                rock.advance_simulation(&mut chamber, stream, curr_rock_location)
            {
                curr_rock_location = new_location;
            } else {
                stoped_rocks += 1;
                break;
            };
        }
    }

    chamber.into_iter().map(|(_, y)| y).max().unwrap() + 1
}

pub fn part2(input: &str) -> u64 {
    let mut stoped_rocks: u64 = 0;

    let mut chamber: HashSet<(u64, u64)> = HashSet::new();

    let mut stream_directions = input
        .trim_end()
        .as_bytes()
        .iter()
        .map(|ch| match ch {
            b'<' => Stream::Left,
            b'>' => Stream::Right,
            _ => unreachable!(),
        })
        .enumerate()
        .cycle();

    let mut previous_hashes = HashMap::new();
    let mut extra = 0;
    'outer: for rock in ROCKS.into_iter().cycle() {
        let highest_y_coord = chamber.iter().map(|(_, y)| *y).max();
        let mut curr_rock_location = match highest_y_coord {
            Some(y) => (2, y + 4),
            None => (2, 3),
        };

        for (stream_idx, stream) in &mut stream_directions {
            if stoped_rocks == 1_000_000_000_000 {
                break 'outer;
            }

            if let Some(new_location) =
                rock.advance_simulation(&mut chamber, stream, curr_rock_location)
            {
                curr_rock_location = new_location;
            } else {
                // optimization
                let highest_y_coord = chamber.iter().map(|(_, y)| *y).max().unwrap();
                let chamber_hash = (
                    stoped_rocks % 5,
                    stream_idx,
                    chamber
                        .iter()
                        .filter_map(|&(x, y)| {
                            (y >= highest_y_coord.saturating_sub(32))
                                .then_some((x, highest_y_coord - y))
                        })
                        .unique()
                        .sorted()
                        .collect_vec(),
                );
                if stoped_rocks >= 2022 {
                    if let Some((prev_stoped_rocks, prev_highest_y_coord)) =
                        previous_hashes.get(&chamber_hash)
                    {
                        let d_y = highest_y_coord - prev_highest_y_coord;
                        let d_stoped = stoped_rocks - prev_stoped_rocks;

                        let repeated_cycles = (1_000_000_000_000 - stoped_rocks) / d_stoped;

                        extra += repeated_cycles * d_y;

                        stoped_rocks += repeated_cycles * d_stoped;
                    }
                    previous_hashes.insert(chamber_hash, (stoped_rocks, highest_y_coord));
                }
                // end optimization
                stoped_rocks += 1;
                break;
            };
        }
    }

    chamber.into_iter().map(|(_, y)| y).max().unwrap() + 1 + extra
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>";

    #[test]
    fn part1_works() {
        let output = 3068;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    fn part2_works() {
        let output = 1_514_285_714_288;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

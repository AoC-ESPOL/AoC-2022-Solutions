#![allow(unused)]

use bstr::ByteSlice;
use itertools::Itertools;
use ndarray::{array, s, Array2};
use nom::{
    branch::alt,
    bytes::complete::{is_not, tag},
    character::complete::{alpha1, anychar, digit1, i32, newline, u32, u64},
    combinator::{map, value},
    multi::{many1, separated_list0},
    sequence::{delimited, preceded, terminated, tuple},
    IResult,
};
use petgraph::{
    algo::{all_simple_paths, toposort},
    prelude::*,
};
// 200x150

const D: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];
pub fn part1(input: &str) -> usize {
    let (board, passwd) = input.split_once("\n\n").unwrap();
    let (board, mut curr_position) = parse_board(board);
    let passwd = parse_passwd(passwd).unwrap().1;
    let mut facing: i8 = 0;

    for mv in passwd {
        match mv {
            Move::ClockWise => facing = (facing + 1) % 4,
            Move::CounterCW => facing = (facing - 1).rem_euclid(4),
            Move::Steps(n) => {
                for _ in 0..n {
                    let (dx, dy) = D[facing as usize];
                    let (x, y) = (curr_position.0 as i32 + dx, curr_position.1 as i32 + dy);

                    if let Some(chr) = board.get([x as usize, y as usize]) {
                        match chr {
                            0 => (), // has to wrap if possible
                            1 => {
                                curr_position = (x as usize, y as usize);
                                continue;
                            } // ok to move
                            2 => break, // has to stop
                            _ => unreachable!(),
                        }
                    }

                    match facing {
                        0 => {
                            let min_y = board
                                .slice(s![x, ..])
                                .into_iter()
                                .position(|&t| t != 0)
                                .unwrap();

                            if let Some(chr) = board.get([x as usize, min_y]) {
                                match chr {
                                    1 => {
                                        curr_position = (x as usize, min_y);
                                        continue;
                                    } // ok to move
                                    2 => break, // has to stop
                                    _ => unreachable!(),
                                }
                            };
                        } // wrap to min h if possible
                        1 => {
                            let min_x = board
                                .slice(s![.., y])
                                .into_iter()
                                .position(|&t| t != 0)
                                .unwrap();

                            if let Some(chr) = board.get([min_x, y as usize]) {
                                match chr {
                                    1 => {
                                        curr_position = (min_x, y as usize);
                                        continue;
                                    } // ok to move
                                    2 => break, // has to stop
                                    _ => unreachable!(),
                                }
                            };
                        } // wrap to min vert if possible
                        2 => {
                            let max_y = 149
                                - board
                                    .slice(s![x, ..])
                                    .into_iter()
                                    .rev()
                                    .position(|&t| t != 0)
                                    .unwrap();

                            if let Some(chr) = board.get([x as usize, max_y]) {
                                match chr {
                                    1 => {
                                        curr_position = (x as usize, max_y);
                                        continue;
                                    } // ok to move
                                    2 => break, // has to stop
                                    _ => unreachable!(),
                                }
                            };
                        } // wrap to max h if possible
                        3 => {
                            let max_x = 199
                                - board
                                    .slice(s![.., y])
                                    .into_iter()
                                    .rev()
                                    .position(|&t| t != 0)
                                    .unwrap();

                            if let Some(chr) = board.get([max_x, y as usize]) {
                                match chr {
                                    1 => {
                                        curr_position = (max_x, y as usize);
                                        continue;
                                    } // ok to move
                                    2 => break, // has to stop
                                    _ => unreachable!(),
                                }
                            };
                        } // wrap to max vert if possible
                        _ => unreachable!(),
                    };
                }
            }
        }
    }

    1000 * (curr_position.0 + 1) + 4 * (curr_position.1 + 1) + facing as usize
}

fn parse_passwd(passwd: &str) -> IResult<&str, Vec<Move>> {
    many1(alt((
        map(i32, Move::Steps),
        value(Move::ClockWise, tag("R")),
        value(Move::CounterCW, tag("L")),
    )))(passwd)
}

#[derive(Debug, Clone)]
enum Move {
    Steps(i32),
    ClockWise,
    CounterCW,
}

pub fn part2(input: &str) -> usize {
    let (board, passwd) = input.split_once("\n\n").unwrap();
    let (board, mut curr_position) = parse_board(board);
    let passwd = parse_passwd(passwd).unwrap().1;
    let mut facing: i8 = 0;

    for mv in passwd {
        match mv {
            Move::ClockWise => facing = (facing + 1) % 4,
            Move::CounterCW => facing = (facing - 1).rem_euclid(4),
            Move::Steps(n) => {
                for _ in 0..n {
                    let (dx, dy) = D[facing as usize];
                    let (x, y) = (curr_position.0 as i32 + dx, curr_position.1 as i32 + dy);

                    if let Some(chr) = board.get([x as usize, y as usize]) {
                        match chr {
                            0 => (), // has to wrap if possible
                            1 => {
                                curr_position = (x as usize, y as usize);
                                continue;
                            } // ok to move
                            2 => break, // has to stop
                            _ => unreachable!(),
                        }
                    }

                    if x == -1 && (50..100).contains(&y) && facing == 3 {
                        if let Some(chr) = board.get([y as usize + 100, 0]) {
                            match chr {
                                1 => {
                                    curr_position = (y as usize + 100, 0);
                                    facing = 0;
                                    continue;
                                } // ok to move
                                2 => break, // has to stop
                                _ => unreachable!(),
                            }
                        }
                    } else if y == -1 && (150..200).contains(&x) && facing == 2 {
                        if let Some(chr) = board.get([0, x as usize - 100]) {
                            match chr {
                                1 => {
                                    curr_position = (0, x as usize - 100);
                                    facing = 1;
                                    continue;
                                } // ok to move
                                2 => break, // has to stop
                                _ => unreachable!(),
                            }
                        }
                    } else if x == -1 && (100..150).contains(&y) && facing == 3 {
                        if let Some(chr) = board.get([199, y as usize - 100]) {
                            match chr {
                                1 => {
                                    curr_position = (199, y as usize - 100);
                                    continue;
                                } // ok to move
                                2 => break, // has to stop
                                _ => unreachable!(),
                            }
                        }
                    } else if x == 200 && (0..50).contains(&y) && facing == 1 {
                        if let Some(chr) = board.get([0, y as usize + 100]) {
                            match chr {
                                1 => {
                                    curr_position = (0, y as usize + 100);
                                    continue;
                                } // ok to move
                                2 => break, // has to stop
                                _ => unreachable!(),
                            }
                        }
                    } else if y == 150 && (0..50).contains(&x) && facing == 0 {
                        if let Some(chr) = board.get([149 - x as usize, 99]) {
                            match chr {
                                1 => {
                                    curr_position = (149 - x as usize, 99);
                                    facing = 2;
                                    continue;
                                } // ok to move
                                2 => break, // has to stop
                                _ => unreachable!(),
                            }
                        }
                    } else if y == 100 && (100..150).contains(&x) && facing == 0 {
                        if let Some(chr) = board.get([149 - x as usize, 149]) {
                            match chr {
                                1 => {
                                    curr_position = (149 - x as usize, 149);
                                    facing = 2;
                                    continue;
                                } // ok to move
                                2 => break, // has to stop
                                _ => unreachable!(),
                            }
                        }
                    } else if x == 50 && (100..150).contains(&y) && facing == 1 {
                        if let Some(chr) = board.get([y as usize - 50, 99]) {
                            match chr {
                                1 => {
                                    curr_position = (y as usize - 50, 99);
                                    facing = 2;
                                    continue;
                                } // ok to move
                                2 => break, // has to stop
                                _ => unreachable!(),
                            }
                        }
                    } else if y == 100 && (50..100).contains(&x) && facing == 0 {
                        if let Some(chr) = board.get([49, x as usize + 50]) {
                            match chr {
                                1 => {
                                    curr_position = (49, x as usize + 50);
                                    facing = 3;
                                    continue;
                                } // ok to move
                                2 => break, // has to stop
                                _ => unreachable!(),
                            }
                        }
                    } else if y == 49 && (0..50).contains(&x) && facing == 2 {
                        if let Some(chr) = board.get([149 - x as usize, 0]) {
                            match chr {
                                1 => {
                                    curr_position = (149 - x as usize, 0);
                                    facing = 0;
                                    continue;
                                } // ok to move
                                2 => break, // has to stop
                                _ => unreachable!(),
                            }
                        }
                    } else if y == -1 && (100..150).contains(&x) && facing == 2 {
                        if let Some(chr) = board.get([149 - x as usize, 50]) {
                            match chr {
                                1 => {
                                    curr_position = (149 - x as usize, 50);
                                    facing = 0;
                                    continue;
                                } // ok to move
                                2 => break, // has to stop
                                _ => unreachable!(),
                            }
                        }
                    } else if y == 49 && (50..100).contains(&x) && facing == 2 {
                        if let Some(chr) = board.get([100, x as usize - 50]) {
                            match chr {
                                1 => {
                                    curr_position = (100, x as usize - 50);
                                    facing = 1;
                                    continue;
                                } // ok to move
                                2 => break, // has to stop
                                _ => unreachable!(),
                            }
                        }
                    } else if x == 99 && (0..50).contains(&y) && facing == 3 {
                        if let Some(chr) = board.get([y as usize + 50, 50]) {
                            match chr {
                                1 => {
                                    curr_position = (y as usize + 50, 50);
                                    facing = 0;
                                    continue;
                                } // ok to move
                                2 => break, // has to stop
                                _ => unreachable!(),
                            }
                        }
                    } else if x == 150 && (50..100).contains(&y) && facing == 1 {
                        if let Some(chr) = board.get([y as usize + 100, 49]) {
                            match chr {
                                1 => {
                                    curr_position = (y as usize + 100, 49);
                                    facing = 2;
                                    continue;
                                } // ok to move
                                2 => break, // has to stop
                                _ => unreachable!(),
                            }
                        }
                    } else if y == 50 && (150..200).contains(&x) && facing == 0 {
                        if let Some(chr) = board.get([149, x as usize - 100]) {
                            match chr {
                                1 => {
                                    curr_position = (149, x as usize - 100);
                                    facing = 3;
                                    continue;
                                } // ok to move
                                2 => break, // has to stop
                                _ => unreachable!(),
                            }
                        }
                    } else {
                        unreachable!()
                    }
                }
            }
        }
    }

    1000 * (curr_position.0 + 1) + 4 * (curr_position.1 + 1) + facing as usize
}

fn parse_board(input: &str) -> (Array2<i8>, (usize, usize)) {
    let mut gr = Array2::zeros((200, 150));
    let mut start = None;

    for (x, line) in input.lines().enumerate() {
        for (y, chr) in line.chars().enumerate() {
            if start.is_none() && chr != ' ' {
                start = Some((x, y))
            }
            gr[[x, y]] = match chr {
                ' ' => 0,
                '.' => 1,
                '#' => 2,
                _ => unreachable!(),
            };
        }
    }
    (gr, start.unwrap())
}

// #[cfg(test)]
// mod tests {
//     use super::{part1, part2};

//     const TEST_INPUT: &str = "\
//     ...#
//     .#..
//     #...
//     ....
// ...#.......#
// ........#...
// ..#....#....
// ..........#.
//     ...#....
//     .....#..
//     .#......
//     ......#.

// 10R5L5R10L4R5L5";

//     #[test]
//     fn part1_works() {
//         let output = 6032;

//         assert_eq!(part1(TEST_INPUT), output);
//     }

//     // #[test]
//     // fn part2_works() {
//     //     let output = 55267;

//     //     assert_eq!(part2(TEST_INPUT), output);
//     // }
// }

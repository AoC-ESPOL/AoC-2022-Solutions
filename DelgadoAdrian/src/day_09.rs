#![allow(unused)]

use std::collections::HashSet;

use bstr::ByteSlice;
use itertools::Itertools;
use ndarray::{array, s, Array2};
use nom::{
    branch::alt,
    bytes::complete::{is_not, tag},
    character::complete::{alpha1, digit1, i64, u32},
    combinator::value,
    sequence::{delimited, preceded, separated_pair, terminated, tuple},
    IResult,
};
use petgraph::{
    algo::{all_simple_paths, toposort},
    prelude::*,
};

pub fn part1(input: &str) -> usize {
    let mut positions_tail = HashSet::new();
    let mut head = [0_i64, 0];
    let mut tail = [0_i64, 0];
    for (dir, n) in input.lines().map(|line| parse_line(line).unwrap().1) {
        for _ in 0..n {
            match dir {
                Dir::Up => {
                    head[1] += 1;
                }
                Dir::Down => {
                    head[1] -= 1;
                }
                Dir::Left => {
                    head[0] -= 1;
                }
                Dir::Right => {
                    head[0] += 1;
                }
            }
            let dx = head[0] - tail[0];
            let dy = head[1] - tail[1];
            let direction = [dx.signum(), dy.signum()];
            let too_far = dx * dx + dy * dy > 2;
            if too_far {
                match direction {
                    [1, 0] => tail[0] += 1,
                    [1, 1] => {
                        tail[0] += 1;
                        tail[1] += 1
                    }
                    [0, 1] => tail[1] += 1,
                    [-1, 1] => {
                        tail[0] -= 1;
                        tail[1] += 1;
                    }
                    [-1, 0] => tail[0] -= 1,
                    [-1, -1] => {
                        tail[0] -= 1;
                        tail[1] -= 1;
                    }
                    [0, -1] => tail[1] -= 1,
                    [1, -1] => {
                        tail[0] += 1;
                        tail[1] -= 1;
                    }
                    _ => (),
                }
            }
            positions_tail.insert(tail);
        }
    }
    positions_tail.len()
}

pub fn part2(input: &str) -> usize {
    let mut positions_tail = HashSet::new();
    let mut snake = [[0_i64, 0_i64]; 10]; // head 0, tail 9
    for (dir, n) in input.lines().map(|line| parse_line(line).unwrap().1) {
        for _ in 0..n {
            match dir {
                Dir::Up => {
                    snake[0][1] += 1;
                }
                Dir::Down => {
                    snake[0][1] -= 1;
                }
                Dir::Left => {
                    snake[0][0] -= 1;
                }
                Dir::Right => {
                    snake[0][0] += 1;
                }
            }

            for idx in 0..snake.len() - 1 {
                let dx = snake[idx][0] - snake[idx + 1][0];
                let dy = snake[idx][1] - snake[idx + 1][1];
                let direction = [dx.signum(), dy.signum()];
                let too_far = dx * dx + dy * dy > 2;
                if too_far {
                    match direction {
                        [1, 0] => snake[idx + 1][0] += 1,
                        [1, 1] => {
                            snake[idx + 1][0] += 1;
                            snake[idx + 1][1] += 1
                        }
                        [0, 1] => snake[idx + 1][1] += 1,
                        [-1, 1] => {
                            snake[idx + 1][0] -= 1;
                            snake[idx + 1][1] += 1;
                        }
                        [-1, 0] => snake[idx + 1][0] -= 1,
                        [-1, -1] => {
                            snake[idx + 1][0] -= 1;
                            snake[idx + 1][1] -= 1;
                        }
                        [0, -1] => snake[idx + 1][1] -= 1,
                        [1, -1] => {
                            snake[idx + 1][0] += 1;
                            snake[idx + 1][1] -= 1;
                        }
                        _ => (),
                    }
                }
            }

            positions_tail.insert(snake[9]);
        }
    }
    positions_tail.len()
}

fn parse_line(input: &str) -> IResult<&str, (Dir, i64)> {
    let (rest, pair) = separated_pair(
        alt((
            value(Dir::Up, tag("U")),
            value(Dir::Down, tag("D")),
            value(Dir::Left, tag("L")),
            value(Dir::Right, tag("R")),
        )),
        tag(" "),
        i64,
    )(input)?;
    Ok((rest, pair))
}

#[derive(Debug, Clone, Copy)]
enum Dir {
    Up,
    Down,
    Left,
    Right,
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2";
    const TEST_INPUT_2: &str = "\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 13;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 36;

        assert_eq!(part2(TEST_INPUT_2), output);
    }
}

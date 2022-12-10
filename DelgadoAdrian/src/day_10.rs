#![allow(unused)]

use bstr::ByteSlice;
use itertools::Itertools;
use ndarray::{array, s, Array2};
use nom::{
    branch::alt,
    bytes::complete::{is_not, tag},
    character::complete::{alpha1, digit1, i64, u32},
    combinator::{map, value},
    sequence::{delimited, preceded, separated_pair, terminated, tuple},
    IResult,
};
use petgraph::{
    algo::{all_simple_paths, toposort},
    prelude::*,
};

pub fn part1(input: &str) -> i64 {
    let mut x = 1;
    let mut cycle = 1;
    let mut strength = 0;
    let check = [20, 60, 100, 140, 180, 220];
    for op in input.lines().map(|line| parse_line(line).unwrap().1) {
        cycle += 1;
        match op {
            Op::Noop => {}
            Op::Addx(n) => {
                if check.contains(&cycle) {
                    strength += x * cycle;
                }
                cycle += 1;
                x += n;
            }
        }
        if check.contains(&cycle) {
            strength += x * cycle;
        }
    }

    strength
}

pub fn part2(input: &str) -> i64 {
    // 40 wide and 6 high
    let mut x = 1;
    let mut cycle = 1;
    let mut strength = 0;
    let check = [20, 60, 100, 140, 180, 220];
    let mut to_print = [[' '; 40]; 6];
    for op in input.lines().map(|line| parse_line(line).unwrap().1) {
        if ((cycle - 1) % 40_i64).abs_diff(x) < 2 {
            to_print[(cycle as usize - 1) / 40][(cycle as usize - 1) % 40] = '#'
        }
        cycle += 1;
        match op {
            Op::Noop => {}
            Op::Addx(n) => {
                if check.contains(&cycle) {
                    strength += x * cycle;
                }
                if ((cycle - 1) % 40_i64).abs_diff(x) < 2 {
                    to_print[(cycle as usize - 1) / 40][(cycle as usize - 1) % 40] = '#'
                }
                cycle += 1;
                x += n;
            }
        }
        if check.contains(&cycle) {
            strength += x * cycle;
        }
    }
    for row in to_print {
        println!("{}", row.into_iter().collect::<String>());
    }
    strength
}

fn parse_line(input: &str) -> IResult<&str, Op> {
    alt((
        map(preceded(tag("addx "), i64), Op::Addx),
        value(Op::Noop, tag("noop")),
    ))(input)
}
#[derive(Debug, Clone, Copy)]
enum Op {
    Noop,
    Addx(i64),
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop";

    #[test]
    fn part1_works() {
        let output = 13140;

        assert_eq!(part1(TEST_INPUT), output);
    }

    // #[test]
    // fn part2_works() {
    //     let output = 45000.to_string();

    //     assert_eq!(part2(TEST_INPUT), output);
    // }
}

#![allow(unused)]

use std::collections::HashSet;

use bstr::ByteSlice;
use itertools::Itertools;
use ndarray::{array, s, Array2};
use nom::{
    branch::alt,
    bytes::complete::{is_not, tag},
    character::complete::{alpha1, digit1, i64, newline, u32, u64},
    combinator::{map, value},
    multi::separated_list0,
    sequence::{delimited, preceded, separated_pair, terminated, tuple},
    IResult,
};
use petgraph::{
    algo::{all_simple_paths, toposort},
    prelude::*,
};

pub fn part1(input: &str) -> usize {
    // 460-537, 15-161

    let mut cave = HashSet::new();
    for scan in input.lines().map(|line| parse_line(line).unwrap().1) {
        for line in scan.windows(2) {
            let [(x1, y1), (x2, y2)] = *line else { unreachable!() };
            if x1 == x2 {
                for y in y1.min(y2)..=y2.max(y1) {
                    cave.insert((x1, y));
                }
            } else {
                for x in x1.min(x2)..=x2.max(x1) {
                    cave.insert((x, y1));
                }
            }
        }
    }

    let amount_rocks = cave.len();

    let max_y = cave.iter().map(|(_, y)| *y).max().unwrap();

    loop {
        // if cave.contains(&(500, 0)) {
        //     return cave.len() - amount_rocks;
        // }
        let mut curr_x = 500;
        let mut curr_y = 0;
        loop {
            if curr_y > max_y {
                return cave.len() - amount_rocks;
            }

            if !cave.contains(&(curr_x, curr_y + 1)) {
                curr_y += 1;
            } else if !cave.contains(&(curr_x - 1, curr_y + 1)) {
                curr_y += 1;
                curr_x -= 1;
            } else if !cave.contains(&(curr_x + 1, curr_y + 1)) {
                curr_y += 1;
                curr_x += 1;
            } else {
                cave.insert((curr_x, curr_y));
                break;
            }
        }
    }
}

pub fn part2(input: &str) -> usize {
    // 460-537, 15-161

    let mut cave = HashSet::new();
    for scan in input.lines().map(|line| parse_line(line).unwrap().1) {
        for line in scan.windows(2) {
            let [(x1, y1), (x2, y2)] = *line else { unreachable!() };
            if x1 == x2 {
                for y in y1.min(y2)..=y2.max(y1) {
                    cave.insert((x1, y));
                }
            } else {
                for x in x1.min(x2)..=x2.max(x1) {
                    cave.insert((x, y1));
                }
            }
        }
    }

    let amount_rocks = cave.len();

    let max_y = cave.iter().map(|(_, y)| *y).max().unwrap();

    loop {
        if cave.contains(&(500, 0)) {
            return cave.len() - amount_rocks;
        }
        let mut curr_x = 500;
        let mut curr_y = 0;
        loop {
            if curr_y > max_y {
                cave.insert((curr_x, curr_y));
                break;
            }

            if !cave.contains(&(curr_x, curr_y + 1)) {
                curr_y += 1;
            } else if !cave.contains(&(curr_x - 1, curr_y + 1)) {
                curr_y += 1;
                curr_x -= 1;
            } else if !cave.contains(&(curr_x + 1, curr_y + 1)) {
                curr_y += 1;
                curr_x += 1;
            } else {
                cave.insert((curr_x, curr_y));
                break;
            }
        }
    }
}

fn parse_line(input: &str) -> IResult<&str, Vec<(u32, u32)>> {
    separated_list0(tag(" -> "), separated_pair(u32, tag(","), u32))(input)
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9";

    #[test]
    fn part1_works() {
        let output = 24;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    fn part2_works() {
        let output = 93;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

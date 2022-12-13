#![allow(unused)]

use std::cmp::Ordering;

use bstr::ByteSlice;
use itertools::Itertools;
use ndarray::{array, s, Array2};
use nom::{
    branch::alt,
    bytes::complete::{is_not, tag},
    character::complete::{alpha1, digit1, i64, newline, u32, u64},
    combinator::{map, value},
    multi::{separated_list0, separated_list1},
    sequence::{delimited, preceded, separated_pair, terminated, tuple},
    IResult,
};
use petgraph::{
    algo::{all_simple_paths, toposort},
    prelude::*,
};

pub fn part1(input: &str) -> usize {
    let mut right_order = 0;
    for (i, (p1, p2)) in input
        .split("\n\n")
        .map(|line| parse_line(line).unwrap().1)
        .enumerate()
    {
        if compare_packets(&p1, &p2) == Ordering::Less {
            right_order += i + 1;
        }
    }

    right_order
}

fn compare_packets(p1: &[Data], p2: &[Data]) -> Ordering {
    for pair in std::iter::zip(p1, p2) {
        let order = match pair {
            (Data::Integer(i1), Data::Integer(i2)) => i1.cmp(i2),
            (Data::Integer(n), Data::List(v)) => compare_packets(&[Data::Integer(*n)], v),
            (Data::List(v), Data::Integer(n)) => compare_packets(v, &[Data::Integer(*n)]),
            (Data::List(v1), Data::List(v2)) => compare_packets(v1, v2),
        };

        if order != Ordering::Equal {
            return order;
        }
    }

    p1.len().cmp(&p2.len())
}

pub fn part2(input: &str) -> usize {
    let mut packets: Vec<_> = input
        .split("\n\n")
        .flat_map(str::lines)
        .map(|line| parse_vec(line).unwrap().1)
        .collect();

    let divider_1 = vec![Data::List(vec![Data::Integer(2)])];
    packets.push(divider_1);
    let divider_2 = vec![Data::List(vec![Data::Integer(6)])];
    packets.push(divider_2);

    packets.sort_unstable_by(|v1, v2| compare_packets(v1, v2));

    packets
        .into_iter()
        .zip(1..)
        .filter(|(ref p, _)| {
            p == &vec![Data::List(vec![Data::Integer(2)])]
                || p == &vec![Data::List(vec![Data::Integer(6)])]
        })
        .map(|(_, idx)| idx)
        .product()
}

fn parse_line(input: &str) -> IResult<&str, (Vec<Data>, Vec<Data>)> {
    separated_pair(parse_vec, newline, parse_vec)(input)
}

fn parse_vec(input: &str) -> IResult<&str, Vec<Data>> {
    delimited(
        tag("["),
        separated_list0(
            tag(","),
            alt((map(u32, Data::Integer), map(parse_vec, Data::List))),
        ),
        tag("]"),
    )(input)
}

#[derive(Debug, Clone, PartialEq)]
enum Data {
    Integer(u32),
    List(Vec<Data>),
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]";

    #[test]
    fn part1_works() {
        let output = 13;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    fn part2_works() {
        let output = 140;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

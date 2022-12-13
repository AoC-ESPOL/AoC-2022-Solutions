use std::cmp::Ordering;

use itertools::Itertools;
use nom::{
    branch::alt,
    bytes::complete::tag,
    character::complete::{newline, u32},
    combinator::map,
    multi::separated_list0,
    sequence::{delimited, separated_pair},
    IResult,
};

pub fn part1(input: &str) -> usize {
    input
        .split("\n\n")
        .map(|line| parse_pair(line).unwrap().1)
        .zip(1..)
        .filter(|((p1, p2), _)| cmp_packets(p1, p2) == Ordering::Less)
        .map(|(_, idx)| idx)
        .sum()
}

pub fn part2(input: &str) -> usize {
    input
        .split("\n\n")
        .flat_map(str::lines)
        .chain(["[[2]]", "[[6]]"])
        .map(|line| parse_vec(line).unwrap().1)
        .sorted_unstable_by(|v1, v2| cmp_packets(v1, v2))
        .zip(1..)
        .filter(
            |(p, _)| matches!(&p[..], [Data::List(l)] if matches!(l[..], [Data::Integer(2 | 6)])),
        )
        .map(|(_, idx)| idx)
        .product()
}

fn parse_pair(input: &str) -> IResult<&str, (Vec<Data>, Vec<Data>)> {
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

fn cmp_packets(p1: &[Data], p2: &[Data]) -> Ordering {
    std::iter::zip(p1, p2)
        .map(|pair| match pair {
            (Data::Integer(int_1), Data::Integer(int_2)) => int_1.cmp(int_2),
            (Data::Integer(int), Data::List(l)) => cmp_packets(&[Data::Integer(*int)], l),
            (Data::List(l), Data::Integer(int)) => cmp_packets(l, &[Data::Integer(*int)]),
            (Data::List(l_1), Data::List(l_2)) => cmp_packets(l_1, l_2),
        })
        .find(|&order| order != Ordering::Equal)
        .unwrap_or_else(|| p1.len().cmp(&p2.len()))
}

#[derive(Debug)]
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
    #[ignore]
    fn part1_works() {
        let output = 13;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 140;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

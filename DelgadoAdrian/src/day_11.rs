#![allow(unused)]

use std::{collections::VecDeque, vec};

use bstr::ByteSlice;
use itertools::Itertools;
use ndarray::{array, s, Array2};
use nom::{
    branch::alt,
    bytes::complete::{is_not, tag},
    character::complete::{alpha1, digit1, i64, u64},
    combinator::{map, value},
    multi::{many1, separated_list1},
    sequence::{delimited, preceded, terminated, tuple},
    IResult,
};
use petgraph::{
    algo::{all_simple_paths, toposort},
    prelude::*,
};

pub fn part1(input: &str) -> u64 {
    let mut vec_monkeys: Vec<_> = input
        .split("\n\n")
        .map(|line| parse_block(line).unwrap().1)
        .collect();

    for _ in 0..20 {
        for i in 0..vec_monkeys.len() {
            while let Some(item) = vec_monkeys[i].starting_items.pop_front() {
                let worry = match vec_monkeys[i].operation {
                    Op::Add(n) => (item + n),
                    Op::Mul(n) => (item * n),
                    Op::MulOld => (item * item),
                } / 3;

                vec_monkeys[i].inspections += 1;
                let test = worry % vec_monkeys[i].divisible_by == 0;
                if test {
                    let idx = vec_monkeys[i].if_true;

                    vec_monkeys[idx].starting_items.push_back(worry);
                } else {
                    let idx = vec_monkeys[i].if_false;

                    vec_monkeys[idx].starting_items.push_back(worry);
                };
            }
        }
        // for m in &mut vec_monkeys {
        //     println!(
        //         "M {}: {:?}",
        //         m.monkey_num,
        //         m.starting_items.make_contiguous()
        //     );
        // }
    }

    vec_monkeys.sort_by_key(|m| m.inspections);
    vec_monkeys.reverse();
    let [a,b,..] = &vec_monkeys[..] else { unreachable!()};
    // println!("{a:?}");
    // println!("{b:?}");
    a.inspections * b.inspections
}

pub fn part2(input: &str) -> u64 {
    let mut vec_monkeys: Vec<_> = input
        .split("\n\n")
        .map(|line| parse_block(line).unwrap().1)
        .collect();

    let common_mul: u64 = vec_monkeys.iter().map(|m| m.divisible_by).product();

    for _ in 0..10_000 {
        for i in 0..vec_monkeys.len() {
            while let Some(item) = vec_monkeys[i].starting_items.pop_front() {
                let worry = match vec_monkeys[i].operation {
                    Op::Add(n) => (item + n),
                    Op::Mul(n) => (item * n),
                    Op::MulOld => (item * item),
                } % common_mul;

                vec_monkeys[i].inspections += 1;
                let test = worry % vec_monkeys[i].divisible_by == 0;
                if test {
                    let idx = vec_monkeys[i].if_true;

                    vec_monkeys[idx].starting_items.push_back(worry);
                } else {
                    let idx = vec_monkeys[i].if_false;

                    vec_monkeys[idx].starting_items.push_back(worry);
                };
            }
        }
        // for m in &mut vec_monkeys {
        //     println!(
        //         "M {}: {:?}",
        //         m.monkey_num,
        //         m.starting_items.make_contiguous()
        //     );
        // }
    }

    vec_monkeys.sort_by_key(|m| m.inspections);
    vec_monkeys.reverse();
    let [a,b,..] = &vec_monkeys[..] else { unreachable!()};
    // println!("{a:?}");
    // println!("{b:?}");
    a.inspections * b.inspections
}

fn parse_block(input: &str) -> IResult<&str, Monkey> {
    let (input, monkey_num) = delimited(tag("Monkey "), u64, tag(":\n"))(input)?;
    let (input, starting_items) = delimited(
        tag("  Starting items: "),
        separated_list1(tag(", "), u64),
        tag("\n"),
    )(input)?;
    let (input, operation) = delimited(
        tag("  Operation: new = old "),
        alt((
            map(preceded(tag("* "), u64), Op::Mul),
            map(preceded(tag("+ "), u64), Op::Add),
            value(Op::MulOld, tag("* old")),
        )),
        tag("\n"),
    )(input)?;
    let (input, divisible_by) = delimited(tag("  Test: divisible by "), u64, tag("\n"))(input)?;
    let (input, if_true) = delimited(tag("    If true: throw to monkey "), u64, tag("\n"))(input)?;
    let (input, if_false) = preceded(tag("    If false: throw to monkey "), u64)(input)?;
    Ok((
        input,
        Monkey {
            monkey_num,
            starting_items: starting_items.into(),
            operation,
            divisible_by,
            if_true: if_true as _,
            if_false: if_false as _,
            inspections: 0,
        },
    ))
}

#[derive(Debug, Clone)]
struct Monkey {
    monkey_num: u64,
    starting_items: VecDeque<u64>,
    operation: Op,
    divisible_by: u64,
    if_true: usize,
    if_false: usize,
    inspections: u64,
}

#[derive(Debug, Clone)]
enum Op {
    Add(u64),
    Mul(u64),
    MulOld,
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1";

    #[test]
    fn part1_works() {
        let output = 10605;

        assert_eq!(part1(TEST_INPUT), output);
    }

    // #[test]
    // fn part2_works() {
    //     let output = 45000.to_string();

    //     assert_eq!(part2(TEST_INPUT), output);
    // }
}

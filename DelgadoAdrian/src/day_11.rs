use std::collections::VecDeque;

use nom::{
    branch::alt,
    bytes::complete::tag,
    character::complete::{digit1, newline, u32, u64},
    combinator::{map, value},
    multi::separated_list1,
    sequence::{delimited, preceded, tuple},
    IResult,
};

fn monkey_business<const LARGE: bool>(input: &str) -> usize {
    let mut monkeys: Vec<_> = input
        .split("\n\n")
        .map(|line| parse_block(line).unwrap().1)
        .collect();

    let common_mul: u64 = monkeys.iter().map(|m| m.divisible_test).product();

    for _ in 0..(if LARGE { 10_000 } else { 20 }) {
        for i in 0..monkeys.len() {
            monkeys[i].inspections += monkeys[i].starting_items.len();

            while let Some(item) = monkeys[i].starting_items.pop_front() {
                let worry = match monkeys[i].operation {
                    Op::Add(n) => item + n,
                    Op::Mul(n) => item * n,
                    Op::MulOld => item * item,
                };

                let worry = if LARGE { worry % common_mul } else { worry / 3 };

                let throw = if worry % monkeys[i].divisible_test == 0 {
                    monkeys[i].if_true
                } else {
                    monkeys[i].if_false
                };

                monkeys[throw].starting_items.push_back(worry);
            }
        }
    }

    monkeys.sort_unstable_by_key(|m| m.inspections);

    monkeys
        .into_iter()
        .rev()
        .take(2)
        .map(|m| m.inspections)
        .product()
}

pub fn part1(input: &str) -> usize {
    monkey_business::<false>(input)
}

pub fn part2(input: &str) -> usize {
    monkey_business::<true>(input)
}

fn parse_block(input: &str) -> IResult<&str, Monkey> {
    let (input, (starting_items, operation, divisible_by, if_true, if_false)) = tuple((
        delimited(
            tuple((tag("Monkey "), digit1, tag(":\n  Starting items: "))),
            separated_list1(tag(", "), u64),
            newline,
        ),
        delimited(
            tag("  Operation: new = old "),
            alt((
                map(preceded(tag("* "), u64), Op::Mul),
                map(preceded(tag("+ "), u64), Op::Add),
                value(Op::MulOld, tag("* old")),
            )),
            newline,
        ),
        delimited(tag("  Test: divisible by "), u64, newline),
        delimited(tag("    If true: throw to monkey "), u32, newline),
        preceded(tag("    If false: throw to monkey "), u32),
    ))(input)?;

    Ok((
        input,
        Monkey {
            starting_items: VecDeque::from(starting_items),
            operation,
            divisible_test: divisible_by,
            if_true: if_true as usize,
            if_false: if_false as usize,
            inspections: 0,
        },
    ))
}

#[derive(Debug, Clone)]
struct Monkey {
    starting_items: VecDeque<u64>,
    operation: Op,
    divisible_test: u64,
    if_true: usize,
    if_false: usize,
    inspections: usize,
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
        let output = 10_605;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    fn part2_works() {
        let output = 2_713_310_158;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

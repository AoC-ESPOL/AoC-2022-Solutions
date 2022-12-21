use std::collections::HashMap;

use nom::{
    branch::alt,
    bytes::complete::tag,
    character::complete::{alpha1, digit1},
    combinator::map,
    sequence::separated_pair,
    IResult,
};

pub fn part1(input: &str) -> i64 {
    let mut monkeys: HashMap<_, _> = input
        .lines()
        .map(|line| parse_line(line).unwrap().1)
        .collect();

    loop {
        for (monkey, oper) in &monkeys.clone() {
            let result = match oper {
                Op::Add((a, b)) => {
                    let Some(Op::Number(x)) = monkeys.get(a) else { continue; };
                    let Some(Op::Number(y)) = monkeys.get(b) else { continue; };
                    x + y
                }
                Op::Sub((a, b)) => {
                    let Some(Op::Number(x)) = monkeys.get(a) else { continue; };
                    let Some(Op::Number(y)) = monkeys.get(b) else { continue; };
                    x - y
                }
                Op::Mul((a, b)) => {
                    let Some(Op::Number(x)) = monkeys.get(a) else { continue; };
                    let Some(Op::Number(y)) = monkeys.get(b) else { continue; };
                    x * y
                }
                Op::Div((a, b)) => {
                    let Some(Op::Number(x)) = monkeys.get(a) else { continue; };
                    let Some(Op::Number(y)) = monkeys.get(b) else { continue; };
                    x / y
                }
                Op::Number(_) | Op::Eq(_) => continue,
            };

            if *monkey == "root" {
                return result.round() as i64;
            }

            monkeys.insert(monkey, Op::Number(result));
        }
    }
}

pub fn part2(input: &str) -> i64 {
    let mut monkeys: HashMap<_, _> = input
        .lines()
        .map(|line| parse_line(line).unwrap().1)
        .collect();

    let Op::Add(pair) = monkeys["root"] else { unreachable!() };

    monkeys.insert("root", Op::Eq(pair));

    // binary search
    let mut low = 0;
    let mut high = 1 << 62;

    loop {
        let mut monkeys = monkeys.clone();

        let response = (low + high) / 2;
        monkeys.insert("humn", Op::Number(response as f64));

        'outer: loop {
            for (monkey, oper) in monkeys
                .clone()
                .iter()
                .filter(|(_, o)| !matches!(o, Op::Number(_)))
            {
                let result = match oper {
                    Op::Add((a, b)) => {
                        let Some(Op::Number(x)) = monkeys.get(a) else { continue; };
                        let Some(Op::Number(y)) = monkeys.get(b) else { continue; };
                        x + y
                    }
                    Op::Sub((a, b)) => {
                        let Some(Op::Number(x)) = monkeys.get(a) else { continue; };
                        let Some(Op::Number(y)) = monkeys.get(b) else { continue; };
                        x - y
                    }
                    Op::Mul((a, b)) => {
                        let Some(Op::Number(x)) = monkeys.get(a) else { continue; };
                        let Some(Op::Number(y)) = monkeys.get(b) else { continue; };
                        x * y
                    }
                    Op::Div((a, b)) => {
                        let Some(Op::Number(x)) = monkeys.get(a) else { continue; };
                        let Some(Op::Number(y)) = monkeys.get(b) else { continue; };
                        x / y
                    }
                    Op::Eq((a, b)) => {
                        let Some(Op::Number(x)) = monkeys.get(a) else { continue; };
                        let Some(Op::Number(y)) = monkeys.get(b) else { continue; };

                        match x.total_cmp(y) {
                            std::cmp::Ordering::Equal => return response,
                            std::cmp::Ordering::Less => {
                                if cfg!(test) {
                                    low = response;
                                } else {
                                    high = response;
                                }
                                break 'outer;
                            }
                            std::cmp::Ordering::Greater => {
                                if cfg!(test) {
                                    high = response;
                                } else {
                                    low = response;
                                }
                                break 'outer;
                            }
                        }
                    }
                    Op::Number(_) => unreachable!(),
                };
                monkeys.insert(monkey, Op::Number(result));
            }
        }
    }
}

fn parse_line(input: &str) -> IResult<&str, (&str, Op)> {
    separated_pair(
        alpha1,
        tag(": "),
        alt((
            map(digit1, |n: &str| Op::Number(n.parse().unwrap())),
            map(separated_pair(alpha1, tag(" + "), alpha1), Op::Add),
            map(separated_pair(alpha1, tag(" - "), alpha1), Op::Sub),
            map(separated_pair(alpha1, tag(" * "), alpha1), Op::Mul),
            map(separated_pair(alpha1, tag(" / "), alpha1), Op::Div),
        )),
    )(input)
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 152;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 301;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

#[derive(Debug, Clone)]
enum Op<'a> {
    Add((&'a str, &'a str)),
    Sub((&'a str, &'a str)),
    Mul((&'a str, &'a str)),
    Div((&'a str, &'a str)),
    Eq((&'a str, &'a str)),
    Number(f64),
}

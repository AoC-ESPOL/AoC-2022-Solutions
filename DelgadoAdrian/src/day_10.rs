use bstr::ByteSlice;
use itertools::Itertools;
use nom::{
    branch::alt,
    bytes::complete::tag,
    character::complete::i16,
    combinator::{map, value},
    sequence::preceded,
    IResult,
};

pub fn part1(input: &str) -> i16 {
    let mut x = 1;
    let mut cycle = 0;
    let mut strength = 0;

    for op in input.lines().map(|line| parse_line(line).unwrap().1) {
        cycle += 1;
        if matches!(cycle, 20 | 60 | 100 | 140 | 180 | 220) {
            strength += x * cycle;
        }
        match op {
            Op::Addx(n) => {
                cycle += 1;
                if matches!(cycle, 20 | 60 | 100 | 140 | 180 | 220) {
                    strength += x * cycle;
                }
                x += n;
            }
            Op::Noop => (),
        }
    }

    strength
}

#[allow(clippy::cast_possible_truncation, clippy::cast_possible_wrap)]
pub fn part2(input: &str) -> String {
    let mut x = 1;
    let mut cycle = 0;
    let mut screen = [b'.'; 40 * 6];

    for op in input.lines().map(|line| parse_line(line).unwrap().1) {
        if (cycle as i16 % 40).abs_diff(x) < 2 {
            screen[cycle] = b'#';
        }
        cycle += 1;
        match op {
            Op::Addx(n) => {
                if (cycle as i16 % 40).abs_diff(x) < 2 {
                    screen[cycle] = b'#';
                }
                cycle += 1;
                x += n;
            }
            Op::Noop => (),
        }
    }
    screen
        .chunks(40)
        .map(|row| row.to_str().unwrap())
        .join("\n")
}

fn parse_line(input: &str) -> IResult<&str, Op> {
    alt((
        map(preceded(tag("addx "), i16), Op::Addx),
        value(Op::Noop, tag("noop")),
    ))(input)
}

#[derive(Debug, Clone, Copy)]
enum Op {
    Noop,
    Addx(i16),
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
    #[ignore]
    fn part1_works() {
        let output = 13140;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = "\
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....";

        assert_eq!(part2(TEST_INPUT), output);
    }
}

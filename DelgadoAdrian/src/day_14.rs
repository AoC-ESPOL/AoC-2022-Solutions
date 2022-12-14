use std::collections::HashSet;

use itertools::Itertools;
use nom::{
    bytes::complete::tag, character::complete::u16, multi::separated_list0,
    sequence::separated_pair, IResult,
};

fn solve<const PART_2: bool>(input: &str) -> usize {
    let mut cave: HashSet<_> = input
        .lines()
        .map(|line| parse_line(line).unwrap().1)
        .flat_map(|scan| {
            scan.into_iter()
                .tuple_windows()
                .flat_map(|((x1, y1), (x2, y2))| {
                    (x1.min(x2)..=x2.max(x1)).cartesian_product(y1.min(y2)..=y2.max(y1))
                })
        })
        .collect();

    let amount_rocks = cave.len();

    let max_y = cave.iter().map(|(_, y)| *y).max().unwrap();

    'outer: loop {
        if PART_2 && cave.contains(&(500, 0)) {
            break;
        }
        let mut curr_x = 500;
        let mut curr_y = 0;

        let new_position = loop {
            if curr_y > max_y {
                if PART_2 {
                    break (curr_x, curr_y);
                }
                break 'outer;
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
                break (curr_x, curr_y);
            }
        };

        cave.insert(new_position);
    }

    cave.len() - amount_rocks
}

pub fn part1(input: &str) -> usize {
    solve::<false>(input)
}

pub fn part2(input: &str) -> usize {
    solve::<true>(input)
}

fn parse_line(input: &str) -> IResult<&str, Vec<(u16, u16)>> {
    separated_list0(tag(" -> "), separated_pair(u16, tag(","), u16))(input)
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 24;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 93;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

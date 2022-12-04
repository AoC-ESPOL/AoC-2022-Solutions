use itertools::Itertools;

fn priority(chr: char) -> u32 {
    match chr {
        'a'..='z' => (chr as u32 - 'a' as u32) + 1,
        'A'..='Z' => (chr as u32 - 'A' as u32) + 27,
        _ => unreachable!(),
    }
}

pub fn part1(input: &str) -> u32 {
    input
        .lines()
        .map(|line| line.split_at(line.len() / 2))
        .map(|(start, end)| start.chars().find(|&chr| end.contains(chr)).unwrap())
        .map(priority)
        .sum()
}

pub fn part2(input: &str) -> u32 {
    input
        .lines()
        .tuples()
        .map(|(a, b, c)| {
            a.chars()
                .find(|&chr| b.contains(chr) && c.contains(chr))
                .unwrap()
        })
        .map(priority)
        .sum()
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 157;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 70;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

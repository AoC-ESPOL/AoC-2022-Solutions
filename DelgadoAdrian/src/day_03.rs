use itertools::Itertools;

fn priority(chr: char) -> u32 {
    match chr {
        'a'..='z' => chr as u32 - 96,
        'A'..='Z' => chr as u32 - 38,
        _ => unreachable!(),
    }
}

pub fn part1(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            let (start, end) = line.split_at(line.len() / 2);
            let common = start.chars().find(|&chr| end.contains(chr)).unwrap();

            priority(common)
        })
        .sum()
}

pub fn part2(input: &str) -> u32 {
    input
        .lines()
        .tuples()
        .map(|(a, b, c)| {
            let common = a
                .chars()
                .find(|&chr| b.contains(chr) && c.contains(chr))
                .unwrap();

            priority(common)
        })
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
    fn part1_works() {
        let output = 157;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    fn part2_works() {
        let output = 70;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

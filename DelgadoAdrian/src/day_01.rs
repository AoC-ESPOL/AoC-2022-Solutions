use std::cmp::Reverse;

pub fn part1(input: &str) -> String {
    input
        .split("\n\n")
        .map(|elf_cals| {
            elf_cals
                .lines()
                .map(|line| line.parse::<u32>().unwrap())
                .sum::<u32>()
        })
        .max()
        .unwrap()
        .to_string()
}

pub fn part2(input: &str) -> String {
    let mut calories: Vec<_> = input
        .split("\n\n")
        .map(|elf_cals| {
            elf_cals
                .lines()
                .map(|line| line.parse::<u32>().unwrap())
                .sum::<u32>()
        })
        .collect();

    calories.sort_by_key(|&cals| Reverse(cals));
    calories.truncate(3);

    calories.into_iter().sum::<u32>().to_string()
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 24000.to_string();

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 45000.to_string();

        assert_eq!(part2(TEST_INPUT), output);
    }
}

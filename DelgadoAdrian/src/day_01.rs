fn calories_per_elf(input: &str) -> impl Iterator<Item = u32> + '_ {
    input.split("\n\n").map(|elf_cals| -> u32 {
        elf_cals
            .lines()
            .map(|line| -> u32 { line.parse().unwrap() })
            .sum()
    })
}

pub fn part1(input: &str) -> u32 {
    calories_per_elf(input).max().unwrap()
}

pub fn part2(input: &str) -> u32 {
    let mut calories: Vec<_> = calories_per_elf(input).collect();
    calories.sort_unstable();
    calories.into_iter().rev().take(3).sum()
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
        let output = 24000;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 45000;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

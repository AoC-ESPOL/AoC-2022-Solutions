use std::collections::BinaryHeap;

fn calories_per_elf(input: &str) -> impl Iterator<Item = u32> + '_ {
    input.split("\n\n").map(|elf_cals| -> u32 {
        elf_cals
            .lines()
            .map(|line| line.parse::<u32>().unwrap())
            .sum()
    })
}

pub fn part1(input: &str) -> String {
    calories_per_elf(input).max().unwrap().to_string()
}

pub fn part2(input: &str) -> String {
    calories_per_elf(input)
        .collect::<BinaryHeap<_>>()
        .into_iter()
        .take(3)
        .sum::<u32>()
        .to_string()
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

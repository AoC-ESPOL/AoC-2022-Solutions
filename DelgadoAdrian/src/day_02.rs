use nom::{
    branch::alt, bytes::complete::tag, combinator::value, sequence::separated_pair, IResult,
};

pub fn part1(input: &str) -> u32 {
    input
        .lines()
        .map(|line| parse_line(line).unwrap().1)
        .map(|(opponent, you)| {
            let shape_selected = match you {
                Second::X => 1, // Rock
                Second::Y => 2, // Paper
                Second::Z => 3, // Scissors
            };

            let outcome = match (opponent, you) {
                (Opponent::Rock, Second::Y)
                | (Opponent::Paper, Second::Z)
                | (Opponent::Scissors, Second::X) => 6, // Win
                (Opponent::Rock, Second::X)
                | (Opponent::Scissors, Second::Z)
                | (Opponent::Paper, Second::Y) => 3, // Draw
                (Opponent::Rock, Second::Z)
                | (Opponent::Paper, Second::X)
                | (Opponent::Scissors, Second::Y) => 0, // Lose
            };

            outcome + shape_selected
        })
        .sum()
}

pub fn part2(input: &str) -> u32 {
    input
        .lines()
        .map(|line| parse_line(line).unwrap().1)
        .map(|(opponent, you)| {
            let outcome = match you {
                Second::X => 0, // Lose
                Second::Y => 3, // Draw
                Second::Z => 6, // Win
            };

            let shape_selected = match (opponent, you) {
                (Opponent::Rock, Second::Y)
                | (Opponent::Paper, Second::X)
                | (Opponent::Scissors, Second::Z) => 1, // Rock
                (Opponent::Rock, Second::Z)
                | (Opponent::Paper, Second::Y)
                | (Opponent::Scissors, Second::X) => 2, // Paper
                (Opponent::Rock, Second::X)
                | (Opponent::Paper, Second::Z)
                | (Opponent::Scissors, Second::Y) => 3, // Scissors
            };

            outcome + shape_selected
        })
        .sum()
}

fn parse_line(input: &str) -> IResult<&str, (Opponent, Second)> {
    separated_pair(
        alt((
            value(Opponent::Rock, tag("A")),
            value(Opponent::Paper, tag("B")),
            value(Opponent::Scissors, tag("C")),
        )),
        tag(" "),
        alt((
            value(Second::X, tag("X")),
            value(Second::Y, tag("Y")),
            value(Second::Z, tag("Z")),
        )),
    )(input)
}

#[derive(Debug, Clone, Copy)]
enum Opponent {
    Rock,
    Paper,
    Scissors,
}

#[derive(Debug, Clone, Copy)]
enum Second {
    X,
    Y,
    Z,
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
A Y
B X
C Z";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 15;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 12;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

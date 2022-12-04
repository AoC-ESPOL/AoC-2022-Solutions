use nom::{bytes::complete::tag, character::complete::u32, sequence::tuple, IResult};

pub fn part1(input: &str) -> usize {
    input
        .lines()
        .map(|line| parse_line(line).unwrap().1)
        .filter(|(a, b, x, y)| (a <= x && y <= b) || (a >= x && y >= b))
        .count()
}

pub fn part2(input: &str) -> usize {
    input
        .lines()
        .map(|line| parse_line(line).unwrap().1)
        .filter(|(a, b, x, y)| (b >= x) && (y >= a))
        .count()
}

fn parse_line(input: &str) -> IResult<&str, (u32, u32, u32, u32)> {
    let (rest, (a, _, b, _, x, _, y)) =
        tuple((u32, tag("-"), u32, tag(","), u32, tag("-"), u32))(input)?;
    Ok((rest, (a, b, x, y)))
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 2;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 4;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

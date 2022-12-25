pub fn part1(input: &str) -> String {
    let mut decimal: i64 = input.lines().map(parse_snafu).sum();

    let mut snafu = String::new();

    while decimal > 0 {
        let (digit, chr) = match decimal % 5 {
            0 => (0, '0'),
            1 => (1, '1'),
            2 => (2, '2'),
            3 => (-2, '='),
            4 => (-1, '-'),
            _ => unreachable!(),
        };
        snafu.push(chr);
        decimal -= digit;
        decimal /= 5;
    }

    snafu.chars().rev().collect()
}

pub fn part2(_input: &str) -> &'static str {
    "Merry Christmas!"
}

fn parse_snafu(input: &str) -> i64 {
    input
        .chars()
        .rev()
        .enumerate()
        .fold(0, |acc, (position, chr)| {
            let digit: i64 = match chr {
                '=' => -2,
                '-' => -1,
                '0' => 0,
                '1' => 1,
                '2' => 2,
                _ => unreachable!(),
            };

            acc + 5_i64.pow(position as u32) * digit
        })
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122";

    #[test]
    fn part1_works() {
        let output = "2=-1=0";

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    fn part2_works() {
        let output = "Merry Christmas!";

        assert_eq!(part2(TEST_INPUT), output);
    }
}

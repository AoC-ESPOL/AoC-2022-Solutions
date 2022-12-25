pub fn part1(input: &str) -> String {
    let mut decimal: i64 = input
        .as_bytes()
        .split(|&c| c == b'\n')
        .flat_map(|line| {
            line.iter().rev().zip(0..).map(|(chr, position)| {
                let digit = match chr {
                    b'=' => -2,
                    b'-' => -1,
                    _ => i64::from(chr - b'0'),
                };

                5_i64.pow(position) * digit
            })
        })
        .sum();

    let mut snafu = Vec::new();

    while decimal > 0 {
        #[allow(clippy::cast_sign_loss, clippy::cast_possible_truncation)]
        let chr = match decimal % 5 {
            3 => b'=',
            4 => b'-',
            rem => b'0' + rem as u8,
        };
        snafu.push(chr);
        decimal = (decimal + 2) / 5;
    }

    snafu.reverse();

    String::from_utf8(snafu).unwrap()
}

pub fn part2(_input: &str) -> &'static str {
    "Merry Christmas!"
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

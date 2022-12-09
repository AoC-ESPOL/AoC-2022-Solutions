use std::collections::HashSet;

use nom::{
    branch::alt, bytes::complete::tag, character::complete::u8, combinator::value,
    sequence::separated_pair, IResult,
};

pub fn part1(input: &str) -> usize {
    simulate_snake::<2>(input)
}

pub fn part2(input: &str) -> usize {
    simulate_snake::<10>(input)
}

fn simulate_snake<const LEN_SNAKE: usize>(input: &str) -> usize {
    let mut positions_tail = HashSet::new();
    let mut snake = [[0; 2]; LEN_SNAKE]; // [head, .., tail]
    for (dir, n) in input.lines().map(|line| parse_line(line).unwrap().1) {
        for _ in 0..n {
            add_inplace(&mut snake[0], dir);

            for idx in 1..LEN_SNAKE {
                let previous = snake[idx - 1];
                update_snake_mut(&mut snake[idx], previous);
            }

            positions_tail.insert(snake[LEN_SNAKE - 1]);
        }
    }

    positions_tail.len()
}

fn add_inplace([x1, y1]: &mut [i16; 2], [x2, y2]: [i16; 2]) {
    *x1 += x2;
    *y1 += y2;
}

fn get_deltas([x1, y1]: [i16; 2], [x2, y2]: [i16; 2]) -> [i16; 2] {
    [x1 - x2, y1 - y2]
}

fn update_snake_mut(current: &mut [i16; 2], previous: [i16; 2]) {
    let [dx, dy] = get_deltas(previous, *current);
    if dx * dx + dy * dy > 2 {
        let direction = [dx.signum(), dy.signum()];
        add_inplace(current, direction);
    }
}

fn parse_line(input: &str) -> IResult<&str, ([i16; 2], u8)> {
    separated_pair(
        alt((
            value([0, 1], tag("U")),
            value([0, -1], tag("D")),
            value([-1, 0], tag("L")),
            value([1, 0], tag("R")),
        )),
        tag(" "),
        u8,
    )(input)
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT_1: &str = "\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2";

    const TEST_INPUT_2: &str = "\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 13;

        assert_eq!(part1(TEST_INPUT_1), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 1;

        assert_eq!(part2(TEST_INPUT_1), output);

        let output = 36;

        assert_eq!(part2(TEST_INPUT_2), output);
    }
}

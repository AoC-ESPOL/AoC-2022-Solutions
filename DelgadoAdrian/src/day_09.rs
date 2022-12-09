use std::collections::HashSet;

use nom::{
    branch::alt, bytes::complete::tag, character::complete::u8, combinator::value,
    sequence::separated_pair, IResult,
};

pub fn part1(input: &str) -> usize {
    let mut positions_tail = HashSet::new();
    let mut snake = [[0; 2]; 2]; // head 0, tail 1

    for (dir, n) in input.lines().map(|line| parse_line(line).unwrap().1) {
        for _ in 0..n {
            let [ref mut head, ref mut tail] = snake;

            add_inplace(head, dir);
            update_snake_mut(tail, *head);

            positions_tail.insert(*tail);
        }
    }

    positions_tail.len()
}

pub fn part2(input: &str) -> usize {
    let mut positions_tail = HashSet::new();
    let mut snake = [[0; 2]; 10]; // head 0, tail 9
    for (dir, n) in input.lines().map(|line| parse_line(line).unwrap().1) {
        for _ in 0..n {
            add_inplace(&mut snake[0], dir);

            for idx in 1..snake.len() {
                let previous = snake[idx - 1];
                update_snake_mut(&mut snake[idx], previous);
            }

            positions_tail.insert(snake[9]);
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
        let output = 36;

        assert_eq!(part2(TEST_INPUT_2), output);
    }
}

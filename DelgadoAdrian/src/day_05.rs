use bstr::ByteSlice;
use nom::{bytes::complete::tag, character::complete::u32, sequence::tuple, IResult};

pub fn part1(input: &str) -> String {
    let (crates, moves) = input.split_once("\n\n").unwrap();
    let mut stacks = parse_crates(crates.as_bytes());

    for (amount, from, to) in moves.lines().map(|line| parse_move(line).unwrap().1) {
        let (from, to) = get_mut_2(&mut stacks, from, to);

        let split_idx = from.len() - amount;
        to.extend(from[split_idx..].iter().rev());
        from.truncate(split_idx);
    }

    stacks
        .into_iter()
        .map(|mut stack| stack.pop().unwrap() as char)
        .collect()
}

pub fn part2(input: &str) -> String {
    let (crates, moves) = input.split_once("\n\n").unwrap();
    let mut stacks = parse_crates(crates.as_bytes());

    for (amount, from, to) in moves.lines().map(|line| parse_move(line).unwrap().1) {
        let (from, to) = get_mut_2(&mut stacks, from, to);

        let split_idx = from.len() - amount;
        to.extend_from_slice(&from[split_idx..]);
        from.truncate(split_idx);
    }

    stacks
        .into_iter()
        .map(|mut stack| stack.pop().unwrap() as char)
        .collect()
}

fn parse_crates(input: &[u8]) -> Vec<Vec<u8>> {
    const BLOCK_LEN: usize = "[_] ".len();

    let width = input.find("\n").unwrap() + "\n".len();
    let cols = width / BLOCK_LEN;
    let rows = input.len() / width;

    let mut stacks = vec![Vec::with_capacity(rows); cols];

    for (col_idx, curr_stack) in stacks.iter_mut().enumerate().take(cols) {
        for current_row in 1..=rows {
            let col_position = BLOCK_LEN * col_idx;
            let rows_before = rows - current_row;
            let chars_in_rows_before = rows_before * width;
            let current_position = chars_in_rows_before + col_position + "[".len();

            let current_char = input[current_position];

            if current_char == b' ' {
                break;
            }
            curr_stack.push(current_char);
        }
    }

    stacks
}

fn parse_move(input: &str) -> IResult<&str, (usize, usize, usize)> {
    let (rest, (_, a, _, b, _, c)) =
        tuple((tag("move "), u32, tag(" from "), u32, tag(" to "), u32))(input)?;
    // Subtract 1 to use as an index
    Ok((rest, (a as usize, b as usize - 1, c as usize - 1)))
}

fn get_mut_2<T>(arr: &mut [T], a0: usize, a1: usize) -> (&mut T, &mut T) {
    assert!(a0 != a1);
    // SAFETY: this is safe because we know a0 != a1
    unsafe {
        (
            &mut *std::ptr::addr_of_mut!(arr[a0]),
            &mut *std::ptr::addr_of_mut!(arr[a1]),
        )
    }
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "    [D]    \n\
[N] [C]    \n\
[Z] [M] [P]\n\
 1   2   3 \n\
\n\
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = "CMZ".to_string();

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = "MCD".to_string();

        assert_eq!(part2(TEST_INPUT), output);
    }
}

use std::collections::VecDeque;

pub fn part1(input: &str) -> i64 {
    let mut encr_file: VecDeque<_> = input
        .lines()
        .map(|line| line.parse::<i64>().unwrap())
        .enumerate()
        .collect();

    let modl = encr_file.len();

    for i in 0..modl {
        let to_origin = encr_file.iter().position(|(n, _)| *n == i).unwrap();

        encr_file.rotate_left(to_origin);

        let shift = encr_file.pop_front().unwrap();

        let num_pops = shift.1.rem_euclid(modl as i64 - 1);

        encr_file.rotate_left(num_pops as usize);

        encr_file.push_back(shift);
    }

    let start = encr_file.iter().position(|(_, v)| *v == 0).unwrap();

    encr_file[(start + 1000) % modl].1
        + encr_file[(start + 2000) % modl].1
        + encr_file[(start + 3000) % modl].1
}

pub fn part2(input: &str) -> i64 {
    let mut encr_file: VecDeque<_> = input
        .lines()
        .map(|line| line.parse::<i64>().unwrap() * 811589153) // encription key
        .enumerate()
        .collect();

    let modl = encr_file.len();

    // 10 rounds of mixing
    for _ in 0..10 {
        for i in 0..modl {
            let to_origin = encr_file.iter().position(|(n, _)| *n == i).unwrap();

            encr_file.rotate_left(to_origin);

            let shift = encr_file.pop_front().unwrap();

            let num_pops = shift.1.rem_euclid(modl as i64 - 1);

            encr_file.rotate_left(num_pops as usize);

            encr_file.push_back(shift);
        }
    }

    let start = encr_file.iter().position(|(_, v)| *v == 0).unwrap();

    encr_file[(start + 1000) % modl].1
        + encr_file[(start + 2000) % modl].1
        + encr_file[(start + 3000) % modl].1
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
1
2
-3
3
-2
0
4";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 3;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 1623178306;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

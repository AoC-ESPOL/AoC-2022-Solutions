use std::collections::HashSet;

pub fn part1(input: &str) -> usize {
    n_different(input, 4)
}

pub fn part2(input: &str) -> usize {
    n_different(input, 14)
}

fn n_different(input: &str, size: usize) -> usize {
    input
        .as_bytes()
        .windows(size)
        .position(|win| {
            let mut set = HashSet::with_capacity(size);
            win.iter().all(|c| set.insert(c)) // shortcircuit
        })
        .unwrap()
        + size
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
";

    #[test]
    #[ignore]
    fn part1_works() {
        let outputs = [7, 5, 6, 10, 11];

        for (line, out) in TEST_INPUT.lines().zip(outputs) {
            assert_eq!(part1(line), out);
        }
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let outputs = [19, 23, 23, 29, 26];

        for (line, out) in TEST_INPUT.lines().zip(outputs) {
            assert_eq!(part2(line), out);
        }
    }
}

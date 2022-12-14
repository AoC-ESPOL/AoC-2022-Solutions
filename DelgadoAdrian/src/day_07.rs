use std::collections::HashMap;

use nom::{
    branch::alt,
    bytes::complete::tag,
    character::complete::u32,
    combinator::{map, rest, value},
    sequence::{preceded, separated_pair},
    IResult,
};

fn get_dir_sizes(input: &str) -> HashMap<Vec<&str>, u32> {
    let mut prev_dirs = Vec::new();
    let mut dir_sizes = HashMap::new();
    for command in input.lines().map(|line| parse_line(line).unwrap().1) {
        match command {
            Command::Cd(name) => prev_dirs.push(name),
            Command::Prev => prev_dirs.truncate(prev_dirs.len() - 1),
            Command::File((size, _)) => {
                for i in 0..prev_dirs.len() {
                    let dir = prev_dirs[0..=i].to_vec();
                    *dir_sizes.entry(dir).or_default() += size;
                }
            }
            Command::Ls | Command::Dir(_) => (),
        }
    }

    dir_sizes
}

pub fn part1(input: &str) -> u32 {
    get_dir_sizes(input)
        .values()
        .filter(|&&v| v <= 100_000)
        .sum()
}

pub fn part2(input: &str) -> u32 {
    let dir_sizes = get_dir_sizes(input);

    let free_space = 70_000_000 - dir_sizes[["/"].as_ref()];

    dir_sizes
        .into_values()
        .filter(|v| free_space + v >= 30_000_000)
        .min()
        .unwrap()
}

fn parse_line(input: &str) -> IResult<&str, Command> {
    alt((
        value(Command::Prev, tag("$ cd ..")),
        map(preceded(tag("$ cd "), rest), Command::Cd),
        value(Command::Ls, tag("$ ls")),
        map(preceded(tag("dir "), rest), Command::Dir),
        map(separated_pair(u32, tag(" "), rest), Command::File),
    ))(input)
}

#[derive(Debug, Clone)]
enum Command<'a> {
    Cd(&'a str),
    Prev,
    Ls,
    Dir(&'a str),
    File((u32, &'a str)),
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 95437;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 24933642;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

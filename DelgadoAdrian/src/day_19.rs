use std::collections::{HashSet, VecDeque};

use nom::{
    bytes::complete::tag,
    character::complete::i64,
    combinator::map,
    sequence::{preceded, tuple},
    IResult,
};

pub fn part1(input: &str) -> i64 {
    let mut sum_quality = 0;
    for bluep in input.lines().map(|line| parse_line(line).unwrap().1) {
        let starting_state = (0, 0, 0, 0, 1, 0, 0, 0, 24); // 24 min

        let mut queue = VecDeque::new();
        queue.push_back(starting_state);

        let mut max_geodes = 0;

        let mut memo = HashSet::new();

        let max_ore_cost = [bluep.ore, bluep.clay, bluep.obsidian_ore, bluep.geode_ore]
            .into_iter()
            .max()
            .unwrap();

        while let Some((
            mut ore,
            mut clay,
            mut obsidian,
            geode,
            mut ore_robot,
            mut clay_robot,
            mut obsidian_robot,
            geode_robot,
            minute,
        )) = queue.pop_front()
        {
            max_geodes = max_geodes.max(geode);

            if minute == 0 {
                continue;
            }
            // Skip not interesting
            ore_robot = max_ore_cost.min(ore_robot);
            clay_robot = bluep.obsidian_clay.min(clay_robot);
            obsidian_robot = bluep.geode_obsidian.min(obsidian_robot);
            ore = ore.min(max_ore_cost * minute - ore_robot * (minute - 1));
            clay = clay.min(bluep.obsidian_clay * minute - clay_robot * (minute - 1));
            obsidian = obsidian.min(bluep.geode_obsidian * minute - obsidian_robot * (minute - 1));

            let state = (
                ore,
                clay,
                obsidian,
                geode,
                ore_robot,
                clay_robot,
                obsidian_robot,
                geode_robot,
                minute,
            );

            if !memo.insert(state) {
                continue;
            }

            let add_ore_robot = ore >= bluep.ore;
            let add_clay_robot = ore >= bluep.clay;
            let add_obsidian_robot = ore >= bluep.obsidian_ore && clay >= bluep.obsidian_clay;
            let add_geode_robot = ore >= bluep.geode_ore && obsidian >= bluep.geode_obsidian;

            queue.push_back((
                ore + ore_robot,
                clay + clay_robot,
                obsidian + obsidian_robot,
                geode + geode_robot,
                ore_robot,
                clay_robot,
                obsidian_robot,
                geode_robot,
                minute - 1,
            ));

            if add_ore_robot {
                queue.push_back((
                    ore - bluep.ore + ore_robot,
                    clay + clay_robot,
                    obsidian + obsidian_robot,
                    geode + geode_robot,
                    ore_robot + 1,
                    clay_robot,
                    obsidian_robot,
                    geode_robot,
                    minute - 1,
                ));
            }
            if add_clay_robot {
                queue.push_back((
                    ore - bluep.clay + ore_robot,
                    clay + clay_robot,
                    obsidian + obsidian_robot,
                    geode + geode_robot,
                    ore_robot,
                    clay_robot + 1,
                    obsidian_robot,
                    geode_robot,
                    minute - 1,
                ));
            }
            if add_obsidian_robot {
                queue.push_back((
                    ore - bluep.obsidian_ore + ore_robot,
                    clay - bluep.obsidian_clay + clay_robot,
                    obsidian + obsidian_robot,
                    geode + geode_robot,
                    ore_robot,
                    clay_robot,
                    obsidian_robot + 1,
                    geode_robot,
                    minute - 1,
                ));
            }
            if add_geode_robot {
                queue.push_back((
                    ore - bluep.geode_ore + ore_robot,
                    clay + clay_robot,
                    obsidian - bluep.geode_obsidian + obsidian_robot,
                    geode + geode_robot,
                    ore_robot,
                    clay_robot,
                    obsidian_robot,
                    geode_robot + 1,
                    minute - 1,
                ));
            }
        }

        sum_quality += bluep.num * max_geodes;
    }

    sum_quality
}

pub fn part2(input: &str) -> i64 {
    let mut prod_geodes = 1;
    for bluep in input
        .lines()
        .map(|line| parse_line(line).unwrap().1)
        .take(3)
    {
        let starting_state = (0, 0, 0, 0, 1, 0, 0, 0, 32); // 32 min

        let mut queue = VecDeque::new();
        queue.push_back(starting_state);

        let mut max_geodes = 0;

        let mut memo = HashSet::new();

        let max_ore_cost = [bluep.ore, bluep.clay, bluep.obsidian_ore, bluep.geode_ore]
            .into_iter()
            .max()
            .unwrap();

        while let Some((
            mut ore,
            mut clay,
            mut obsidian,
            geode,
            mut ore_robot,
            mut clay_robot,
            mut obsidian_robot,
            geode_robot,
            minute,
        )) = queue.pop_front()
        {
            max_geodes = max_geodes.max(geode);

            if minute == 0 {
                continue;
            }
            // Skip not interesting
            ore_robot = max_ore_cost.min(ore_robot);
            clay_robot = bluep.obsidian_clay.min(clay_robot);
            obsidian_robot = bluep.geode_obsidian.min(obsidian_robot);
            ore = ore.min(max_ore_cost * minute - ore_robot * (minute - 1));
            clay = clay.min(bluep.obsidian_clay * minute - clay_robot * (minute - 1));
            obsidian = obsidian.min(bluep.geode_obsidian * minute - obsidian_robot * (minute - 1));

            let state = (
                ore,
                clay,
                obsidian,
                geode,
                ore_robot,
                clay_robot,
                obsidian_robot,
                geode_robot,
                minute,
            );

            if !memo.insert(state) {
                continue;
            }

            let add_ore_robot = ore >= bluep.ore;
            let add_clay_robot = ore >= bluep.clay;
            let add_obsidian_robot = ore >= bluep.obsidian_ore && clay >= bluep.obsidian_clay;
            let add_geode_robot = ore >= bluep.geode_ore && obsidian >= bluep.geode_obsidian;

            queue.push_back((
                ore + ore_robot,
                clay + clay_robot,
                obsidian + obsidian_robot,
                geode + geode_robot,
                ore_robot,
                clay_robot,
                obsidian_robot,
                geode_robot,
                minute - 1,
            ));

            if add_ore_robot {
                queue.push_back((
                    ore - bluep.ore + ore_robot,
                    clay + clay_robot,
                    obsidian + obsidian_robot,
                    geode + geode_robot,
                    ore_robot + 1,
                    clay_robot,
                    obsidian_robot,
                    geode_robot,
                    minute - 1,
                ));
            }
            if add_clay_robot {
                queue.push_back((
                    ore - bluep.clay + ore_robot,
                    clay + clay_robot,
                    obsidian + obsidian_robot,
                    geode + geode_robot,
                    ore_robot,
                    clay_robot + 1,
                    obsidian_robot,
                    geode_robot,
                    minute - 1,
                ));
            }
            if add_obsidian_robot {
                queue.push_back((
                    ore - bluep.obsidian_ore + ore_robot,
                    clay - bluep.obsidian_clay + clay_robot,
                    obsidian + obsidian_robot,
                    geode + geode_robot,
                    ore_robot,
                    clay_robot,
                    obsidian_robot + 1,
                    geode_robot,
                    minute - 1,
                ));
            }
            if add_geode_robot {
                queue.push_back((
                    ore - bluep.geode_ore + ore_robot,
                    clay + clay_robot,
                    obsidian - bluep.geode_obsidian + obsidian_robot,
                    geode + geode_robot,
                    ore_robot,
                    clay_robot,
                    obsidian_robot,
                    geode_robot + 1,
                    minute - 1,
                ));
            }
        }

        prod_geodes *= max_geodes;
    }

    prod_geodes
}

#[derive(Debug)]
struct Blueprint {
    num: i64,
    ore: i64,
    clay: i64,
    obsidian_ore: i64,
    obsidian_clay: i64,
    geode_ore: i64,
    geode_obsidian: i64,
}

fn parse_line(input: &str) -> IResult<&str, Blueprint> {
    map(
        tuple((
            preceded(tag("Blueprint "), i64),
            preceded(tag(": Each ore robot costs "), i64),
            preceded(tag(" ore. Each clay robot costs "), i64),
            preceded(tag(" ore. Each obsidian robot costs "), i64),
            preceded(tag(" ore and "), i64),
            preceded(tag(" clay. Each geode robot costs "), i64),
            preceded(tag(" ore and "), i64),
        )),
        |(num, ore, clay, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian)| Blueprint {
            num,
            ore,
            clay,
            obsidian_ore,
            obsidian_clay,
            geode_ore,
            geode_obsidian,
        },
    )(input)
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 33;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 56 * 62;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

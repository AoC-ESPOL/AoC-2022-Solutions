use std::{cell::Cell, collections::HashMap};

use nom::{
    branch::alt,
    bytes::complete::tag,
    character::complete::{alpha1, u32},
    multi::separated_list1,
    sequence::{preceded, tuple},
    IResult,
};

pub fn part1(input: &str) -> u32 {
    let mut valves = HashMap::new();

    for (valve, flow_rate, leads) in input.lines().map(|line| parse_line(line).unwrap().1) {
        valves.insert(valve, (flow_rate, leads, Cell::new(false))); // false == not open
    }

    let mut visited: HashMap<(String, u32), u32> = HashMap::new(); //(valve, position) -> local max released

    traverse_p1("AA", 1, vec![0], &valves, &mut visited)
}

fn traverse_p1(
    curr_valve: &str,
    len: u32,
    mut curr_valves_flowing: Vec<u32>,
    valves: &HashMap<&str, (u32, Vec<&str>, Cell<bool>)>,
    visited: &mut HashMap<(String, u32), u32>,
) -> u32 {
    let mut max_released = 0;
    let curr_released = curr_valves_flowing.iter().sum();

    if visited.get(&(curr_valve.to_string(), len)) >= Some(&curr_released) {
        max_released = curr_released.max(max_released);
        return max_released;
    }

    visited.insert((curr_valve.to_string(), len), curr_released);

    if len == 30 {
        max_released = curr_released.max(max_released);

        return max_released;
    }

    if !(valves[curr_valve].2.get()) {
        valves[curr_valve].2.set(true);

        let new_releasing: u32 = valves
            .iter()
            .filter_map(|(_, (flow_rate, _, open))| open.get().then_some(*flow_rate))
            .sum();

        curr_valves_flowing.push(new_releasing);
        max_released = max_released.max(traverse_p1(
            curr_valve,
            len + 1,
            curr_valves_flowing.clone(),
            valves,
            visited,
        ));
        curr_valves_flowing.pop();
        valves[curr_valve].2.set(false);
    }

    let new_releasing: u32 = valves
        .iter()
        .filter_map(|(_, (flow_rate, _, open))| open.get().then_some(*flow_rate))
        .sum();

    let connected_valves = &valves[curr_valve].1;
    curr_valves_flowing.push(new_releasing);

    for val in connected_valves {
        max_released = max_released.max(traverse_p1(
            val,
            len + 1,
            curr_valves_flowing.clone(),
            valves,
            visited,
        ));
    }

    max_released
}

pub fn part2(input: &str) -> u32 {
    let mut valves = HashMap::new();

    for (valve, flow_rate, leads) in input.lines().map(|line| parse_line(line).unwrap().1) {
        valves.insert(valve, (flow_rate, leads, Cell::new(false))); // false == not open
    }

    let mut visited: HashMap<(String, String, u32), u32> = HashMap::new(); //(valve,valve_ele, position) -> local max released

    traverse_p2("AA", "AA", 1, vec![0], &valves, &mut visited)
}

fn traverse_p2(
    curr_valve: &str,
    elephant_valve: &str,
    len: u32,
    mut curr_valves_flowing: Vec<u32>,
    valves: &HashMap<&str, (u32, Vec<&str>, Cell<bool>)>,
    visited: &mut HashMap<(String, String, u32), u32>,
) -> u32 {
    let mut max_released = 0;
    let curr_released = curr_valves_flowing.iter().sum();

    if visited.get(&(curr_valve.to_string(), elephant_valve.to_string(), len))
        >= Some(&curr_released)
    {
        max_released = curr_released.max(max_released);
        return max_released;
    }

    visited.insert(
        (curr_valve.to_string(), elephant_valve.to_string(), len),
        curr_released,
    );

    if len == 26 {
        max_released = curr_released.max(max_released);

        return max_released;
    }

    if valves
        .iter()
        .all(|(_, (flow_rate, _, open))| *flow_rate == 0 || open.get())
    {
        let new_releasing: u32 = valves
            .iter()
            .filter_map(|(_, (flow_rate, _, open))| open.get().then_some(*flow_rate))
            .sum();

        curr_valves_flowing.push(new_releasing);

        max_released = max_released.max(traverse_p2(
            curr_valve,
            elephant_valve,
            len + 1,
            curr_valves_flowing.clone(),
            valves,
            visited,
        ));

        return max_released;
    }

    if !(valves[curr_valve].2.get() || valves[curr_valve].0 == 0) {
        valves[curr_valve].2.set(true);
        // ---
        if !(valves[elephant_valve].2.get() || valves[elephant_valve].0 == 0) {
            valves[elephant_valve].2.set(true);

            let new_releasing: u32 = valves
                .iter()
                .filter_map(|(_, (flow_rate, _, open))| open.get().then_some(*flow_rate))
                .sum();

            curr_valves_flowing.push(new_releasing);
            max_released = max_released.max(traverse_p2(
                curr_valve,
                elephant_valve,
                len + 1,
                curr_valves_flowing.clone(),
                valves,
                visited,
            ));
            curr_valves_flowing.pop();
            valves[elephant_valve].2.set(false);
        }
        // ---
        let new_releasing: u32 = valves
            .iter()
            .filter_map(|(_, (flow_rate, _, open))| open.get().then_some(*flow_rate))
            .sum();

        curr_valves_flowing.push(new_releasing);
        let connected_valves = &valves[elephant_valve].1;
        for val in connected_valves {
            max_released = max_released.max(traverse_p2(
                curr_valve,
                val,
                len + 1,
                curr_valves_flowing.clone(),
                valves,
                visited,
            ));
        }
        curr_valves_flowing.pop();

        // ---
        valves[curr_valve].2.set(false);
    }

    let connected_valves = &valves[curr_valve].1;

    for val in connected_valves {
        if !(valves[elephant_valve].2.get() || valves[elephant_valve].0 == 0) {
            valves[elephant_valve].2.set(true);

            let new_releasing: u32 = valves
                .iter()
                .filter_map(|(_, (flow_rate, _, open))| open.get().then_some(*flow_rate))
                .sum();

            curr_valves_flowing.push(new_releasing);
            max_released = max_released.max(traverse_p2(
                val,
                elephant_valve,
                len + 1,
                curr_valves_flowing.clone(),
                valves,
                visited,
            ));
            curr_valves_flowing.pop();
            valves[elephant_valve].2.set(false);
        }

        let new_releasing: u32 = valves
            .iter()
            .filter_map(|(_, (flow_rate, _, open))| open.get().then_some(*flow_rate))
            .sum();

        curr_valves_flowing.push(new_releasing);
        let connected_valves = &valves[elephant_valve].1;
        for val_ele in connected_valves {
            max_released = max_released.max(traverse_p2(
                val,
                val_ele,
                len + 1,
                curr_valves_flowing.clone(),
                valves,
                visited,
            ));
        }
        curr_valves_flowing.pop();
    }

    max_released
}

fn parse_line(input: &str) -> IResult<&str, (&str, u32, Vec<&str>)> {
    let (rest, tuple) = preceded(
        tag("Valve "),
        tuple((
            alpha1,
            preceded(tag(" has flow rate="), u32),
            preceded(
                alt((
                    tag("; tunnels lead to valves "),
                    tag("; tunnel leads to valve "),
                )),
                separated_list1(tag(", "), alpha1),
            ),
        )),
    )(input)?;
    Ok((rest, tuple))
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 1651;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 1707;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

#![allow(unused)]

use std::collections::{HashMap, HashSet};

use bstr::ByteSlice;
use itertools::{iproduct, Itertools};
use ndarray::{array, s, Array2};
use nom::{
    branch::alt,
    bytes::complete::{is_not, tag},
    character::complete::{alpha1, digit1, i64, newline, u64},
    combinator::{map, value},
    multi::separated_list0,
    sequence::{delimited, preceded, terminated, tuple},
    IResult,
};
use petgraph::{
    algo::{all_simple_paths, toposort},
    prelude::*,
};

type Cube = (i64, i64, i64);

const DELTAS: [Cube; 6] = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1),
];

pub fn part1(input: &str) -> usize {
    let mut cubes_map: HashMap<Cube, HashSet<Cube>> = HashMap::new();
    for cube in input.lines().map(|line| parse_cube(line).unwrap().1) {
        cubes_map.insert(cube, HashSet::new());
    }
    for cube in input.lines().map(|line| parse_cube(line).unwrap().1) {
        for delta in DELTAS {
            let adyacent_cube = add_points(cube, delta);
            if cubes_map.contains_key(&adyacent_cube) {
                cubes_map.get_mut(&cube).unwrap().insert(adyacent_cube);
                cubes_map.get_mut(&adyacent_cube).unwrap().insert(cube);
            }
        }
    }

    cubes_map.into_values().map(|ady| 6 - ady.len()).sum()
}

fn add_points((x1, y1, z1): Cube, (x2, y2, z2): Cube) -> Cube {
    (x1 + x2, y1 + y2, z1 + z2)
}

pub fn part2(input: &str) -> usize {
    let mut cubes_map: HashMap<Cube, HashSet<Cube>> = HashMap::new();
    for cube in input.lines().map(|line| parse_cube(line).unwrap().1) {
        cubes_map.insert(cube, HashSet::new());
    }
    for cube in input.lines().map(|line| parse_cube(line).unwrap().1) {
        for delta in DELTAS {
            let adyacent_cube = add_points(cube, delta);
            if cubes_map.contains_key(&adyacent_cube) {
                cubes_map.get_mut(&cube).unwrap().insert(adyacent_cube);
                cubes_map.get_mut(&adyacent_cube).unwrap().insert(cube);
            }
        }
    }
    let mut not_scanned: HashSet<_> = iproduct!(0..20, 0..20, 0..20)
        .filter(|cube| !cubes_map.contains_key(cube))
        .collect();

    let mut stack: Vec<Cube> = vec![(0, 0, 0)];

    while let Some(cube) = stack.pop() {
        if not_scanned.contains(&cube) {
            not_scanned.remove(&cube);
            for delta in DELTAS {
                let adyacent_cube = add_points(cube, delta);
                stack.push(adyacent_cube);
            }
        }
    }

    cubes_map
        .into_iter()
        .map(|(cube, ady)| {
            let mut count = 0;
            for delta in DELTAS {
                let adyacent_cube = add_points(cube, delta);
                if !ady.contains(&adyacent_cube) && !not_scanned.contains(&adyacent_cube) {
                    count += 1;
                }
            }
            count
        })
        .sum()
}

fn parse_cube(input: &str) -> IResult<&str, Cube> {
    let (rest, (a, _, b, _, c)) = tuple((i64, tag(","), i64, tag(","), i64))(input)?;
    Ok((rest, (a, b, c)))
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5";

    #[test]
    fn part1_works() {
        let output = 64;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    fn part2_works() {
        let output = 58;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

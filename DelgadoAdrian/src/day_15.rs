#![allow(unused)]

use bstr::ByteSlice;
use itertools::Itertools;
use ndarray::{array, s, Array2};
use nom::{
    branch::alt,
    bytes::complete::{is_not, tag},
    character::complete::{alpha1, digit1, i64, newline, u32, u64},
    combinator::{map, value},
    multi::separated_list0,
    sequence::{delimited, preceded, terminated, tuple},
    IResult,
};
use petgraph::{
    algo::{all_simple_paths, toposort},
    prelude::*,
};

const STUFF: [[(i64, i64); 2]; 26] = [
    [(3999724, 2000469), (4281123, 2282046)],
    [(3995530, 8733), (3321979, 692911)],
    [(3016889, 2550239), (2408038, 2645605)],
    [(3443945, 3604888), (3610223, 3768674)],
    [(168575, 491461), (1053731, 142061)],
    [(2820722, 3865596), (3191440, 3801895)],
    [(2329102, 2456329), (2408038, 2645605)],
    [(3889469, 3781572), (3610223, 3768674)],
    [(3256726, 3882107), (3191440, 3801895)],
    [(3729564, 3214899), (3610223, 3768674)],
    [(206718, 2732608), (-152842, 3117903)],
    [(2178192, 2132103), (2175035, 2000000)],
    [(1884402, 214904), (1053731, 142061)],
    [(3060435, 980430), (2175035, 2000000)], // here
    [(3998355, 3965954), (3610223, 3768674)],
    [(3704399, 3973731), (3610223, 3768674)],
    [(1421672, 3446889), (2408038, 2645605)],
    [(3415633, 3916020), (3191440, 3801895)],
    [(2408019, 2263990), (2408038, 2645605)],
    [(3735247, 2533767), (4281123, 2282046)],
    [(1756494, 1928662), (2175035, 2000000)],
    [(780161, 1907142), (2175035, 2000000)],
    [(3036853, 3294727), (3191440, 3801895)],
    [(53246, 3908582), (-152842, 3117903)],
    [(2110517, 2243287), (2175035, 2000000)],
    [(3149491, 3998374), (3191440, 3801895)],
];

pub fn part1(input: &str) -> u64 {
    let y_coord = 2_000_000;
    let distances =
        STUFF.map(|[sensor, closest_beacon]| (sensor, distance(sensor, closest_beacon)));

    let max_distance = distances.iter().map(|(_, d)| *d).max().unwrap();

    let x_values = (-1_000_000)..(2175035 + 3_000_000);
    let mut asdf = 0;
    for x in x_values {
        if distances
            .iter()
            .any(|(sensor, d)| distance((x, y_coord), *sensor) <= *d)
        {
            asdf += 1;
        }
    }

    asdf - 1
}

fn distance((x1, y1): (i64, i64), (x2, y2): (i64, i64)) -> u64 {
    x1.abs_diff(x2) + y1.abs_diff(y2)
}

pub fn part2(_input: &str) -> i64 {
    let distances =
        STUFF.map(|[sensor, closest_beacon]| (sensor, distance(sensor, closest_beacon)));

    let max_distance = distances.iter().map(|(_, d)| *d).max().unwrap();

    for (sensor, d) in distances {
        for (x, y) in border(sensor, d as i64) {
            if !(0..=4000000).contains(&x) || !(0..=4000000).contains(&y) {
                continue;
            }
            if distances
                .iter()
                .all(|(sensor, d)| distance((x, y), *sensor) > *d)
            {
                return x * 4000000 + y;
            }
        }
    }

    0
}

fn border((x1, y1): (i64, i64), d: i64) -> impl Iterator<Item = (i64, i64)> {
    let signs = [(1, 1), (-1, 1), (-1, -1), (1, -1)];

    (0..d + 2)
        .map(move |dx| (dx, (d + 1) - dx))
        .flat_map(move |deltas| signs.into_iter().map(move |signs| (deltas, signs)))
        .map(move |((dx, dy), (sgnx, sgny))| (x1 + (dx * sgnx), y1 + (dy * sgny)))
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
";

    #[test]
    fn part1_works() {
        let output = 24000;

        assert_eq!(part1(TEST_INPUT), output);
    }

    // #[test]
    // fn part2_works() {
    //     let output = 45000;

    //     assert_eq!(part2(TEST_INPUT), output);
    // }
}

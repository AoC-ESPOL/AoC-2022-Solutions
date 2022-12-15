use nom::{
    bytes::complete::tag,
    character::complete::i64,
    sequence::{preceded, separated_pair},
    IResult,
};

#[cfg(test)]
const Y: i64 = 10;
#[cfg(not(test))]
const Y: i64 = 2_000_000;

#[cfg(test)]
const LIMIT_COORD: i64 = 20;
#[cfg(not(test))]
const LIMIT_COORD: i64 = 4_000_000;

pub fn part1(input: &str) -> usize {
    let sensor_data: Vec<_> = input
        .lines()
        .map(|line| parse_line(line).unwrap().1)
        .collect();

    let mut min_x = i64::MAX;
    let mut max_x = i64::MIN;

    for (min_range, max_range) in sensor_data
        .iter()
        .filter_map(|&(sensor, closest_beacon)| min_max_pair(sensor, closest_beacon))
    {
        min_x = min_x.min(min_range);
        max_x = max_x.max(max_range);
    }

    let beacons_x: Vec<_> = sensor_data
        .iter()
        .filter(|(_, (_, y))| *y == Y)
        .map(|(_, (x, _))| *x)
        .collect();

    (min_x..=max_x)
        .filter(|&x| {
            sensor_data
                .iter()
                .map(|&(sensor, closest_beacon)| (sensor, manhattan(sensor, closest_beacon)))
                .any(|(sensor, d)| manhattan((x, Y), sensor) <= d)
                && !beacons_x.contains(&x)
        })
        .count()
}

pub fn part2(input: &str) -> i64 {
    let sensor_data: Vec<_> = input
        .lines()
        .map(|line| parse_line(line).unwrap().1)
        .collect();

    let distances = sensor_data
        .iter()
        .map(|&(sensor, closest_beacon)| (sensor, manhattan(sensor, closest_beacon)));

    for (sensor, d) in distances.clone() {
        for (x, y) in border(sensor, d.try_into().unwrap()) {
            if !(0..=LIMIT_COORD).contains(&x) || !(0..=LIMIT_COORD).contains(&y) {
                continue;
            }
            if distances
                .clone()
                .all(|(sensor, d)| manhattan((x, y), sensor) > d)
            {
                return x * 4_000_000 + y;
            }
        }
    }

    unreachable!()
}

fn min_max_pair((x1, y1): (i64, i64), closest_beacon: (i64, i64)) -> Option<(i64, i64)> {
    let d = manhattan((x1, y1), closest_beacon);
    let distance_to_y = y1.abs_diff(Y);
    let dx: i64 = (d >= distance_to_y)
        .then_some(d.wrapping_sub(distance_to_y))?
        .try_into()
        .unwrap();

    Some((x1 - dx, x1 + dx))
}

fn manhattan((x1, y1): (i64, i64), (x2, y2): (i64, i64)) -> u64 {
    x1.abs_diff(x2) + y1.abs_diff(y2)
}

fn border((x1, y1): (i64, i64), d: i64) -> impl Iterator<Item = (i64, i64)> {
    (0..d + 2)
        .map(move |dx| (dx, (d + 1) - dx))
        .flat_map(|deltas| {
            [(1, 1), (-1, 1), (-1, -1), (1, -1)]
                .into_iter()
                .map(move |signs| (deltas, signs))
        })
        .map(move |((dx, dy), (sgnx, sgny))| (x1 + (dx * sgnx), y1 + (dy * sgny)))
}

type SensorData = ((i64, i64), (i64, i64));

fn parse_line(input: &str) -> IResult<&str, SensorData> {
    preceded(
        tag("Sensor at x="),
        separated_pair(pair_parser, tag(": closest beacon is at x="), pair_parser),
    )(input)
}

fn pair_parser(input: &str) -> IResult<&str, (i64, i64)> {
    separated_pair(i64, tag(", y="), i64)(input)
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 26;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 56000011;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

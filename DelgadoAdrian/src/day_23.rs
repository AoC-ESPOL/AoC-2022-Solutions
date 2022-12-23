use std::collections::{hash_map::Entry, HashMap, HashSet};

const DIRECTIONS: [[(i32, i32); 3]; 4] = [
    [(-1, -1), (-1, 0), (-1, 1)], // N
    [(1, -1), (1, 0), (1, 1)],    // S
    [(1, -1), (0, -1), (-1, -1)], // W
    [(-1, 1), (0, 1), (1, 1)],    // E
];

const ADJ: [(i32, i32); 8] = [
    (0, 1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
];

pub fn part1(input: &str) -> usize {
    let mut ground = parse_ground(input);

    for round in 0..10 {
        let mut considered = HashMap::new();
        for &[x, y] in ground.iter() {
            // check if elf is alone
            if ADJ.into_iter().all(|(dx, dy)| {
                let (x_1, y_1) = (x + dx, y + dy);
                !ground.contains(&[x_1, y_1])
            }) {
                continue;
            };
            for deltas in DIRECTIONS.into_iter().cycle().skip(round % 4).take(4) {
                if deltas.into_iter().all(|(dx, dy)| {
                    let (x_1, y_1) = (x + dx, y + dy);
                    !ground.contains(&[x_1, y_1])
                }) {
                    let (dx, dy) = deltas[1];

                    let new_cell = [x + dx, y + dy];
                    match considered.entry(new_cell) {
                        Entry::Occupied(mut entry) => {
                            entry.insert(None);
                        }
                        Entry::Vacant(entry) => {
                            entry.insert(Some([x, y]));
                        }
                    };
                    break;
                }
            }
        }

        // populate considered
        for (to, from) in considered {
            let Some(from) = from else { continue; };
            ground.insert(to);
            ground.remove(&from);
        }
    }

    let mut min_x = i32::MAX;
    let mut max_x = i32::MIN;

    let mut min_y = i32::MAX;
    let mut max_y = i32::MIN;

    for &[x, y] in ground.iter() {
        min_x = min_x.min(x);
        max_x = max_x.max(x);
        min_y = min_y.min(y);
        max_y = max_y.max(y);
    }

    ((max_x - min_x + 1) * (max_y - min_y + 1)) as usize
        - ground
            .into_iter()
            .filter(|&[x, y]| ((min_x..=max_x).contains(&x) && (y..=max_y).contains(&y)))
            .count()
}

pub fn part2(input: &str) -> usize {
    let mut ground = parse_ground(input);

    for round in 0.. {
        let mut considered = HashMap::new();
        for &[x, y] in ground.iter() {
            // check if elf is alone
            if ADJ.into_iter().all(|(dx, dy)| {
                let (x_1, y_1) = (x + dx, y + dy);
                !ground.contains(&[x_1, y_1])
            }) {
                continue;
            };
            for deltas in DIRECTIONS.into_iter().cycle().skip(round % 4).take(4) {
                if deltas.into_iter().all(|(dx, dy)| {
                    let (x_1, y_1) = (x + dx, y + dy);
                    !ground.contains(&[x_1, y_1])
                }) {
                    let (dx, dy) = deltas[1];

                    let new_cell = [x + dx, y + dy];
                    match considered.entry(new_cell) {
                        Entry::Occupied(mut entry) => {
                            entry.insert(None);
                        }
                        Entry::Vacant(entry) => {
                            entry.insert(Some([x, y]));
                        }
                    };
                    break;
                }
            }
        }

        if considered.is_empty() {
            return round + 1;
        }

        // populate considered
        for (to, from) in considered {
            let Some(from) = from else { continue; };
            ground.insert(to);
            ground.remove(&from);
        }
    }

    unreachable!()
}

fn parse_ground(input: &str) -> HashSet<[i32; 2]> {
    let mut gr = HashSet::new();

    for (x, line) in input.lines().enumerate() {
        for (y, chr) in line.chars().enumerate() {
            if chr == '#' {
                gr.insert([x as i32, y as i32]);
            }
        }
    }

    gr
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 110;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 20;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

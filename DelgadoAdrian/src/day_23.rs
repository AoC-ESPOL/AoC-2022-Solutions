use std::collections::{hash_map::Entry, HashMap};

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

pub fn part1(input: &str) -> i32 {
    let mut ground = parse_ground(input); // 1 -> elf, 0 -> empty

    for round in 0..10 {
        let mut considered = HashMap::new();
        for (&[x, y], _) in ground.iter().filter(|&(_, chr)| *chr == 1) {
            // check if elf is alone
            if ADJ.into_iter().all(|(dx, dy)| {
                let (x_1, y_1) = (x + dx, y + dy);
                ground.get(&[x_1, y_1]) != Some(&1)
            }) {
                continue;
            };
            for deltas in DIRECTIONS.into_iter().cycle().skip(round % 4).take(4) {
                if deltas.into_iter().all(|(dx, dy)| {
                    let (x_1, y_1) = (x + dx, y + dy);
                    ground.get(&[x_1, y_1]) != Some(&1)
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
            ground.insert(to, 1);
            ground.insert(from, 0);
        }
    }

    let mut min_x = i32::MAX;
    let mut max_x = i32::MIN;

    let mut min_y = i32::MAX;
    let mut max_y = i32::MIN;

    for (&[x, y], _) in ground.iter().filter(|&(_, n)| *n == 1) {
        min_x = min_x.min(x);
        max_x = max_x.max(x);
        min_y = min_y.min(y);
        max_y = max_y.max(y);
    }

    (max_x - min_x + 1) * (max_y - min_y + 1)
        - ground
            .into_iter()
            .filter_map(|([x, y], t)| {
                ((min_x..=max_x).contains(&x) && (y..=max_y).contains(&y)).then_some(t)
            })
            .sum::<i32>()
}

pub fn part2(input: &str) -> usize {
    let mut ground = parse_ground(input); // 1 -> elf, 0 -> empty

    for round in 0.. {
        let mut considered = HashMap::new();
        for (&[x, y], _) in ground.iter().filter(|&(_, chr)| *chr == 1) {
            // check if elf is alone
            if ADJ.into_iter().all(|(dx, dy)| {
                let (x_1, y_1) = (x + dx, y + dy);
                ground.get(&[x_1, y_1]) != Some(&1)
            }) {
                continue;
            };
            for deltas in DIRECTIONS.into_iter().cycle().skip(round % 4).take(4) {
                if deltas.into_iter().all(|(dx, dy)| {
                    let (x_1, y_1) = (x + dx, y + dy);
                    ground.get(&[x_1, y_1]) != Some(&1)
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
            ground.insert(to, 1);
            ground.insert(from, 0);
        }
    }

    unreachable!()
}

fn parse_ground(input: &str) -> HashMap<[i32; 2], i32> {
    let mut gr = HashMap::new();

    for (x, line) in input.lines().enumerate() {
        for (y, chr) in line.chars().enumerate() {
            let tile = match chr {
                '.' => 0,
                '#' => 1,
                _ => unreachable!(),
            };
            gr.insert([x as i32, y as i32], tile);
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

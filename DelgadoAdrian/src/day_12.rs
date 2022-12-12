use ndarray::Array2;

use petgraph::{algo::astar, prelude::*};

pub fn part1(input: &str) -> i32 {
    let cols = input.find("\n").unwrap();
    let rows = input.trim_end().lines().count();
    let arr = Array2::<i32>::from_shape_vec(
        (rows, cols),
        input
            .replace("\n", "")
            .as_bytes()
            .into_iter()
            .map(|&ch| match ch {
                b'S' => b'a',
                b'E' => b'z',
                _ => ch,
            } as i32)
            .collect(),
    )
    .unwrap();

    let mut gr = DiGraphMap::new();
    for (row, line) in arr.rows().into_iter().enumerate() {
        for (col, ch) in line.into_iter().enumerate() {
            gr.add_node([row, col]);

            if row < rows - 1 && (arr[[row + 1, col]] - ch) <= 1 {
                gr.add_edge([row, col], [row + 1, col], 1_i32);
            }
            if row > 0 && (arr[[row - 1, col]] - ch) <= 1 {
                gr.add_edge([row, col], [row - 1, col], 1);
            }
            if col > 0 && (arr[[row, col - 1]] - ch) <= 1 {
                gr.add_edge([row, col], [row, col - 1], 1);
            }
            if col < cols - 1 && (arr[[row, col + 1]] - ch) <= 1 {
                gr.add_edge([row, col], [row, col + 1], 1);
            }
        }
    }

    astar(&gr, [20, 0], |f| f == [20, 40], |e| *e.weight(), |_| 0_i32)
        .unwrap()
        .0
}

pub fn part2(input: &str) -> i32 {
    let cols = input.find("\n").unwrap();
    let rows = input.trim_end().lines().count();
    let arr = Array2::<i32>::from_shape_vec(
        (rows, cols),
        input
            .replace("\n", "")
            .as_bytes()
            .into_iter()
            .map(|&ch| match ch {
                b'S' => b'a',
                b'E' => b'z',
                _ => ch,
            } as i32)
            .collect(),
    )
    .unwrap();

    let mut gr = DiGraphMap::new();
    for (row, line) in arr.rows().into_iter().enumerate() {
        for (col, ch) in line.into_iter().enumerate() {
            gr.add_node([row, col]);

            if row < rows - 1 && (arr[[row + 1, col]] - ch) <= 1 {
                gr.add_edge([row, col], [row + 1, col], 1_i32);
            }
            if row > 0 && (arr[[row - 1, col]] - ch) <= 1 {
                gr.add_edge([row, col], [row - 1, col], 1);
            }
            if col > 0 && (arr[[row, col - 1]] - ch) <= 1 {
                gr.add_edge([row, col], [row, col - 1], 1);
            }
            if col < cols - 1 && (arr[[row, col + 1]] - ch) <= 1 {
                gr.add_edge([row, col], [row, col + 1], 1);
            }
        }
    }

    let mut fewest_steps = 370;

    for (row, line) in arr.rows().into_iter().enumerate() {
        for (col, ch) in line.into_iter().enumerate() {
            if *ch == (b'a' as i32) {
                fewest_steps = fewest_steps.min(
                    astar(
                        &gr,
                        [row, col],
                        |f| f == [20, 40],
                        |e| *e.weight(),
                        |_| 0_i32,
                    )
                    .unwrap_or((370, vec![]))
                    .0,
                );
            }
        }
    }

    fewest_steps
}

// #[cfg(test)]
// mod tests {
//     use super::{part1, part2};

//     const TEST_INPUT: &str = "\
// ";

//     #[test]
//     fn part1_works() {
//         let output = 24000;

//         assert_eq!(part1(TEST_INPUT), output);
//     }

//     #[test]
//     fn part2_works() {
//         let output = 45000;

//         assert_eq!(part2(TEST_INPUT), output);
//     }
// }

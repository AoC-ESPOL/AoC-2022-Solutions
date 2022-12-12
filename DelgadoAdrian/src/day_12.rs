use bstr::ByteSlice;
use ndarray::Array2;
use petgraph::{algo::astar, prelude::*};

fn create_array(rows: usize, cols: usize, input: Vec<u8>) -> Array2<i32> {
    Array2::from_shape_vec(
        (rows, cols),
        input
            .into_iter()
            .map(|ch| {
                i32::from(match ch {
                    b'S' => b'a',
                    b'E' => b'z',
                    _ => ch,
                })
            })
            .collect(),
    )
    .unwrap()
}

fn create_graph(arr: &Array2<i32>, rows: usize, cols: usize) -> DiGraphMap<[usize; 2], ()> {
    let mut gr = DiGraphMap::new();
    for (row, line) in arr.rows().into_iter().enumerate() {
        for (col, ch) in line.into_iter().enumerate() {
            gr.add_node([row, col]);

            if row < rows - 1 && (arr[[row + 1, col]] - ch) <= 1 {
                gr.add_edge([row, col], [row + 1, col], ());
            }
            if row > 0 && (arr[[row - 1, col]] - ch) <= 1 {
                gr.add_edge([row, col], [row - 1, col], ());
            }
            if col > 0 && (arr[[row, col - 1]] - ch) <= 1 {
                gr.add_edge([row, col], [row, col - 1], ());
            }
            if col < cols - 1 && (arr[[row, col + 1]] - ch) <= 1 {
                gr.add_edge([row, col], [row, col + 1], ());
            }
        }
    }
    gr
}

pub fn part1(input: &str) -> i32 {
    let cols = input.find('\n').unwrap();
    let rows = input.trim_end().lines().count();
    let input = Vec::from(input.replace('\n', ""));
    let start = {
        let idx = input.find("S").unwrap();
        [idx / cols, idx % cols]
    };
    let end = {
        let idx = input.find("E").unwrap();
        [idx / cols, idx % cols]
    };

    let arr = create_array(rows, cols, input);

    let gr = create_graph(&arr, rows, cols);

    astar(&gr, start, |f| f == end, |_| 1, |_| 0).unwrap().0
}

pub fn part2(input: &str) -> i32 {
    let cols = input.find('\n').unwrap();
    let rows = input.trim_end().lines().count();
    let input = Vec::from(input.replace('\n', ""));
    let end = {
        let idx = input.find("E").unwrap();
        [idx / cols, idx % cols]
    };

    let arr = create_array(rows, cols, input);

    let gr = create_graph(&arr, rows, cols);

    let mut fewest_steps = i32::MAX;

    for (row, line) in arr.rows().into_iter().enumerate() {
        for (col, ch) in line.into_iter().enumerate() {
            if *ch == i32::from(b'a') {
                let Some((steps, _)) =
                    astar(&gr, [row, col], |f| f == end, |_| 1, |_| 0) else { continue; };

                fewest_steps = fewest_steps.min(steps);
            }
        }
    }

    fewest_steps
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi";

    #[test]
    fn part1_works() {
        let output = 31;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    fn part2_works() {
        let output = 29;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

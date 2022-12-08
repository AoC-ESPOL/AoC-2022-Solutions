use ndarray::{s, Array2, ArrayView1};
use ndarray_stats::QuantileExt;

pub fn part1(input: &str) -> u32 {
    let size = input.find('\n').unwrap();
    let grid = Array2::from_shape_vec((size, size), input.replace("\n", "").into_bytes()).unwrap();
    let mut visible = Array2::zeros((size, size));
    for (x, row) in grid.rows().into_iter().enumerate() {
        set_visible::<false>(&mut visible, row, x);
    }
    for (y, col) in grid.columns().into_iter().enumerate() {
        set_visible::<true>(&mut visible, col, y);
    }

    visible.sum()
}

fn set_visible<const TRANSPOSE: bool>(visible: &mut Array2<u32>, lane: ArrayView1<u8>, pos: usize) {
    let mut height = 0;

    for (idx, num) in lane.iter().copied().enumerate() {
        let [x, y] = if TRANSPOSE { [idx, pos] } else { [pos, idx] };

        if num > height {
            visible[[x, y]] = 1;
            height = num;
        }
    }

    let mut height = 0;

    for (idx, num) in lane.iter().copied().enumerate().rev() {
        let [x, y] = if TRANSPOSE { [idx, pos] } else { [pos, idx] };

        if num > height {
            visible[[x, y]] = 1;
            height = num;
        }
    }
}

pub fn part2(input: &str) -> u32 {
    let size = input.find('\n').unwrap();
    let grid = Array2::from_shape_vec((size, size), input.replace("\n", "").into_bytes()).unwrap();
    let mut scores = Array2::ones((size, size));
    for (x, row) in grid.rows().into_iter().enumerate() {
        set_scores::<false>(&mut scores, row, x);
    }
    for (y, col) in grid.columns().into_iter().enumerate() {
        set_scores::<true>(&mut scores, col, y);
    }

    *scores.max().unwrap()
}

fn set_scores<const TRANSPOSE: bool>(scores: &mut Array2<u32>, lane: ArrayView1<u8>, pos: usize) {
    for (idx, num) in lane.iter().enumerate() {
        let mut score = 0;

        for n in lane.slice(s![..idx;-1]) {
            score += 1;
            if n >= num {
                break;
            }
        }

        let [x, y] = if TRANSPOSE { [idx, pos] } else { [pos, idx] };

        scores[[x, y]] *= score;
    }

    for (idx, num) in lane.iter().enumerate().rev() {
        let mut score = 0;

        for n in lane.slice(s![idx + 1..]) {
            score += 1;
            if n >= num {
                break;
            }
        }

        let [x, y] = if TRANSPOSE { [idx, pos] } else { [pos, idx] };

        scores[[x, y]] *= score;
    }
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    const TEST_INPUT: &str = "\
30373
25512
65332
33549
35390";

    #[test]
    #[ignore]
    fn part1_works() {
        let output = 21;

        assert_eq!(part1(TEST_INPUT), output);
    }

    #[test]
    #[ignore]
    fn part2_works() {
        let output = 8;

        assert_eq!(part2(TEST_INPUT), output);
    }
}

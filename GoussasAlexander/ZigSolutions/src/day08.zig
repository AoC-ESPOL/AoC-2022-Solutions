const std = @import("std");
const Grid = @import("./grid.zig");

fn charToInt(c: u8) i32 {
    return c - '0';
}

pub fn partOne(input: []const u8) !usize {
    var grid = try Grid.fromString(i32, charToInt, input);
    var visibleTrees = grid.rows * 2 + (grid.cols - 2) * 2;

    var i: usize = 1;
    while (i < grid.rows - 1) : (i += 1) {
        var j: usize = 1;
        while (j < grid.cols - 1) : (j += 1) {
            const currentItem = grid.get(i, j);
            var idx = @intCast(i32, i - 1);
            var isVisible = false;

            // Check up
            while (idx >= 0 and grid.get(@intCast(usize, idx), j) < currentItem) : (idx -= 1) {}
            isVisible = isVisible or idx < 0;

            // Check down
            idx = @intCast(i32, i + 1);
            while (!isVisible and idx < grid.rows and grid.get(@intCast(usize, idx), j) < currentItem) : (idx += 1) {}
            isVisible = isVisible or idx == grid.rows;

            // Check left
            idx = @intCast(i32, j - 1);
            while (!isVisible and idx >= 0 and grid.get(i, @intCast(usize, idx)) < currentItem) : (idx -= 1) {}
            isVisible = isVisible or idx < 0;

            // Check right
            idx = @intCast(i32, j + 1);
            while (!isVisible and idx < grid.cols and grid.get(i, @intCast(usize, idx)) < currentItem) : (idx += 1) {}
            isVisible = isVisible or idx == grid.cols;

            visibleTrees += if (isVisible) 1 else 0;
        }
    }

    return visibleTrees;
}

pub fn partTwo(input: []const u8) !usize {
    var grid = try Grid.fromString(i32, charToInt, input);

    var maxScenicScore: usize = 0;
    var i: i32 = 1;

    while (i < grid.rows - 1) : (i += 1) {
        var j: i32 = 1;
        while (j < grid.cols - 1) : (j += 1) {
            const currentItem = grid.get(@intCast(usize, i), @intCast(usize, j));
            var treeScenicScore = [_]usize{0} ** 4;

            var idx = i - 1;
            // Check up
            while (idx >= 0) : (idx -= 1) {
                treeScenicScore[0] += 1;
                if (grid.get(@intCast(usize, idx), @intCast(usize, j)) >= currentItem)
                    break;
            }

            // Check down
            idx = i + 1;
            while (idx < grid.rows) : (idx += 1) {
                treeScenicScore[1] += 1;
                if (grid.get(@intCast(usize, idx), @intCast(usize, j)) >= currentItem)
                    break;
            }

            // Check left
            idx = j - 1;
            while (idx >= 0) : (idx -= 1) {
                treeScenicScore[2] += 1;
                if (grid.get(@intCast(usize, i), @intCast(usize, idx)) >= currentItem)
                    break;
            }

            // Check right
            idx = j + 1;
            while (idx < grid.cols) : (idx += 1) {
                treeScenicScore[3] += 1;
                if (grid.get(@intCast(usize, i), @intCast(usize, idx)) >= currentItem)
                    break;
            }

            const score = treeScenicScore[0] * treeScenicScore[1] * treeScenicScore[2] * treeScenicScore[3];
            maxScenicScore = std.math.max(maxScenicScore, score);
        }
    }

    return maxScenicScore;
}

test "Part one with the example input returns 21" {
    const input = @embedFile("./day08-sample.txt");
    const result = try partOne(input);
    try std.testing.expectEqual(@as(usize, 21), result);
}

test "Part two with the example input returns 8" {
    const input = @embedFile("./day08-sample.txt");
    const result = try partTwo(input);
    try std.testing.expectEqual(@as(usize, 8), result);
}

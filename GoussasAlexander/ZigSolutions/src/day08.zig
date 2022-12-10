const std = @import("std");
const Grid = @import("./grid.zig");
var gpa = std.heap.GeneralPurposeAllocator(.{}){};
var allocator = gpa.allocator();

fn charToInt(c: u8) i32 {
    return c - '0';
}

pub fn partOne(input: []const u8) !usize {
    var grid = try Grid.fromString(i32, allocator, charToInt, input);
    defer grid.deinit();

    var gridIterator = grid.iterator();
    var visibleTrees: usize = 0;

    while (gridIterator.next()) |gridItem| {
        const i: usize = gridItem.row;
        const j: usize = gridItem.col;
        const item: i32 = gridItem.item.*;

        var idx: i32 = undefined;
        var isVisible = false;

        // Check up
        idx = @intCast(i32, @intCast(i32, i) - 1);
        while (idx >= 0 and grid.get(@intCast(usize, idx), j) < item) : (idx -= 1) {}
        isVisible = isVisible or idx < 0;

        // Check down
        idx = @intCast(i32, i + 1);
        while (!isVisible and idx < grid.rows and grid.get(@intCast(usize, idx), j) < item) : (idx += 1) {}
        isVisible = isVisible or idx == grid.rows;

        // Check left
        idx = @intCast(i32, @intCast(i32, j) - 1);
        while (!isVisible and idx >= 0 and grid.get(i, @intCast(usize, idx)) < item) : (idx -= 1) {}
        isVisible = isVisible or idx < 0;

        // Check right
        idx = @intCast(i32, j + 1);
        while (!isVisible and idx < grid.cols and grid.get(i, @intCast(usize, idx)) < item) : (idx += 1) {}
        isVisible = isVisible or idx == grid.cols;

        visibleTrees += if (isVisible) 1 else 0;
    }

    return visibleTrees;
}

pub fn partTwo(input: []const u8) !usize {
    var grid = try Grid.fromString(i32, allocator, charToInt, input);
    var gridIterator = grid.iterator();
    var maxScenicScore: usize = 0;

    while (gridIterator.next()) |gridItem| {
        const i: usize = gridItem.row;
        const j: usize = gridItem.col;
        const item = gridItem.item.*;

        var treeScenicScore = [_]usize{0} ** 4;
        var idx: i32 = undefined;

        // Check up
        idx = @intCast(i32, i) - 1;
        while (idx >= 0) : (idx -= 1) {
            treeScenicScore[0] += 1;
            if (grid.get(@intCast(usize, idx), j) >= item) break;
        }

        // Check down
        idx = @intCast(i32, i) + 1;
        while (idx < grid.rows) : (idx += 1) {
            treeScenicScore[1] += 1;
            if (grid.get(@intCast(usize, idx), j) >= item) break;
        }

        // Check left
        idx = @intCast(i32, j) - 1;
        while (idx >= 0) : (idx -= 1) {
            treeScenicScore[2] += 1;
            if (grid.get(i, @intCast(usize, idx)) >= item) break;
        }

        // Check right
        idx = @intCast(i32, j) + 1;
        while (idx < grid.cols) : (idx += 1) {
            treeScenicScore[3] += 1;
            if (grid.get(i, @intCast(usize, idx)) >= item) break;
        }

        const score = treeScenicScore[0] * treeScenicScore[1] * treeScenicScore[2] * treeScenicScore[3];
        maxScenicScore = std.math.max(maxScenicScore, score);

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

const std = @import("std");

pub fn partOne(input: []const u8) !usize {
    var elfIterator = std.mem.split(u8, input, "\n\n");
    var maxCalories: usize = 0;

    while (elfIterator.next()) |elf| {
        var lines_it = std.mem.tokenize(u8, elf, "\n");
        var elfCalories: usize = 0;

        while (lines_it.next()) |line| {
            elfCalories += try std.fmt.parseInt(usize, line, 10);
        }

        maxCalories = std.math.max(maxCalories, elfCalories);
    }

    return maxCalories;
}

pub fn partTwo(input: []const u8) !usize {
    var elfIterator = std.mem.split(u8, input, "\n\n");
    var topThreeCalories = [_]usize{0} ** 3;

    while (elfIterator.next()) |elf| {
        var lines_it = std.mem.tokenize(u8, elf, "\n");
        var elfCalories: usize = 0;

        while (lines_it.next()) |line| {
            elfCalories += try std.fmt.parseInt(usize, line, 10);
        }

        if (elfCalories > topThreeCalories[0]) {
            topThreeCalories[1] = topThreeCalories[0];
            topThreeCalories[0] = elfCalories;
        } else if (elfCalories > topThreeCalories[1]) {
            topThreeCalories[2] = topThreeCalories[1];
            topThreeCalories[1] = elfCalories;
        } else if (elfCalories > topThreeCalories[2]) {
            topThreeCalories[2] = elfCalories;
        }
    }

    return topThreeCalories[0] + topThreeCalories[1] + topThreeCalories[2];
}

test "Example input works" {
    const input: []const u8 = @embedFile("day01-sample.txt");
    var result = try partOne(input);
    try std.testing.expectEqual(@as(usize, 24000), result);
}

test "Puzzle input for part one works" {
    const input: []const u8 = @embedFile("day01.txt");
    var result = try partOne(input);
    try std.testing.expectEqual(@as(usize, 69795), result);
}

test "Example input for part two works" {
    const input: []const u8 = @embedFile("day01-sample.txt");
    var result = try partTwo(input);
    try std.testing.expectEqual(@as(usize, 45000), result);
}

test "Puzzle input for part one works" {
    const input: []const u8 = @embedFile("day01.txt");
    var result = try partTwo(input);
    try std.testing.expectEqual(@as(usize, 208437), result);
}

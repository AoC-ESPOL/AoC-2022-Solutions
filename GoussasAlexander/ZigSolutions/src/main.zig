const std = @import("std");

const input = @embedFile("./day07.txt");
const day = @import("./day07.zig");

pub fn main() !void {
    const partOne = try day.partOne(input);
    const partTwo = try day.partTwo(input);
    std.debug.print("Part one = {}\n", .{partOne});
    std.debug.print("Part two = {}\n", .{partTwo});
}

const std = @import("std");
var gpa = std.heap.GeneralPurposeAllocator(.{}){};
var allocator = gpa.allocator();

pub fn Grid2D(comptime T: type) type {
    return struct {
        const Self = @This();

        cols: usize,
        rows: usize,
        grid: std.ArrayList(std.ArrayList(T)),

        pub fn init(rows_: usize, cols_: usize) !Self {
            if (rows_ == 0 or cols_ == 0) return empty();

            var grid = try std.ArrayList(std.ArrayList(T)).initCapacity(allocator, rows_);
            grid.expandToCapacity();

            var i: usize = 0;
            while (i < rows_) : (i += 1) {
                grid.items[i] = try std.ArrayList(T).initCapacity(allocator, cols_);
                grid.items[i].expandToCapacity();
            }

            return Self{
                .cols = cols_,
                .rows = rows_,
                .grid = grid,
            };
        }

        pub fn empty() !Self {
            return Self{
                .cols = 0,
                .rows = 0,
                .grid = std.ArrayList(std.ArrayList(T)).init(allocator),
            };
        }

        pub fn set(self: *Self, x: usize, y: usize, elem: T) void {
            self.grid.items[x].items[y] = elem;
        }

        pub fn get(self: *const Self, x: usize, y: usize) T {
            return self.grid.items[x].items[y];
        }

        pub fn print(self: *const Self) void {
            for (self.grid) |row| {
                for (row) |tree| {
                    std.debug.print("{}", .{tree});
                }
                std.debug.print("\n", .{});
            }
        }
    };
}

pub fn fromString(comptime T: type, comptime convert: *const fn (u8) T, input: []const u8) !Grid2D(T) {
    var lines = std.mem.tokenize(u8, input, "\n");

    var rows: usize = blk: {
        var rows = std.mem.count(u8, input, "\n");
        if (std.mem.endsWith(u8, input, "\n")) {
            rows -= 1;
        }
        break :blk rows;
    };

    var cols: usize = undefined;
    var aLine: []const u8 = undefined;

    if (lines.next()) |line| {
        cols = line.len;
        aLine = line;
    } else return Grid2D(i32).init(0, 0);

    var grid = try Grid2D(i32).init(rows, cols);

    for (aLine) |c, idx| {
        grid.set(0, idx, convert(c));
    }

    var i: usize = 1;

    while (lines.next()) |line| : (i += 1) {
        for (line) |c, idx| {
            grid.set(i, idx, convert(c));
        }
    }

    return grid;
}

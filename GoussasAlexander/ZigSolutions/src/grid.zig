const std = @import("std");

pub fn Grid2DIterator(comptime T: type) type {
    const Item = struct {
        row: usize,
        col: usize,
        item: *const T,
    };

    return struct {
        const Self = @This();

        row: usize,
        col: usize,
        hasNext: bool = true,
        grid: *Grid2D(T),

        pub fn new(grid: *Grid2D(T)) Self {
            return Self{
                .row = 0,
                .col = 0,
                .hasNext = true,
                .grid = grid,
            };
        }

        pub fn next(self: *Self) ?Item {
            if (!self.hasNext) return null;

            var row: usize = self.row;
            var col: usize = self.col;

            std.debug.assert(row < self.grid.rows and col < self.grid.cols);

            // Handle specially the case where we are on the last cell.
            if (self.row == self.grid.rows - 1 and self.col == self.grid.cols - 1) {
                self.hasNext = false;
            } else {
                self.row = if (self.col+1 >= self.grid.cols) self.row+1 else self.row;
                self.col = (self.col+1) % self.grid.cols;
            }

            return Item{
                .row = row,
                .col = col,
                .item = &self.grid.get(row, col),
            };
        }
    };
}

pub fn Grid2D(comptime T: type) type {
    return struct {
        const Self = @This();

        cols: usize,
        rows: usize,
        grid: std.ArrayList(std.ArrayList(T)),

        pub fn init(allocator: std.mem.Allocator, rows_: usize, cols_: usize) !Self {
            if (rows_ == 0 or cols_ == 0) return empty(allocator);

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

        pub fn deinit(self: *Self) void {
            var i: usize = 0;
            while (i < self.rows) : (i += 1) {
                self.grid.items[i].deinit();
            }
            self.grid.deinit();
        }

        pub fn empty(allocator: std.mem.Allocator) !Self {
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

        /// Return an iterator to the cells of the grid.
        pub fn iterator(self: *Self) Grid2DIterator(T) {
            return Grid2DIterator(T).new(self);
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

pub fn fromString(
    comptime T: type,
    allocator: std.mem.Allocator,
    comptime convert: *const fn (u8) T,
    input: []const u8) !Grid2D(T) {
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
    } else return Grid2D(i32).init(allocator, 0, 0);

    var grid = try Grid2D(i32).init(allocator, rows, cols);

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

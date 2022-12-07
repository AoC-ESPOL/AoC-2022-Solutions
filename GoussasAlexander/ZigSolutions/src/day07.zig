const std = @import("std");
var gpa = std.heap.GeneralPurposeAllocator(.{}){};
var allocator = gpa.allocator();

const File = struct {
    size: usize,

    pub fn new(size: usize) File {
        return .{ .size = size };
    }
};

const Directory = struct {
    contents: std.ArrayList(Node),

    pub fn new() Directory {
        return .{ .contents = std.ArrayList(Node).init(allocator) };
    }
};

const NodeTag = enum {
    file,
    directory,
};

const Node = struct {
    parent: ?*Node = null,
    type: NodeTag,
    as: union(NodeTag) {
        file: File,
        directory: Directory,
    },
    name: []const u8,

    pub fn newDirectory(name: []const u8, parent: ?*Node, directory: Directory) Node {
        return .{
            .name = name,
            .parent = parent,
            .type = .directory,
            .as = .{ .directory = directory },
        };
    }

    pub fn newFile(name: []const u8, parent: *Node, file: File) Node {
        return .{
            .name = name,
            .parent = parent,
            .type = .file,
            .as = .{ .file = file },
        };
    }

    pub fn isDirectory(self: *const @This()) bool {
        return switch (self.type) {
            .directory => true,
            else => false,
        };
    }

    pub fn size(self: *const @This()) usize {
        return switch (self.type) {
            .file => self.as.file.size,
            .directory => blk: {
                var nodeSize: usize = 0;
                for (self.as.directory.contents.items) |*node| {
                    nodeSize += node.size();
                }
                break :blk nodeSize;
            },
        };
    }
};

fn calculateTotalSize(root: *const Node) usize {
    return switch (root.type) {
        .file => 0,
        .directory => blk: {
            var size: usize = 0;
            if (root.size() < 100000) {
                size += root.size();
            }
            for (root.as.directory.contents.items) |*node| {
                size += calculateTotalSize(node);
            }
            break :blk size;
        },
    };
}

fn buildFileSystem(input: []const u8) !Node {
    var lines = std.mem.tokenize(u8, input, "\n");
    var root = Node.newDirectory("/", null, Directory.new());
    var currentDirectory: *Node = &root;

    // Skip root cd.
    _ = lines.next();

    while (lines.next()) |line| {
        if (std.mem.startsWith(u8, line, "$ cd")) {
            const dirname = line[5..];
            if (std.mem.eql(u8, dirname, "..")) {
                currentDirectory = currentDirectory.parent.?;
            } else {
                var directory: *Node = undefined;
                for (currentDirectory.as.directory.contents.items) |*file| {
                    directory = switch (file.type) {
                        .directory => if (std.mem.eql(u8, file.name, dirname)) file else directory,
                        .file => directory,
                    };
                }
                currentDirectory = directory;
            }
        } else if (std.mem.startsWith(u8, line, "dir")) {
            const dirname = line[4..];
            const directory = Node.newDirectory(dirname, currentDirectory, Directory.new());
            try currentDirectory.as.directory.contents.append(directory);
        } else if (!std.mem.eql(u8, line, "$ ls")) {
            var it = std.mem.tokenize(u8, line, " ");
            const fileSize = try std.fmt.parseInt(usize, it.next().?, 10);
            const fileName = it.next().?;
            const file = Node.newFile(fileName, currentDirectory, File.new(fileSize));
            try currentDirectory.as.directory.contents.append(file);
        }
    }
    return root;
}

pub fn partOne(input: []const u8) !usize {
    const root = try buildFileSystem(input);
    return calculateTotalSize(&root);
}

pub fn partTwo(input: []const u8) !usize {
    const root = try buildFileSystem(input);
    const freeSpace = 70000000 - root.size();
    const spaceToFree = 30000000 - freeSpace;

    var stack = std.ArrayList(Node).init(allocator);
    try stack.append(root);

    var totalSize = root.size();

    while (stack.items.len > 0) {
        const node = stack.pop();
        const size = node.size();

        if (size >= spaceToFree) {
            totalSize = std.math.min(totalSize, size);
        }

        for (node.as.directory.contents.items) |item| {
            if (item.isDirectory()) {
                try stack.append(item);
            }
        }
    }

    return totalSize;
}

test "Part one for the sample input works" {
    const input: []const u8 = @embedFile("./day07-sample.txt");
    const result = try partOne(input);
    try std.testing.expectEqual(@as(usize, 95437), result);
}

test "Part two for the sample input returns 24933642" {
    const input: []const u8 = @embedFile("./day07-sample.txt");
    const result = try partTwo(input);
    try std.testing.expectEqual(@as(usize, 24933642), result);
}

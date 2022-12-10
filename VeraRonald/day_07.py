def get_tree(file):
    tree = {}
    try:
        with open(file, 'r') as file:
            lines  = file.readlines()
            info_directory = [] #  lines correspondent to the directory content
            wait_answer = ""
            location = ""
            for line in lines:
                line = line.strip()
                # Is it a command?
                if "$" in line:
                    command_composition = line.split()
                    # What type of command is this?
                    command_type = command_composition[1]

                    # Before, resolve wait process
                    if wait_answer == "ls":
                        if len(info_directory) != 0:
                            content_directory = get_content_directory(info_directory)
                            tree[location] = content_directory
                            info_directory.clear()

                    if command_type == "cd":
                        current_directory = command_composition[2]
                        if current_directory == "..":
                            location = "/".join(location.split("/")[:-2]) + "/"
                            if not location:
                                location = "/"
                        else:
                            if current_directory != "/":
                                location += f"{current_directory}/"
                            else:
                                location += f"{current_directory}"
                    elif command_type == "ls":
                            wait_answer = command_type
                else:
                    if wait_answer == "ls":
                        info_directory.append(line)

            locations = tree.keys()
            locations_by_level = {}
            for location in locations:
                level = len(location[1:].split("/"))-1
                if level in locations_by_level:
                    locations_by_level[level] += [location]
                else:
                    locations_by_level[level] = [location]

            # Update size since back
            directories_and_size = {}

            for level, locations in list(locations_by_level.items())[::-1]:
                for location in locations:
                    real_size = 0
                    content_directory = tree[location]
                    # Here, have we internal dirs?
                    real_size += content_directory[-1]
                    if len(content_directory[0].keys()) != 0:
                        for internal_dir in content_directory[0].keys():
                            internal_dir = f"{location}{internal_dir}/"
                            if internal_dir in tree:
                                relative_size = tree[internal_dir][-1]
                                real_size += relative_size
                        tree[location] = tree[location][:-1] + [real_size]
                    directories_and_size[location] = real_size
            return directories_and_size
    except FileNotFoundError:
        print('File not found')

def get_content_directory(info_directory):
    content_directory = []
    directory = {}
    file = {}
    relative_size = 0
    for i in info_directory:
        info = i.split()
        # The current info corresponds to a directory or a file
        if "dir" in info:
            directory[info[1]] = []
        else:
            file_size, file_name = info
            relative_size += int(file_size)
            file[file_name] = int(file_size)
    content_directory.append(directory)
    content_directory.append(file)
    content_directory.append(relative_size)
    return content_directory

tree = get_tree("input.txt")
# PART 1
sum_of_size_directories = sum([value for key, value in tree.items() if value<=100000])
print(sum_of_size_directories)
# PART 2
space_available = 70000000
necessary_space = 30000000
unused_space = space_available - tree["/"]
smallest_directory = ""
for key, value in get_tree("input.txt").items():
    if unused_space + value >= necessary_space:
        smallest_directory += key
        break
print(tree[smallest_directory])
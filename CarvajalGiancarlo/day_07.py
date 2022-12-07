print("\n¡AoC! - Day 07\n")

print('Part One\n\n')

file = open('input_day_07.txt', 'r')

tree = {}
space_dict = {}

current_tree = tree
current_key = ''

tree_stack = []
tree_stack.insert(0, current_tree)

key_stack = []

while True:
    line = file.readline()
    if(len(line) == 0):
        break

    if '$ ls' in line:
        continue

    elif '$ cd' in line:
        dir = line.split(" ")[2].replace('\n', '')

        if dir == '..':
            tree_stack.pop(0)
            key_stack.pop(0)

            current_tree = tree_stack[0]
            current_key = key_stack[0]
            continue

        current_tree.setdefault(dir, {})
        space_dict.setdefault(current_key+dir, 0)

        current_tree = current_tree[dir]
        current_key += dir

        tree_stack.insert(0, current_tree)
        key_stack.insert(0, current_key)
    
    elif 'dir' in line:
        dir = line.split(" ")[1].replace('\n', '')
        current_tree.setdefault(dir, {})
        space_dict.setdefault(current_key+dir, 0)
    
    else:
        space_dict[current_key] += int(line.split(" ")[0])

total_dict = {}

def calculateTotal(root, subdirs):
    total_dict.setdefault(root, space_dict[root])
    for dir in subdirs:
        calculateTotal(root+dir, subdirs[dir])
        total_dict[root] += total_dict[root+dir]

calculateTotal('/', tree['/'])

result = 0

for dir in total_dict:
    if total_dict[dir] <= 100000:
        result += total_dict[dir]

print(f'\nAnswer: {result}')

print('\nPart Two\n\n')

unused_space = 70000000 - total_dict['/']

tempts = []

for key in total_dict:
    if unused_space + total_dict[key] >= 30000000:
        tempts.append(total_dict[key])

print(f'\nAnswer: {min(tempts)}\n')
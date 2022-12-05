print("\n¡AoC! - Day 05\n")

print('Part One\nAfter the rearrangement procedure completes, what crate ends up on top of each stack?\n')

file = open('input_day_05.txt', 'r')

stacks = {}

for n in range(1, 10):
    stacks[str(n)] = []

for i in range(1, 9):
    for j in range(1, 10):
        letter = file.read(4)[1:2]
        if letter != " ":
            stacks[str(j)].append(letter)

file.read(37)

while True:
    line = file.readline()
    if(len(line) == 0):
        break
    numbers = line.replace("move", "").replace("from", "").replace("to", "").replace("\n", '').split("  ")
    
    for n in range(0, int(numbers[0])):
        stacks[numbers[2]].insert(0, stacks[numbers[1]].pop(0))

result = ''

for stack in stacks:
    result += stacks[stack].pop(0)

file.close()

print(f'\nAnswer: {result}')

print('\nPart Two\nAfter the rearrangement procedure completes, what crate ends up on top of each stack?\n')

file = open('input_day_05.txt', 'r')

stacks = {}

for n in range(1, 10):
    stacks[str(n)] = []

for i in range(1, 9):
    for j in range(1, 10):
        letter = file.read(4)[1:2]
        if letter != " ":
            stacks[str(j)].append(letter)

file.read(37)

while True:
    line = file.readline()
    if(len(line) == 0):
        break
    numbers = line.replace("move", "").replace("from", "").replace("to", "").replace("\n", '').split("  ")

    aux_stack = []
    
    for n in range(0, int(numbers[0])):
        aux_stack.insert(0, stacks[numbers[1]].pop(0))  

    for n in range(0, int(numbers[0])):
        stacks[numbers[2]].insert(0, aux_stack.pop(0))

result = ''

for stack in stacks:
    result += stacks[stack].pop(0)

file.close()

print(f'\nAnswer: {result}\n')
print("\n¡AoC! - Day 10\n")

print('Part One')

file = open('input_day_10.txt', 'r')

cycles = 0
value = 1
result = 0

to_check = [20, 60, 100, 140, 180, 220]

while True:
    line = file.readline()
    if(len(line) == 0):
        break
    line = line.replace('\n', '')

    if line == 'noop':
        cycles += 1
        if cycles in to_check:
            result += (cycles*value)
        continue

    add, x = line.split(' ')
    
    for n in range(0, 2):
        cycles += 1
        if cycles in to_check:
            result += (cycles*value)
    
    value += int(x)

print(f'Answer: {result}\n')

print('Part Two')

file.seek(0)

cycles = 0
value = 1

while True:
    line = file.readline()
    if(len(line) == 0):
        break
    line = line.replace('\n', '')

    if line == 'noop':
        cycles += 1
        if cycles == 41:
            print('')
            cycles = 1
        if cycles in (value, value + 1, value + 2):
            print('#', end='')
        else:
            print('.', end='')
        continue

    add, x = line.split(' ')
    
    for n in range(0, 2):
        cycles += 1
        if cycles == 41:
            print('')
            cycles = 1
        if cycles in (value, value + 1, value + 2):
            print('#', end='')
        else:
            print('.', end='')
    
    value += int(x)
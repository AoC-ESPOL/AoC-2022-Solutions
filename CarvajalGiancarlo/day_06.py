print("\n¡AoC! - Day 06\n")

print('Part One\n\n')

file = open('input_day_06.txt', 'r')

l_list = []

n = 0
while True:
    n += 1
    letter = file.read(1)
    if(len(l_list) == 4):
        l_list.pop(0)
    l_list.append(letter)
    if(len(set(l_list)) == 4):
        break

result = n

file.close()

print(f'\nAnswer: {result}')

print('\nPart Two\n\n')

file = open('input_day_06.txt', 'r')

l_list = []

n = 0
while True:
    n += 1
    letter = file.read(1)
    if(len(l_list) == 14):
        l_list.pop(0)
    l_list.append(letter)
    if(len(set(l_list)) == 14):
        break

result = n

file.close()

print(f'\nAnswer: {result}\n')
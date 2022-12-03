print("\n¡AoC! - Day 03\n")

print('Part One\n\nWhat is the sum of the priorities of those item types?\n')

file = open('input_day_03.txt', 'r')

Lcase = 'abcdefghijklmnopqrstuvwxyz'
Ucase = Lcase.upper()

input_list = list(map(lambda x: x.split("\n"), file.read().split("\n\n")))[0][:-1]

result = 0

for rucksack in input_list:
    for char in rucksack:
        if(char in rucksack[0:int(len(rucksack)/2)] and char in rucksack[int(len(rucksack)/2):]):
            if char.islower():
                result += Lcase.index(char)+1
            else:
                result += Ucase.index(char)+27
            break

print(f'\nAnswer: {result}')

print('\nPart Two\n\nWhat is the sum of the priorities of those item types?\n')

result = 0

for i in range(0, int(len(input_list)/3)):
    sub_list = input_list[i*3:(i*3)+3]
    for char in sub_list[0]:
        if char in sub_list[1] and char in sub_list[2]:
            if char.islower():
                result += Lcase.index(char)+1
            else:
                result += Ucase.index(char)+27
            break

print(f'\nAnswer: {result}\n')
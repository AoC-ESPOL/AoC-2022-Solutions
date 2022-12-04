print("\n¡AoC! - Day 04\n")

print('Part One\n\nIn how many assignment pairs does one range fully contain the other?')

file = open('input_day_04.txt', 'r')

input_list = list(map(lambda x: x.split("\n"), file.read().split("\n\n")))[0][:-1]

result = 0

for pair in input_list:

    p1, p2 = pair.split(",")

    p1L, p1U = p1.split('-')
    p2L, p2U = p2.split('-')

    if(int(p1L) >= int(p2L) and int(p1U) <= int(p2U)) or (int(p1L) <= int(p2L) and int(p1U) >= int(p2U)):
        result += 1

print(f'\nAnswer: {result}')

print('\nPart Two\n\nIn how many assignment pairs do the ranges overlap?')

result = 0

for pair in input_list:

    p1, p2 = pair.split(",")

    p1L, p1U = p1.split('-')
    p2L, p2U = p2.split('-')
    
    if(int(p1L) <= int(p2U) and int(p1L) >= int(p2L)) or (int(p1L) <= int(p2U) and int(p1U) >= int(p2L)):
        result += 1

print(f'\nAnswer: {result}\n')
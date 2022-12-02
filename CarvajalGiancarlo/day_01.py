print("\n¡AoC! - Day 01\n")

print('Part One\n\nFind the Elf carrying the most Calories.\nHow many total Calories is that Elf carrying?')

file = open('input_day_01.txt', 'r')
result = list(map(lambda x: sum([int('0'+i) for i in x]), map(lambda x: x.split("\n"), file.read().split("\n\n"))))
file.close()

print(f'\nAnswer: {max(result)}')

print('\nPart Two\n\nFind the top three Elves carrying the most Calories.\nHow many Calories are those Elves carrying in total?')

set_result = set(result)
top_3 = 0
for n in range(0, 3):
    top_3 += max(set_result)
    set_result.remove(max(set_result))

print(f'\nAnswer: {top_3}\n')
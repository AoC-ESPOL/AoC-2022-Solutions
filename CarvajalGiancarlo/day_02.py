print("\n¡AoC! - Day 02\n")

print('Part One\n\nWhat would your total score be if everything goes exactly according to your strategy guide?\n')

file = open('input_day_02.txt', 'r')

cases = {'A X': 4, 'B Y': 5, 'C Z': 6, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Z': 9, 'C X': 7, 'C Y': 2, '': 0}

input_list = list(map(lambda x: x.split("\n"), file.read().split("\n\n")))[0]
result = list(map(lambda x: cases[x], input_list))

print(f'\nAnswer: {sum(result)}')

print('\nPart Two\n\n Following the Elf\'s instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?')

cases = {'A X': 3, 'B Y': 5, 'C Z': 7, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Z': 9, 'C X': 2, 'C Y': 6, '': 0}

result = list(map(lambda x: cases[x], input_list))

print(f'\nAnswer: {sum(result)}\n')
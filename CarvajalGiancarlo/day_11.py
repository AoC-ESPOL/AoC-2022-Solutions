print("\n¡AoC! - Day 11\n")

print('Part One')

file = open('input_day_11.txt', 'r')

monkeys = {}

def nextLine():
    return file.readline().replace('\n', '')

def getMonkeys():
    for n in range(0, 8):
        nextLine()
        monkeys[n] = {}
        monkeys[n]['inspected'] = 0

        line = nextLine()
        items = line.split(':')
        monkeys[n]['items'] = list(map(lambda x : int(x), items[-1].split(',')))

        line = nextLine()
        operation = line.split(' ')
        monkeys[n]['operation'] =  operation[-2:]

        line = nextLine()
        divisible = line.split(' ')
        monkeys[n]['divisible'] = divisible[-1]

        line = nextLine()
        if_true = line.split(' ')
        monkeys[n]['true'] = if_true[-1]

        line = nextLine()
        if_false = line.split(' ')
        monkeys[n]['false'] = if_false[-1]

        nextLine()

def operate(worry, operator, value):
    if operator == '+':
        return worry + value
    elif operator == '*':
        return worry * value

getMonkeys()
inspections = [0, 0, 0, 0, 0, 0, 0, 0]

for n in range(0, 20):
    for num in monkeys:
        monkey = monkeys[num]
        for i in range(0, len(monkey['items'])):
            monkey['inspected'] += 1
            inspections[num] = monkey['inspected']
            worry = monkey['items'].pop(0)
            if monkey['operation'][1] == 'old':
                worry = (worry ** 2) // 3
            else:
                worry = operate(worry, monkey['operation'][0], int(monkey['operation'][1])) // 3
            if worry % int(monkey['divisible']) == 0:
                monkeys[int(monkey['true'])]['items'].append(worry)
            else:
                monkeys[int(monkey['false'])]['items'].append(worry)

inspections.sort(reverse=True)

print(f'Answer: {inspections[0] * inspections[1]}\n')


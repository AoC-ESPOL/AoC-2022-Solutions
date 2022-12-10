print("\n¡AoC! - Day 09\n")

print('Part One')

file = open('input_day_09.txt', 'r')

tail = head = (0, 0)

tail_visits = set()

def areAdjacent(tail, head):
    return (abs(tail[0] - head[0]) <= 1 and abs(tail[1] - head[1]) <= 1)

def areFar(tail, head):
    return (tail[0] != head[0] and tail[1] != head[1])

def moveTail(tail, head):
    if areAdjacent(tail, head):
        pass

    elif areFar(tail, head):
        if tail[0] < head[0]:
            if tail[1] < head[1]:
                tail = (tail[0] + 1, tail[1] + 1)
            else:
                tail = (tail[0] + 1, tail[1] - 1)
        else:
            if tail[1] < head[1]:
                tail = (tail[0] - 1, tail[1] + 1)
            else:
                tail = (tail[0] - 1, tail[1] - 1)

    else:
        if tail[0] == head[0]:
            if tail[1] < head[1]:
                tail = (tail[0], tail[1] + 1)
            else:
                tail = (tail[0], tail[1] - 1)
        else:
            if tail[0] < head[0]:
                tail = (tail[0] + 1, tail[1])
            else:
                tail = (tail[0] - 1, tail[1])

    return tail

while True:
    line = file.readline()
    if(len(line) == 0):
        break

    line = line.replace('\n', '')

    direction, units = line.split(' ')
    units = int(units)

    for n in range(0, units):
        if direction == 'U':
            head = (head[0], head[1] + 1)
        elif direction == 'R':
            head = (head[0] + 1, head[1])
        elif direction == 'D':
            head = (head[0], head[1] - 1)
        elif direction == 'L':
            head = (head[0] - 1, head[1])
        
        tail = moveTail(tail, head)
        tail_visits.add(tail)

print(f'Answer: {len(tail_visits)}\n')

print('Part Two')

file.seek(0)

rope = list(((0, 0), )*10)

tail_visits = set()

while True:
    line = file.readline()
    if(len(line) == 0):
        break

    line = line.replace('\n', '')

    direction, units = line.split(' ')
    units = int(units)

    for n in range(0, units):
        if direction == 'U':
            rope[9] = (rope[9][0], rope[9][1] + 1)
        elif direction == 'R':
            rope[9] = (rope[9][0] + 1, rope[9][1])
        elif direction == 'D':
            rope[9] = (rope[9][0], rope[9][1] - 1)
        elif direction == 'L':
            rope[9] = (rope[9][0] - 1, rope[9][1])
        
        for i in reversed(range(0, 9)):
            rope[i] = moveTail(rope[i], rope[i+1])

        tail_visits.add(rope[0])

print(f'Answer: {len(tail_visits)}\n')
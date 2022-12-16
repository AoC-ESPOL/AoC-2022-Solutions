print("\n¡AoC! - Day 12\n")

print('Part One')

file = open('input_day_12.txt', 'r')

matrix = []

while True:
    line = file.readline()
    if(len(line) == 0):
        break
    line = line.replace('\n', '')
    row = []
    for c in line:
        row.append(c)
    matrix.append(row)

rows = len(matrix)
columns = len(matrix[0])

def getPositionOf(letter):

    for i in range(0, rows):
        for j in range(0, columns):
            if matrix[i][j] == letter:
                return (i, j)

start = getPositionOf('S')
destiny = getPositionOf('E')

levels  = 'abcdefghijklmnopqrstuvwxyzES'

def getPosibleMovements(position):
    movements = []
    i, j = position

    UP = i - 1
    DOWN = i + 1
    LEFT = j - 1
    RIGHT = j + 1

    level = levels.index(matrix[i][j])

    if UP >= 0:
        if (levels.index(matrix[UP][j]) - level) <= 1:
            movements.append((UP, j))

    if DOWN <= rows - 1:
        if (levels.index(matrix[DOWN][j]) - level) <= 1:
            movements.append((DOWN, j))

    if LEFT >= 0:
        if (levels.index(matrix[i][LEFT]) - level) <= 1:
            movements.append((i, LEFT))

    if RIGHT <= columns - 1:
        if (levels.index(matrix[i][RIGHT]) - level) <= 1:
            movements.append((i, RIGHT))

    return movements

paths = {start:0}
queue = [start]

def calculatePaths(paths, queue):
    while queue:
        position = queue.pop(0)
        cost = paths[position]
        for movement in getPosibleMovements(position):
            if movement not in paths:
                paths.setdefault(movement, cost+1)
                queue.append(movement)
            elif cost + 1 < paths[movement]:
                paths[movement] = cost + 1
                queue.append(movement)

calculatePaths(paths, queue)

print(f'Answer: {paths[destiny]}\n')

print('Part Two')

starting_points = set()

def getNewPositionOf(letter):
    for i in range(0, rows):
        for j in range(0, columns):
            if matrix[i][j] == letter and (i, j) not in starting_points:
                return (i, j)
    return None

while True:
    start = getNewPositionOf('a')
    if not start:
        break
    starting_points.add(start)

paths_paths = []

for start in starting_points:
    paths = {start:0}
    queue = [start]
    calculatePaths(paths, queue)
    paths_paths.append(paths)

print(f'Answer: {min(list(map(lambda x: x[destiny], filter(lambda x: destiny in x, paths_paths))))}\n')
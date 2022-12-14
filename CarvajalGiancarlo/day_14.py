print("\n¡AoC! - Day 14\n")

print('Part One')

file = open('input_day_14.txt', 'r')

ocuppied_original = set()

while True:
    line = file.readline()
    if(len(line) == 0):
        break
    line = line.replace('\n', '')
    guides = line.split(' -> ')

    for n in range(0, len(guides) - 1):
        currentX, currentY = map(lambda x: int(x), guides[n].split(','))
        destinyX, destinyY = map(lambda x: int(x), guides[n+1].split(','))

        ocuppied_original.add((currentX, currentY))

        while currentX != destinyX:
            currentX += 1 if currentX < destinyX else -1
            ocuppied_original.add((currentX, currentY))

        while currentY != destinyY:
            currentY += 1 if currentY < destinyY else -1
            ocuppied_original.add((currentX, currentY))

limitY = max(list(map(lambda x: x[1], ocuppied_original)))

result = 0
occupied_copyOne = ocuppied_original.copy()

while True:
    sand = (500, 0)
    void = False

    while True:
        x, y = sand

        if y == limitY:
            void = True
            break

        if (x, y+1) not in occupied_copyOne:
            sand = (x, y+1)
            continue
        if (x-1, y+1) not in occupied_copyOne:
            sand = (x-1, y+1)
            continue
        if (x+1, y+1) not in occupied_copyOne:
            sand = (x+1, y+1)
            continue
        break

    if void:
        break
    occupied_copyOne.add(sand)
    result += 1

print(f'Answer: {result}\n')

print('Part Two')

floorY = 2 + limitY

result = 0
occupied_copyTwo = ocuppied_original.copy()

while True:
    sand = (500, 0)
    void = False

    while True:
        x, y = sand

        if y == floorY - 1:
            break

        if (x, y+1) not in occupied_copyTwo:
            sand = (x, y+1)
            continue
        if (x-1, y+1) not in occupied_copyTwo:
            sand = (x-1, y+1)
            continue
        if (x+1, y+1) not in occupied_copyTwo:
            sand = (x+1, y+1)
            continue
        break

    occupied_copyTwo.add(sand)
    result += 1
    if sand == (500, 0):
        break

print(f'Answer: {result}\n')
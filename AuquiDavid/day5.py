# David Auqui
# DAY 5

# -- Part One --
print("-- Part One --")
file = open("input.txt")
lines = file.readlines()
file.close()

listIndex = []
counter = 0
line9 = lines[8]
line9 = line9.replace("\n", "")
for i in line9:
    if i != " ":
        listIndex.append(counter)
    counter += 1

stacks = []
stacks2 = []

counter = 0
for i in listIndex:
    stacks.append([])
    stacks2.append([])
    for line in lines[0:8]:
        line = line.replace("\n", "")
        if line[i] != ' ':
            stacks[counter].append(line[i])
            stacks2[counter].append(line[i])
    counter += 1


for line in lines[10:]:
    line = line.replace("\n", "")
    line = line.split(" ")
    listCopy = stacks[int(line[5]) - 1]
    listCopy.reverse()
    listA = []
    i = 0
    while i < int(line[1]):
        listCopy.append(stacks[int(line[3]) - 1][i])
        listA.append(stacks[int(line[3]) - 1][i])
        i += 1
    for i in listA:
        stacks[int(line[3]) - 1].remove(i)
    listCopy.reverse()

    stacks[int(line[5]) - 1] = listCopy

for i in stacks:
    print(i[0])

# -- Part Two --
print("\n-- Part Two --")
for line in lines[10:]:
    line = line.replace("\n", "")
    line = line.split(" ")

    listCopy = stacks2[int(line[5]) - 1]#receptor
    listCopy.reverse()
    listA = []

    listB = []

    i = 0
    while i < int(line[1]):
        listB.append(stacks2[int(line[3]) - 1][i])
        i += 1
    listB.reverse()
    for i in listB:
        listCopy.append(i)
        listA.append(i)
    listB.reverse()
    for i in listB:
        stacks2[int(line[3]) - 1].remove(i)

    listCopy.reverse()

    stacks2[int(line[5]) - 1] = listCopy

for i in stacks2:
    print(i[0])

pairs = []

#-- Part One --
counter = 0
file = open('input.txt')
lines=file.readlines()

for line in lines:
    lock=0
    line = line.replace("\n","")
    line = line.split(",")
    one = line[0].split("-")
    two = line[1].split("-")
    if int(one[0]) >= int(two[0]):
        if int(one[1]) <=int(two[1]):
            counter += 1
            lock = 1
    if int(two[0]) >= int(one[0]):
        if int(two[1]) <=int(one[1]):
            if lock == 0:
                counter += 1

file.close()
print("-- Part One --")
print(counter)

#-- Part Two --
counter = 0
for line in lines:
    lock=0
    line = line.replace("\n","")
    line = line.split(",")
    one = line[0].split("-")
    two = line[1].split("-")
    oneList = range(int(one[0]),(int(one[1])+1))
    twoList = range(int(two[0]),(int(two[1])+1))
    oneList = list(oneList)
    twoList = list(twoList)
    lock = 0

    for i in oneList:
        if i in twoList:
            if lock == 0:
                counter+=1
                lock = 1

print("\n-- Part Two --")
print(counter)
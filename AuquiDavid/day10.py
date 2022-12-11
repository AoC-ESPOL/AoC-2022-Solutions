#DAY 10
#-- PART ONE --

list = [20,60,100,140,180,220]
scores = []

file = open("input.txt")
lines = file.readlines()
file.close()

cycle = 1
x=1
for line in lines:
    line = line.replace("\n","")
    line = line.split(" ")
    if line[0] == "noop":
        cycle+=1
        if cycle in list:
            scores.append((x * cycle))

    if line[0] == "addx":
        for i in range(2):
            if i == 0:
                cycle += 1
                if cycle in list:
                    scores.append((x * cycle))
            if i == 1:
                cycle += 1
                x+=int(line[1])
                if cycle in list:
                    scores.append((x*cycle))

total = 0
for i in scores:
    total+=i
print("-- PART ONE --")
print(total)

#-- PARTE TWO --
print("\n-- PART TWO --")
cycles=[[""],[""],[""],[""],[""],[""],[""]]

cycle = 1
x=1

cx=0
cy=1
for line in lines:
    line = line.replace("\n","")
    line = line.split(" ")
    if line[0] == "noop":
        cycle+=1

        if cy <= 40:
            if cy == x or cy == (x+1) or cy == (x+2):
                cycles[cx][0] = cycles[cx][0]+"#"
            else:
                cycles[cx][0] = cycles[cx][0]+"."
            cy+=1
        if cy == 41:
            cy=0
            cx+=1
            if cy == x or cy == (x + 1) or cy == (x + 2):
                cycles[cx][0] = cycles[cx][0] + "#"
            else:
                cycles[cx][0] = cycles[cx][0] + "."
            cy+=1


    if line[0] == "addx":
        for i in range(2):
            if i == 0:
                cycle += 1

                if cy <= 40:
                    if cy == x or cy == (x + 1) or cy == (x + 2):
                        cycles[cx][0] = cycles[cx][0] + "#"
                    else:
                        cycles[cx][0] = cycles[cx][0] + "."
                    cy += 1
                if cy == 41:
                    cy = 0
                    cx += 1
                    if cy == x or cy == (x + 1) or cy == (x + 2):
                        cycles[cx][0] = cycles[cx][0] + "#"
                    else:
                        cycles[cx][0] = cycles[cx][0] + "."
                    cy += 1


            if i == 1:
                cycle += 1

                if cy <= 40:
                    if cy == x or cy == (x + 1) or cy == (x + 2):
                        cycles[cx][0] = cycles[cx][0] + "#"
                    else:
                        cycles[cx][0] = cycles[cx][0] + "."
                    cy += 1
                if cy == 41:
                    cy = 0
                    cx += 1
                    if cy == x or cy == (x + 1) or cy == (x + 2):
                        cycles[cx][0] = cycles[cx][0] + "#"
                    else:
                        cycles[cx][0] = cycles[cx][0] + "."
                    cy += 1

                x+=int(line[1])



print()
print(cycles[0][0])
counter = 1
for i in cycles[1:]:
    cycles[counter][0] = cycles[counter][0][1:]
    print(cycles[counter][0])
    counter+=1


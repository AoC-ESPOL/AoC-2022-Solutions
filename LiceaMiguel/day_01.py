calories = []
lines = [line for line in open('day1.in')]
cont = 0
for line in lines:
    line = line.strip()
    if line == '':
        calories.append(cont)
        cont = 0
    else:
        cont += int(line)

calories = sorted(calories)
p1 = calories[-1]
p2 = calories[-1]+calories[-2]+calories[-3]
print(p1)
print(p2)
with open("day_14.txt") as file:
    list1 = []
    max1 = 0
    for line in file:
        x = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
        for (x1, y1), (x2, y2) in zip(x, x[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    list1.append(x + y * 1j)
                    max1 = max(max1, y + 1)

c1 = set(list1)
#Parte1
count1 = 0
while True:
    s = 500
    while True:
        if s.imag >= max1:
            print(count1)
            exit()
        if s + 1j not in c1:
            s += 1j
            continue
        if s + 1j - 1 not in c1:
            s += 1j - 1
            continue
        if s + 1j + 1 not in c1:
            s += 1j + 1
            continue
        c1.add(s)
        count1 += 1
        break

#Parte2
count2 = 0
while 500 not in c1:
    s = 500
    while True:
        if s.imag >= max1:
            break
        if s + 1j not in c1:
            s += 1j
            continue
        if s + 1j - 1 not in c1:
            s += 1j - 1
            continue
        if s + 1j + 1 not in c1:
            s += 1j + 1
            continue
        break
    c1.add(s)
    count2 += 1
print(count2)
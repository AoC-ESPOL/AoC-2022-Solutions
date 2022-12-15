with open("day_15.txt") as file:
    contenido = file.read().split("\n")

import tqdm

data = list()
target_row = 2000000
ranges = list()
for x in contenido:
    info0, info1 = x.strip().split(":")
    sensor = info0.strip().split(",")
    baliza = info1.strip().split(",")
    s_x = int(sensor[0][sensor[0].index("=")+1:])
    s_y = int(sensor[1][sensor[1].index("=")+1:])
    b_x = int(baliza[0][baliza[0].index("=")+1:])
    b_y = int(baliza[1][baliza[1].index("=")+1:])
    data.append((s_x, s_y, b_x, b_y))
    L1 = abs(s_x - b_x) + abs(s_y - b_y)
    if (s_y - L1) <= target_row <= (s_y + L1):
        width = L1 - abs(s_y - target_row)
        ranges.append((s_x - width, s_x + width, ))
ranges.sort()
count = 0
head = ranges[0][0]
for x, y in ranges:
	if head < x:
		count += y - x +1
		head = y
	else:
		if head < y:
			count += y - head
			head = y
print(count)

# part 2
xx = set()
M = 4000000
def dist(s_x, s_y, b_x, b_y):
    return abs(s_x - b_x) + abs(s_y - b_y)
for s_x, s_y, b_x, b_y in data:
    d = dist(s_x, s_y, b_x, b_y) + 1
    for x in range(s_x - d, s_x + d + 1):
        y = s_y + (d - abs(s_x - x))
        if (0 <= x <= M) and (0 <= y <= M):
            xx.add((x, y))
        y = s_y - (d - abs(s_x - x))
        if (0 <= x <= M) and (0 <= y <= M):
            xx.add((x, y))
for x, y in tqdm.tqdm(xx):
    if all(dist(sx, sy, x, y) > dist(sx, sy, bx, by) for sx, sy, bx, by in data):
        print(x, y)
        break

from collections import defaultdict

with open("day_07.txt") as file:
    contenido = file.read().strip()
sizes = defaultdict(int)
path = []
for line in contenido.split("\n"):
    if line.startswith("$ cd"):
        d = line.split()[2]
        if d == "/":
            path.append("/")
        elif d == "..":
            ultimo = path.pop()
        else:
            path.append(f"{path[-1]}{'/' if path[-1] != '/' else ''}{d}")
    if line[0].isnumeric():
        for p in path:
            sizes[p] += int(line.split()[0])

print(sizes)
parte_1 = 0
for x in sizes.values():
    if (x <= 100_000):
        parte_1 += x

parte_2 = []
for x in sizes.values():
    if (x >= 30_000_000 - (70_000_000 - sizes['/'])):
        parte_2.append(x)

print(parte_1)
print(min(parte_2))

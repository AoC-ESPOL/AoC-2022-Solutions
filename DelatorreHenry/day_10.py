with open("day_10.txt") as file:
    contenido = file.read().splitlines()

n_cycle = 1
valor = 1
total_sum = 0
for line in contenido:
    n_cycle += 1
    if "addx" in line:
        total_sum += (n_cycle * valor if n_cycle in [20, 60, 100, 140, 180, 220] else 0)
        n_cycle += 1
        valor += int(line.split()[1])
    total_sum += (n_cycle * valor if n_cycle in [20, 60, 100, 140, 180, 220] else 0)
print(total_sum)

draw = []
n_cycle = 0
positions = [0, 1, 2]
for line in contenido:
    for x in range(2 if "addx" in line else 1):
        draw.append('#' if n_cycle in positions else ' ')
        n_cycle = (n_cycle + 1) % 40
        positions = [x + int(line.split()[1]) for x in positions] if x == 1 else positions
for n in range(6):
    print(''.join(draw[n*40:(n+1)*40]))

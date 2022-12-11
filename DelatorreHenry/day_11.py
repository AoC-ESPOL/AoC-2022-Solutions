with open("day_11.txt") as file:
    contenido = file.read().strip()

import math
from copy import deepcopy
from collections import defaultdict

lines = [x for x in contenido.split('\n')]

monkeys = []
operations = []
condition = []
v = []
f = []

for monkey in contenido.split('\n\n'):
    id_, items, op, test, true, false = monkey.split('\n')
    monkeys.append([int(i) for i in items.split(':')[1].split(',')])
    words = op.split()
    op = ''.join(words[-3:])
    operations.append(lambda old,op=op:eval(op))
    condition.append(int(test.split()[-1]))
    v.append(int(true.split()[-1]))
    f.append(int(false.split()[-1]))
ini = deepcopy(monkeys)
lcm = 1
for x in condition:
    lcm = (lcm*x)
ronda = int(input("Ingrese las rondas: "))
info_monkeys = [0 for _ in range(len(monkeys))]
monkeys = deepcopy(ini)
for t in range(ronda):
    for i in range(len(monkeys)):
        for item in monkeys[i]:
            info_monkeys[i] += 1
            item = operations[i](item)
            if ronda == 10000:
                item %= lcm
            if ronda == 20:
                item = (item // 3)
            if item % condition[i] == 0:
                monkeys[v[i]].append(item)
            else:
                monkeys[f[i]].append(item)
        monkeys[i] = []
major = sorted(info_monkeys)[-1]
second_major = sorted(info_monkeys)[-2]
print(major*second_major)

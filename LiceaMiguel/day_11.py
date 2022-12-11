from copy import deepcopy
data = open('day11.in').read()

class Monk:
    def __init__(self, items, op, mod, true_target, false_target):
        self.items = items
        self.op = op
        self.mod = mod
        self.true_target = true_target
        self.false_target = false_target

monks = []
for simio in data.split("\n\n"):
    sim, item, op, mod, true_target, false_target = simio.split("\n")
    op = "".join(op.split()[-3:])
    monk = Monk(items=[int(c) for c in item.split(":")[1].split(",")],
        op = lambda old, op=op:eval(op),
        mod = int(mod.split()[-1]),
        true_target = int(true_target.split()[-1]),
        false_target = int(false_target.split()[-1]))
    monks.append(monk)

mincm = 1
for x in [monk.mod for monk in monks]:
    mincm *= (mincm*x)

init = deepcopy(monks)
values = [0]*len(monks)

for _ in range(20):
    for i,monk in enumerate(monks):
        for item in monk.items:
            values[i]+=1
            item = (monk.op(item)) // 3
            if item % monk.mod == 0:
                monks[monk.true_target].items.append(item)
            else:
                monks[monk.false_target].items.append(item)
        monk.items = []
values.sort()
print(values[-1] * values[-2])

monks = init
values = [0]*len(monks)
for _ in range(10000):
    for i, monk in enumerate(monks):
        for item in monk.items:
            values[i]+=1
            item = (monk.op(item)) % mincm
            if item % monk.mod == 0:
                monks[monk.true_target].items.append(item)
            else:
                monks[monk.false_target].items.append(item)
        monk.items = []
values.sort()
print(values[-1] * values[-2])

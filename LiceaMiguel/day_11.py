from copy import deepcopy
data = open('day11.in').read()

# class Monk():

#     def __init__(self, items, op, mod, true_target, false_target):
#         self.items = items
#         self.op = op
#         self.mod = mod
#         self.true_target = true_target
#         self.false_target = false_target
# monks = []
# items = []
# operations = []
# mods = []
# true_targets = []
# false_targets = []
# for simio in data.split("\n\n"):
#     sim, item, op, mod, true_target, false_target = simio.split("\n")
#     values = [int(c) for c in item.split(":")[1].split(",")]
#     items.append(values)
#     op = "".join(op.split()[-3:])
#     operations.append(lambda old, op=op:eval(op))
#     mods.append(int(mod.split()[-1]))
#     true_targets.append(int(true_target.split()[-1]))
#     false_targets.append(int(false_target.split()[-1]))

items = []
operations = []
mods = []
true_targets = []
false_targets = []
for simio in data.split("\n\n"):
    sim, item, op, mod, true_target, false_target = simio.split("\n")
    values = [int(c) for c in item.split(":")[1].split(",")]
    items.append(values)
    op = "".join(op.split()[-3:])
    operations.append(lambda old, op=op:eval(op))
    mods.append(int(mod.split()[-1]))
    true_targets.append(int(true_target.split()[-1]))
    false_targets.append(int(false_target.split()[-1]))

init = deepcopy(items)

values = [0 for _ in range(len(items))]
items_copy = deepcopy(init)

for _ in range(20):
    for i in range(len(items_copy)):
        for item in items_copy[i]:
            values[i]+=1
            item = (operations[i](item)) // 3
            if item % mods[i] ==0:
                items_copy[true_targets[i]].append(item)
            else:
                items_copy[false_targets[i]].append(item)
        items_copy[i] = []
values.sort()
print(values[-1] * values[-2])

mincm = 1
for i in mods:
    mincm *= (mincm*i)

items_copy = deepcopy(init)
values = [0 for _ in range(len(items))]
for _ in range(10000):
    for i in range(len(items_copy)):
        for item in items_copy[i]:
            values[i]+=1
            item = (operations[i](item)) % mincm
            if item % mods[i] ==0:
                items_copy[true_targets[i]].append(item)
            else:
                items_copy[false_targets[i]].append(item)
        items_copy[i] = []
values.sort()
print(values[-1] * values[-2])

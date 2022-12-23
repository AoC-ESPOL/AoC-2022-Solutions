from collections import Counter
data = open('day23.in').read()

adjacent = [
    (-1, 0),
    (-1, 1),
    (-1, -1),
    (1, 0),
    (1, 1),
    (1, -1),
    (0, -1),
    (0, 1),
]


def calculate_adjacent_pos(i, j):
    adjacent_movs = [(i + x[0], j + x[1]) for x in adjacent]
    return adjacent_movs


def calculate_directions_pos(i, j, directions_ind):
    direction_movs = [(i + x[0], j + x[1]) for x in directions_ind]
    return direction_movs


def s1():
    directions = [
        [(-1, 0), (-1, 1), (-1, -1)],
        [(1, 0), (1, 1), (1, -1)],
        [(0, -1), (1, -1), (-1, -1)],
        [(0, 1), (1, 1), (-1, 1)],
    ]

    cont = 0
    e = set()
    lines = data.splitlines()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                e.add((i, j))

    while True:
        cont += 1
        movements = dict()
        for i, j in e:
            adjacent_movs = calculate_adjacent_pos(i, j)
            act_belongs = list(map(lambda p: p not in e, adjacent_movs))
            if all(act_belongs):
                continue
            for x in directions:
                maybe_new_directions = calculate_directions_pos(i, j, x)
                act_belongs = list(
                    map(lambda p: p not in e, maybe_new_directions))
                if all(act_belongs):
                    movements[(i, j)] = (i + x[0][0], j + x[0][1])
                    break
        if not movements:
            break
        counter = Counter(movements.values())
        for item in movements.items():
            actual_item, new_item = item
            if not counter[new_item] > 1:
                e.remove(actual_item)
                e.add(new_item)

        if cont == 10:
            break
        directions = directions[1:] + [directions[0]]

    i_values = [x[0] for x in e]
    i_diff = (max(i_values)- 1) - min(i_values)
    j_values = [x[1] for x in e]
    j_diff = (max(j_values)- 1) - min(j_values)
    return i_diff * j_diff - len(e)

print(s1())


def s2():

    directions = [
        [(-1, 0), (-1, 1), (-1, -1)],
        [(1, 0), (1, 1), (1, -1)],
        [(0, -1), (1, -1), (-1, -1)],
        [(0, 1), (1, 1), (-1, 1)],
    ]

    cont = 0
    e = set()
    lines = data.splitlines()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                e.add((i, j))

    while True:
        cont += 1
        movements = dict()
        for i, j in e:
            adjacent_movs = calculate_adjacent_pos(i, j)
            act_belongs = list(map(lambda p: p not in e, adjacent_movs))
            if all(act_belongs):
                continue
            for x in directions:
                maybe_new_directions = calculate_directions_pos(i, j, x)
                act_belongs = list(
                    map(lambda p: p not in e, maybe_new_directions))
                if all(act_belongs):
                    movements[(i, j)] = (i + x[0][0], j + x[0][1])
                    break
        if not movements:
            break
        counter = Counter(movements.values())
        for item in movements.items():
            actual_item, new_item = item
            if not counter[new_item] > 1:
                e.remove(actual_item)
                e.add(new_item)
        directions = directions[1:] + [directions[0]]
    return cont

print(s2())
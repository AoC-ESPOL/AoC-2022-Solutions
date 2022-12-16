with open("day_16.txt") as file:
    contenido = file.read().split("\n")
    pres = 0
    moves = 0
    valves = dict()
    for line in contenido:
        valve = line[5:8].strip()
        rate = int(line[line.index("=")+1:line.index(";")])
        others_valves = line.split()[9:]
        valves[valve] = dict()
        valves[valve]["flow"] = 0
        valves[valve]["flow"] += rate
        valves[valve]["tunnels"] = [x[:2] for x in others_valves]
        valves[valve]["paths"] = {}

print(valves)
keys = sorted([x for x in list(valves.keys()) if valves[x]['flow'] != 0])

def bfs(frontier, end):
    depth = 1
    while True:
        next_frontier = set()
        for x in frontier:
            if x == end:
                return depth
            for y in valves[x]['tunnels']:
                next_frontier.add(y)
        frontier = next_frontier
        depth += 1

for k in keys + ['AA']:
    for k2 in keys:
        if k2 != k:
            valves[k]['paths'][k2] = bfs(valves[k]['tunnels'], k2)

def part1():
    best = 0
    def search(opened, flowed, current_room, depth_to_go):
        nonlocal best
        if flowed > best:
            best = flowed
        if depth_to_go <= 0:
            return
        if current_room not in opened:
            search(opened.union([current_room]), flowed + valves[current_room]['flow'] * depth_to_go, current_room, depth_to_go - 1)
        else:
            for k in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
                search(opened, flowed, k, depth_to_go - valves[current_room]['paths'][k])
    search(set(['AA']), 0, 'AA', 29)
    print(best)
part1()

def part2():
    best = 0
    def search(opened, flowed, current_room, depth_to_go, elephants_turn):
        nonlocal best
        if flowed > best:
            best = flowed
        if depth_to_go <= 0:
            return
        if current_room not in opened:
            search(opened.union([current_room]), flowed + valves[current_room]['flow'] * depth_to_go, current_room, depth_to_go - 1, elephants_turn)
            if not elephants_turn:
                search(set([current_room]).union(opened), flowed + valves[current_room]['flow'] * depth_to_go, 'AA', 25, True)
        else:
            for k in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
                search(opened, flowed, k, depth_to_go - valves[current_room]['paths'][k], elephants_turn)
    search(set(['AA']), 0, 'AA', 25, False)
    print(best)
part2()
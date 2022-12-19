from collections import deque
lines = [line.strip() for line in open('day19.in').read().split("\n")]

class Blueprint:
    def __init__(self, id, ore_cost, clay_cost, obsidian_cost, geode_cost):
        self.id = id
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obsidian_cost = obsidian_cost
        self.geode_cost = geode_cost

def parse_blueprint_line(line):
    parts = line.split(':')
    id = int(parts[0].split(' ')[1])
    ore_cost, clay_cost, obsidian_cost, geode_cost = 0, 0, {"ore":0,"clay":0}, {"ore":0,"obsidian":0}
    costs = parts[1].split(' ')
    ore_cost = int(costs[5])
    clay_cost = int(costs[11])
    obsidian_cost["ore"] = int(costs[17])
    obsidian_cost["clay"] = int(costs[20])
    geode_cost["ore"] = int(costs[26])
    geode_cost["obsidian"] = int(costs[29])
    blueprint = Blueprint(id, ore_cost, clay_cost, obsidian_cost, geode_cost)
    return id, blueprint

blueprints = []
for line in lines:
    blueprints.append(parse_blueprint_line(line))

def find_best_geodes(blueprint):
    visited = tuple()
    time_left = 24
    actual = tuple([0,0,0,0,1,0,0,0,time_left])
    max = 0
    explore_queue = deque()
    explore_queue.append(actual)
    while explore_queue:
        actual = explore_queue.popleft()
        geodes=actual[3]
        best = geodes if geodes > best else best
        if time_left == 0: continue
        max_ore = 0
        ores_cost = max([blueprint.ore_cost,
            blueprint.clay_cost, blueprint.obsidian_cost["ore"],
            blueprint.geode_cost["ore"]])
        
        time_left_a = list(actual)[-1]
        
        if actual[4]>=ores_cost:
            actual[4] = ores_cost
        if actual[5]>=blueprint.obsidian_cost["clay"]:
            actual[5] = blueprint.obsidian_cost["clay"]
        if actual[6]>=blueprint.geode_cost["obsidian"]:
            actual[6] = blueprint.geode_cost["obsidian"]
        if actual[0] >= time_left_a*ores_cost-actual[4]*(time_left_a-1):
            actual[0] = time_left_a*ores_cost-actual[4]*(time_left_a-1)
        if actual[1]>=time_left_a*blueprint.obsidian_cost["clay"]-actual[5]*(time_left_a-1):
            actual[1] = time_left_a*blueprint.obsidian_cost["clay"]-actual[6]*(time_left_a-1)
        if actual[2]>=time_left_a*blueprint.geode_cost["obsidian"]-actual[7]*(time_left_a-1):
            actual[2] = time_left_a*blueprint.geode_cost["obsidian"]-actual[7]*(time_left_a-1)

        if actual in visited: continue
        visited.add(actual)

        explore_queue.append(tuple([actual[0]+actual[4], actual[1]+actual[5], actual[3]+actual[6],actual[3]+actual[7], actual[4], actual[5], actual[6], actual[7], time_left_a -1]))
        if actual[0]>=blueprint.ore_cost:
            explore_queue.append((actual[0]-blueprint.ore_cost+actual[4], actual[1]+actual[5], actual[2]+actual[6], actual[3]+actual[7], actual[4]+1,actual[5],actual[6],actual[7],time_left_a-1))
        if actual[0]>=blueprint.clay_cost:
            explore_queue.append((actual[0]-blueprint.clay_cost+actual[4], actual[2]+actual[5], actual[2]+actual[6], actual[3]+actual[7], actual[4],actual[5]+1,actual[6],actual[7],time_left_a-1))
        if actual[0]>=blueprint.obsidian_cost['ore'] and actual[1]>=blueprint.obsidian_cost['clay']:
            explore_queue.append((actual[0]-blueprint.obsidian_cost['ore']+actual[4], actual[1]-blueprint.obsidian_cost['clay']+actual[5], actual[2]+actual[6], actual[3]+actual[7], actual[4],actual[5],actual[6]+1,actual[7],time_left_a-1))
        if actual[0]>=blueprint.geode_cost['ore'] and actual[2]>=blueprint.geode_cost['obsidian']:
            explore_queue.append((actual[0]-blueprint.geode_cost['ore']+actual[4], actual[1]+actual[5], actual[2]-blueprint.geode_cost['obsidian']+actual[6], actual[3]+actual[7], actual[4],actual[5],actual[6],actual[7]+1,time_left_a-1))
    return max

max1, max2 = 0,1
for index,blue in enumerate(blueprints):
    max1 += blue.id*find_best_geodes(blue)

print(max1)

for blue in blueprints[:3]:
    max2 *= find_best_geodes(blue)

print(max2)
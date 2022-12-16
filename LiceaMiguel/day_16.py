import re
from collections import defaultdict

def parse_values():
    valves = {}
    flow_rates = {}
    lines = open('day16.in').read().strip().splitlines()
    for line in lines:
        valve_name = line.split()[1]
        rate = int(line.split()[4].split("=")[1].strip(";"))
        tunnels = [x.strip(",").strip() for x in line.split("to")[1].split()[1:]]
        valves[valve_name] = tunnels
        flow_rates[valve_name] = rate
    return valves, flow_rates

valves, flow_rates = parse_values()

have_rates = {}
for key in flow_rates.keys():
    if flow_rates[key]!=0:
        have_rates[key] = len(have_rates)
com = (2 ** len(have_rates))

memo = defaultdict(lambda: [[0.1]*com ]*31)

def walk(valve, time_left, com):
    if time_left == 0:
        return 0
    memoized_val = memo[valve][time_left][com]
    if  memoized_val == 0.1:
        tunnels_max = []
        for tunnel in valves[valve]:
            tunnels_max.append(walk(tunnel, time_left - 1, com))
        tunnels_max = max(tunnels_max)
        if (1 << have_rates[valve]) & com:
            ac_press = flow_rates[valve] * (time_left - 1)
            paths_press = walk(valve, time_left - 1, com - (1 << have_rates[valve]))
            pressures = [tunnels_max, ac_press + paths_press]
        memo[valve][time_left][com] = max(pressures)
    return memo[valve][time_left][com]

print(walk("AA",30, com-1))

def walk_s2():
    s2 = []
    for com_i in range(com):
        s_press = walk("AA", 26, com - 1 - com_i) + walk("AA", 26, com_i)
        s2.append(s_press)
    return max(s2)

print(walk_s2())
from collections import defaultdict
lines = [x for x in open('day7.in').read().strip().split("\n")]

s1 = 0
s2 = 10000000000000000000000000000000
def create_routes():
    routes = defaultdict(int)
    actual_path = []
    for line in [l.strip() for l in lines]:
        line = line.split()
        command = line[1]
        arg = line[2] if len(line)>2 else 0
        if command == 'cd':
            if arg == '..':
                actual_path.pop()
            else:
                actual_path.append(arg)
        elif command !='ls' and line[0]!='dir':
            for i in range(1, len(actual_path)+1):
                routes['/'.join(actual_path[:i])] += int(line[0])
    return [routes,routes['/']-40000000]

r,f = create_routes()
for arr in r.items():
    if arr[1] <= 100000:
        s1 += arr[1]
    if arr[1]>=f:
        s2 = min(arr[1], s2)
print(s1)
print(s2)
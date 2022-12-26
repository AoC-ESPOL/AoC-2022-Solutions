with open("day_23.txt") as file:
    contenido = file.read().split("\n")
from collections import defaultdict
elfos = set()
lineas = contenido
for r,row in enumerate(lineas):
    for c,ch in enumerate(row):
        if ch=='#':
            elfos.add((r,c))

def show(E):
    r1 = min(r for (r,c) in E)
    r2 = max(r for (r,c) in E)
    c1 = min(c for (r,c) in E)
    c2 = max(c for (r,c) in E)
    for r in range(r1,r2+1):
        row = ''
        for c in range(c1,c2+1):
            row += ('#' if (r,c) in E else '.')
        print(row)
    print('='*80)

dir_list = ['N', 'E', 'S', 'W']
for t in range(10000):
    any_moved = False
    P = defaultdict(list)
    for (r,c) in elfos:
        has_nbr = False
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if (dr!=0 or dc!=0) and (r+dr, c+dc) in elfos:
                    has_nbr = True
        if not has_nbr:
            continue
        moved = False
        for dir_ in dir_list:
            if dir_=='N' and (not moved) and (r-1,c) not in elfos and (r-1,c-1) not in elfos and (r-1,c+1) not in elfos:
                P[(r-1,c)].append((r,c))
                moved = True
            elif dir_=='E' and (not moved) and (r+1,c) not in elfos and (r+1, c-1) not in elfos and (r+1, c+1) not in elfos:
                P[(r+1,c)].append((r,c))
                moved = True
            elif dir_=='S' and (not moved) and (r, c-1) not in elfos and (r-1,c-1) not in elfos and (r+1,c-1) not in elfos:
                P[(r,c-1)].append((r,c))
                moved = True
            elif dir_=='W' and (not moved) and (r, c+1) not in elfos and (r-1,c+1) not in elfos and (r+1,c+1) not in elfos:
                P[(r,c+1)].append((r,c))
                moved = True
    dir_list = dir_list[1:]+[dir_list[0]]
    for k,vs in P.items():
        if len(vs) == 1:
            any_moved = True
            elfos.discard(vs[0])
            elfos.add(k)
    if not any_moved:
        print(t+1)
        break
    if t==9:
        r1 = min(r for (r,c) in elfos)
        r2 = max(r for (r,c) in elfos)
        c1 = min(c for (r,c) in elfos)
        c2 = max(c for (r,c) in elfos)
        ans = 0
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                if (r,c) not in elfos:
                    ans += 1
        print(ans)
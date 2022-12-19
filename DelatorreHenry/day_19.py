from parse import *
from collections import deque
robots = []
with open("day_19.txt") as file:
    contenido = file.read().split("\n")
    for line in contenido:
        info = parse("Blueprint {}: Each ore robot costs {} ore. Each clay robot costs {} ore. Each obsidian robot costs {} ore and {} clay. Each geode robot costs {} ore and {} obsidian.",line)
        robots.append((info.fixed))
def solve(Co, Cc, Co1, Co2, Cg1, Cg2, T):
    best = 0
    S = (0, 0, 0, 0, 1, 0, 0, 0, T)
    Q = deque([S])
    SEEN = set()
    while Q:
        state = Q.popleft()
        o,c,ob,g,r1,r2,r3,r4,t = state
        best = max(best, g)
        if t==0:
            continue
        Core = max([Co, Cc, Co1, Cg1])
        if r1>=Core:
            r1 = Core
        if r2>=Co2:
            r2 = Co2
        if r3>=Cg2:
            r3 = Cg2
        if o >= t*Core-r1*(t-1):
            o = t*Core-r1*(t-1)
        if c>=t*Co2-r2*(t-1):
            c = t*Co2 - r2*(t-1)
        if ob>=t*Cg2-r3*(t-1):
            ob = t*Cg2-r3*(t-1)
        state = (o,c,ob,g,r1,r2,r3,r4,t)
        if state in SEEN:
            continue
        SEEN.add(state)
        assert o>=0 and c>=0 and ob>=0 and g>=0, state
        Q.append((o+r1,c+r2,ob+r3,g+r4,r1,r2,r3,r4,t-1))
        if o>=Co: 
            Q.append((o-Co+r1, c+r2, ob+r3, g+r4, r1+1,r2,r3,r4,t-1))
        if o>=Cc:
            Q.append((o-Cc+r1, c+r2, ob+r3, g+r4, r1,r2+1,r3,r4,t-1))
        if o>=Co1 and c>=Co2:
            Q.append((o-Co1+r1, c-Co2+r2, ob+r3, g+r4, r1,r2,r3+1,r4,t-1))
        if o>=Cg1 and ob>=Cg2:
            Q.append((o-Cg1+r1, c+r2, ob-Cg2+r3, g+r4, r1,r2,r3,r4+1,t-1))
    return best
p1 = 0
p2 = 1
for robot in robots:
    s1 = solve(int(robot[1]), int(robot[2]), int(robot[3]), int(robot[4]),int(robot[5]), int(robot[6]),24)
    p1 += int(robot[0])*s1
for robot in robots[0:3]:
    s2 = solve(int(robot[1]), int(robot[2]), int(robot[3]), int(robot[4]),int(robot[5]), int(robot[6]),32)
    p2 *= s2
print(p1)
print(p2)


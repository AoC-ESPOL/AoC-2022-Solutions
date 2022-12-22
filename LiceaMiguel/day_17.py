input = open('day17.in').read().strip()
lines = [x for x in open('day17.in').read().split('\n')]
top,i,t,added = [0]*4
visited = dict()
def get_p(x, y):
    pieces = {
        0: set([(2,y), (3,y), (4,y), (5,y)]),
        1: set([(3, y+2), (2, y+1), (3,y+1), (4,y+1), (3,y)]),
        2: set([(2, y), (3,y), (4,y), (4,y+1), (4,y+2)]),
        3: set([(2,y),(2,y+1),(2,y+2),(2,y+3)]),
        4: set([(2,y+1),(2,y),(3,y+1),(3,y)])
    }
    return pieces[x]

def walk_up_down(p,up=True):
    movement = []
    for (t,r) in p:
        (movement.append((t,r-1)) if not up else movement.append((t,r+1)))
    return set(movement)

def walk_left_right(p, right=True):
    if (right and len([x==6 for (x,y) in p])>0) or (not right and len([x==0 for (x,y) in p])>0):
        return p
    movement = []
    for (t,r) in p:
        (movement.append((t-1,r)) if not right else movement.append((t+1,r)))
    return set(movement)

rocks = set([(i,0) for i,_ in enumerate(["x"]*7)])
part_len = 1000000000000
s1 = 0
while t<part_len:
    if t==2022:
        s1 = top
    p = get_p(t%5, top+4)
    while True:
        if input[i]=='<':
            p = walk_left_right(p, right=False)
            if p & rocks:
                p = walk_left_right(p)
        else:
            p = walk_left_right(p)
            if p & rocks:
                p = walk_left_right(p, right=False)
        i = (i+1)%len(input)
        p = walk_up_down(p, up=False)
        if p & rocks:
            p = walk_up_down(p)
            rocks = rocks | p
            top = max([y for (_,y) in rocks])
            r_set = frozenset([(x,top-y) for (x,y) in rocks if top-y<=30])

            p_r_bd = (i, t%5, r_set)
            if p_r_bd in visited and t>=2022:
                (oldt, oldy) = visited[p_r_bd]
                dy = top-oldy
                dt = t-oldt
                amt = (part_len-t)//dt
                added += amt*dy
                t += amt*dt
            visited[p_r_bd] = (t,top)
            break
    t += 1
s2 = top+added

print(s1)
print(s2)
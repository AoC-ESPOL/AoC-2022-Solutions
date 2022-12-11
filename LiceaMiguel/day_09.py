lines = [x for x in open('day9.in').read().split("\n")]

tail = head = (0,0)
visited = {tail}

moves = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0),
}

def move_tail(tail,head):
    m1 = (head[0]-tail[0])
    m2 = (head[1]-tail[1])
    t0,t1 = None, None
    if abs(m1)>=2:
        if tail[0]<head[0]:
            t0 = head[0]-1
        else:
            t0 = head[0]+1
    if abs(m2)>=2:
        if tail[1]<head[1]:
            t1 = head[1]-1
        else:
            t1 = head[1]+1
    if abs(m1)>=2 and abs(m2)>=2:
        tail = (t0,t1)
    elif abs(m1)>=2 and abs(m2)<2:
        tail = (t0, head[1])
    elif abs(m2)>=2 and abs(m1)<2:
        tail = (head[0], t1)
    return tail

for line in lines:
    d, c = line.strip().split()
    for i in range(int(c)):
        i1, i2 = moves[d]
        head = (head[0] + i1, head[1]+ i2)
        tail = move_tail(tail,head)
        visited.add(tail)
print(len(visited))

s = [(0,0)]*10
visited = {s[-1]}
for line in lines:
    d, c = line.strip().split()
    for i in range(int(c)):
        i1, i2 = moves[d]
        s[0] = (s[0][0] + i1, s[0][1] + i2)
        for j in range(1, len(s)):
            s[j] = move_tail(s[j],s[j-1])
        visited.add(s[-1])
print(len(visited))

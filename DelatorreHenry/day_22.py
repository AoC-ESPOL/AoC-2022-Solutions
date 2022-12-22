from collections import deque
with open("day_22.txt") as file:
    contenido = file.readlines()
    board = contenido[:-2]
    moves = contenido[-1]
path, walls = set(), set()
startpos = (0,0)
for r,y in enumerate(board):
    for c,x in enumerate(y):
        if board[r][c] == '.':
            if startpos == (0,0):
                startpos = (r+1,c+1)
            path.add((r+1,c+1))
        if board[r][c] == '#':
            walls.add((r+1,c+1))
M = deque([])
x = ''
while moves:
    if moves[0] in 'RL':
        M.append(int(x))
        x = ''
        M.append(moves[0])
    else: x += moves[0]
    moves = moves[1:]
    if len(moves)==0:
        M.append(int(x))

def wrapping(r,c,d):
    if r==1 and 51<=c<=100 and d==3:
        rr,cc=c+100,r
        r,c,d=rr,cc,0
    elif 1<=r<=50 and c==51 and d==2:
        rr,cc=151-r,1
        r,c,d=rr,cc,0
    elif r==1 and 101<=c<=150 and d==3:
        rr,cc=200,c-100
        r,c,d=rr,cc,3
    elif 1<=r<=50 and c==150 and d==0:
        rr,cc=151-r,100
        r,c,d=rr,cc,2
    elif r==50 and 101<=c<=150 and d==1:
        rr,cc=c-50,100
        r,c,d=rr,cc,2 
    elif 51<=r<=100 and c==51 and d==2:
        rr,cc=101,r-50
        r,c,d=rr,cc,1
    elif 51<=r<=100 and c==100 and d==0:
        rr,cc=50,r+50
        r,c,d=rr,cc,3
    elif r==101 and 1<=c<=50 and d==3:
        rr,cc=50+c,51
        r,c,d=rr,cc,0
    elif 101<=r<=150 and c==1 and d==2:
        rr,cc=151-r,51
        r,c,d=rr,cc,0
    elif 101<=r<=150 and c==100 and d==0:
        rr,cc=151-r,150
        r,c,d=rr,cc,2
    elif r==150 and 51<=c<=100 and d==1:
        rr,cc=c+100,50
        r,c,d=rr,cc,2
    elif 151<=r<=200 and c==50 and d==0:
        rr,cc=150,r-100
        r,c,d=rr,cc,3
    elif r==200 and 1<=c<=50 and d==1:
        rr,cc=1,c+100
        r,c,d=rr,cc,1
    elif 151<=r<=200 and c==1 and d==2:
        rr,cc=1,r-100
        r,c,d=rr,cc,1
    return r,c,d

def move(r,c,d,m,p2=False):
    dd = [(0,1),(1,0),(0,-1),(-1,0)]
    nd=d
    if type(m) is str:
        if m == 'R':
            d = (d+1)%4
        elif m == 'L':
            d = (d-1)%4
    else:
        rr,cc = r,c
        for x in range(m):
            rr,cc = rr +dd[d][0], cc+dd[d][1]
            if (rr,cc) not in path and (rr,cc) not in walls:
                if not p2:
                    rr,cc = rr-dd[d][0], cc-dd[d][1]
                    while (rr,cc) in path or (rr,cc) in walls:
                        rr,cc = rr-dd[d][0], cc-dd[d][1]
                    rr,cc = rr +dd[d][0], cc+dd[d][1]
                else:
                    rr,cc,nd = wrapping(r,c,d)
            if (rr,cc) in walls:
                break
            else:
                r,c = rr,cc
                d=nd

    return r,c,d

r,c = startpos
d = 0
for m in M:
    r,c,d = move(r,c,d,m)
print(1000*r +4*c +d)

r,c = startpos
d = 0
for m in M:
    r,c,d = move(r,c,d,m,True)
print(1000*r +4*c +d)

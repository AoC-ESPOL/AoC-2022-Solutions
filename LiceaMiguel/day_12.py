from collections import deque
lines = [x for x in open('day12.in').read().split('\n')]

num_rows = len(lines)
num_columns = len(lines[0])

matrix = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
for i in range(num_rows):
    for j in range(num_columns):
        if lines[i][j]=='S':
            matrix[i][j] = 1
        elif lines[i][j] == 'E':
            matrix[i][j] = 26
        else:
            matrix[i][j] = ord(lines[i][j])-ord('a')+1

def find_shortest1():
    doubly = deque()
    for i in range(num_rows):
        for j in range(num_columns):
            if lines[i][j]=='S':
                doubly.append(((i,j), 0))

    S = set()
    while doubly:
        (i,j),d = doubly.popleft()
        if (i,j) in S:
            continue
        S.add((i,j))
        if lines[i][j]!='E':
            for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                rr = i+dr
                cc = j+dc
                if 0<=rr<num_rows and 0<=cc<num_columns and matrix[rr][cc]<=1+matrix[i][j]:
                    doubly.append(((rr,cc),d+1))
        else: return d
        

def find_shortest2():
    doubly = deque()
    for i in range(num_rows):
        for j in range(num_columns):
            if matrix[i][j] == 1:
                doubly.append(((i,j), 0))

    S = set()
    while doubly:
        (i,j),d = doubly.popleft()
        if (i,j) in S:
            continue
        S.add((i,j))
        if lines[i][j]!='E':
            for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                rr = i+dr
                cc = j+dc
                if 0<=rr<num_rows and 0<=cc<num_columns and matrix[rr][cc]<=1+matrix[i][j]:
                    doubly.append(((rr,cc),d+1))
        else: return d
        
print(find_shortest1())
print(find_shortest2())

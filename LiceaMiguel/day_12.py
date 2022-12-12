from collections import deque
lines = [x for x in open('day12.in').read().split('\n')]

num_rows = len(lines)
num_columns = len(lines[0])
directions = [(-1,0),(0,1),(1,0),(0,-1)]

matrix = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
for i in range(num_rows):
    for j in range(num_columns):
        if lines[i][j]=='S':
            matrix[i][j] = 1
        elif lines[i][j] == 'E':
            matrix[i][j] = 26
        else:
            matrix[i][j] = ord(lines[i][j])-ord('a')+1


def find_start():
    for i in range(num_rows):
        for j in range(num_columns):
            if lines[i][j]=='S':
                return (i,j)
    return (-1,-1)

def find_end():
    for i in range(num_rows):
        for j in range(num_columns):
            if matrix[i][j] == 1:
                return (i,j)
    return (-1,-1)

def search(node):
    queue = deque()
    queue.append((node, 0))
    visited = set()

    while queue:
        (i,j),dist = queue.popleft()
        if (i,j) in visited:
            continue
        visited.add((i,j))
        if lines[i][j]!='E':
            for dir_row, dir_col in directions:
                c_r = i+dir_row
                c_c = j+dir_col
                if 0<=c_r<num_rows and 0<=c_c<num_columns and matrix[c_r][c_c]<=1+matrix[i][j]:
                    queue.append(((c_r,c_c),dist+1))
        else:
            return dist

print(search(find_start()))
print(search(find_end()))
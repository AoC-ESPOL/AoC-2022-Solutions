with open("day_12.txt") as file:
    contenido = file.readlines()

import numpy as np
from collections import deque

matriz = [x[:-2] for x in contenido]
n = len(matriz)
m = len(matriz[0])
matriz_signal = np.zeros((n,m),int)
print(matriz_signal)

for x in range(n):
    for y in range(m):
        if matriz[x][y]=='S':
            matriz_signal[x][y] = 1
        elif matriz[x][y] == 'E':
            matriz_signal[x][y] = 26
        else:
            matriz_signal[x][y] = ord(matriz[x][y])-ord('a')+1
print(matriz_signal)

def signal_tracker(part):
    l1 = deque()
    c1 = set()
    for x in range(n):
        for y in range(m):
          condicion1 = part==1 and matriz[x][y]=='S'
          condicion2 = part==2 and matriz_signal[x][y] == 1
          if condicion1 or condicion2:
            l1.append(((x,y), 0))
    while l1:
        (x,y),d = l1.popleft()
        if (x,y) in c1:
            continue
        c1.add((x,y))
        if matriz[x][y]=='E':
            return d
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            x1,y1 = x+dr,y+dc
            condicion1 = 0<=x1<n
            condicion2 = 0<=y1<m
            if condicion1 and condicion2 and matriz_signal[x1][y1]<=1+matriz_signal[x][y]:
                l1.append(((x1,y1),d+1))
    return None

print(signal_tracker(1))
print(signal_tracker(2))

with open("day_09.txt") as file:
    contenido = file.read().splitlines()

import numpy as np

def tracker(n):
    tracked = {(0, 0)}
    crd = np.zeros((n, 2))
    for order in contenido:
        direction, steps = order.split()
        for _ in range(int(steps)):
            crd[0] += {'L':(0, -1),'R':(0, 1),'U':(1, 0),'D':(-1, 0)}[direction]
            for i in range(1, len(crd)):
                delta = crd[i - 1] - crd[i]
                if np.linalg.norm(delta) >= 2:
                    crd[i] += np.sign(delta)
            tracked.add(tuple(crd[len(crd) - 1]))
    return len(tracked)

print(tracker(2))
print(tracker(10))

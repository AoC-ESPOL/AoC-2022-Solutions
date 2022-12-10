import numpy as np

with open("day_08.txt") as file:
    bosque = np.genfromtxt(file, delimiter=1)
perimetro = 2 * np.sum(bosque.shape) - 4
parte1 = perimetro
parte2 = -1

def view_gen(bosque):
    h, w = bosque.shape
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            u = bosque[i, j] > bosque[:i, j][::-1]
            d = bosque[i, j] > bosque[i + 1 :, j]
            l = bosque[i, j] > bosque[i, :j][::-1]
            r = bosque[i, j] > bosque[i, j + 1 :]
            yield u, d, l, r

for view in view_gen(bosque):
    parte1 += any(map(all,view))

def count_visible(mask):
    if mask.all():
        output = mask.sum()
    else:
        output = 1 + mask.argmin()
    return output

for view in view_gen(bosque):
    parte2 = max(parte2, np.product([count_visible(mask) for mask in view]))

print(parte1)
print(parte2)

l1,x0,x1 = [[]],[[2]],[[6]]
l2 = [x0,x1]
cont = 0
import functools

with open("day_13.txt") as file:
  contenido = file.readlines()
  for line in contenido:
    if line == '\n':
      l1.append([])
    else:
      l1[-1].append(eval(line))
      l2.append(eval(line))

def comparator(x,y):
    i = 0
    for i in range(min(len(x), len(y))):
        if type(x[i]) != type(y[i]):
            if type(x[i]) == type(0):
                x[i] = [x[i]]
            else:
                y[i] = [y[i]]
        if type(x[i]) == type(0):
            if x[i] < y[i]:
                return 1
            elif x[i] > y[i]:
                return -1
        else:
            k = comparator(x[i], y[i])
            if k:
                return k
    if len(x) == len(y):
        return 0
    elif len(x) < len(y):
        return 1
    else:
        return -1

for i in range(len(l1)):
    if comparator(l1[i][0], l1[i][1]) == 1:
        cont += i + 1
print(cont)

l2.sort(key=functools.cmp_to_key(comparator), reverse=True)
valor1 = l2.index(x0)
valor2 = l2.index(x1)
print( (valor1+1) * (valor2+1))

def dia6_p1(path):
  file = open(path, "r")
  for line in file:
    lista = []
    conjunto = set()
    for i in range(len(line)):
      if len(lista) < 14:
        lista.append(line[i])
      else:
        lista.pop(0)
        lista.append(line[i])
        conjunto = set(lista)
        if len(conjunto) == 14:
          return i + 1

def dia6_p2(path):
  file = open(path, "r")
  for line in file:
    lista = []
    conjunto = set()
    for i in range(len(line)):
      if len(lista) < 14:
        lista.append(line[i])
      else:
        lista.pop(0)
        lista.append(line[i])
        conjunto = set(lista)
        if len(conjunto) == 14:
          return i + 1
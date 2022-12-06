def dia5_p1(path):
  file = open(path, "r")
  pilas = []
  not_valid = [" ", "[", "]", "1", "2", "3", "4", "5", "6", "7", "8", "9", "\n"]
  for i in range(9):
    pilas.append([])
  for line in file:
    if line.startswith("move"):
      partes = line.split(" ")
      num = int(partes[1])
      origen = int(partes[3]) - 1
      destino = int(partes[5]) - 1
      for i in range(num):
        obj = pilas[origen].pop()
        pilas[destino].append(obj)
    elif line == "\n":
      for i in range(9):
        pilas[i].reverse()
    else:
      for i in range(len(line)):
        if line[i] not in not_valid:
          idx = int((i-1) / 4)
          pilas[idx].append(line[i])
  res = ""
  for i in range(9):
      res += pilas[i].pop()
  return res

def dia5_p2(path):
  file = open(path, "r")
  pilas = []
  not_valid = [" ", "[", "]", "1", "2", "3", "4", "5", "6", "7", "8", "9", "\n"]
  for i in range(9):
    pilas.append([])
  for line in file:
    if line.startswith("move"):
      partes = line.split(" ")
      num = int(partes[1])
      origen = int(partes[3]) - 1
      destino = int(partes[5]) - 1
      pila_tmp = []
      for i in range(num):
        obj = pilas[origen].pop()
        pila_tmp.append(obj)
      for i in range(num):
        obj = pila_tmp.pop()
        pilas[destino].append(obj)
    elif line == "\n":
      for i in range(9):
        pilas[i].reverse()
    else:
      for i in range(len(line)):
        if line[i] not in not_valid:
          idx = int((i-1) / 4)
          pilas[idx].append(line[i])
  res = ""
  for i in range(9):
      res += pilas[i].pop()
  return res
  
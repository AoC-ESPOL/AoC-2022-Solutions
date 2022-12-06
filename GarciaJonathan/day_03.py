def dia1_p1(path):
  file = open(path, "r")
  res = []
  for line in file:
    long = int(len(line)/2)
    first = line[:long]
    second = line[long:]
    encontrado = False
    for i in range(len(first)):
      for j in range(len(second)):
        if first[i] == second[j]:
          val1 = 0
          if first[i] == first[i].lower():
            val1 = ord(first[i]) - 96
          else:
            val1 = ord(first[i]) - 38
          encontrado = True
          res.append(val1)
          break
      if encontrado:
        break
  return sum(res)
        
def dia2_p2(path):
  file = open(path, "r")
  res = 0
  tmp = []
  for line in file:
    encontrado = False
    tmp.append(line)
    if len(tmp) == 3:
      first = tmp[0]
      second = tmp[1]
      third = tmp[2]
      for i in range(len(first)):
        for j in range(len(second)):
          for k in range(len(third)):
            if first[i] == second[j] and second[j] == third[k]:
              if first[i] == first[i].lower():
                val1 = ord(first[i]) - 96
              else:
                val1 = ord(first[i]) - 38
              encontrado = True
              res += val1
              break
          if encontrado:
            break
        if encontrado:
          break
      tmp = []
  return res
    
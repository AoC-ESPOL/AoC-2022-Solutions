def sign(x):
  if x > 0:
    return 1
  elif x < 0:
    return -1
  else:
    return 0

def move_single_knot(F, S, idx, positions, knots):
  f_x, f_y = F
  s_x, s_y = S
  dif_x = f_x - s_x
  dif_y = f_y - s_y
  if (abs(dif_x) > 1 or abs(dif_y) > 1):
    if (f_x != s_x and f_y != s_y):
      s_x += sign(dif_x)
      s_y += sign(dif_y)
    elif f_x == s_x:
      s_y += sign(dif_y)
    elif f_y == s_y:
      s_x += sign(dif_x)
    if idx == knots-1:
      positions.add((s_x, s_y))
  return (s_x, s_y)

def move_knots_v2(colas, direccion, pasos, positions):
  letras = ["L", "R", "U", "D"]
  lista = [(-1, 0), (1, 0), (0, 1), (0, -1)]
  idx = letras.index(direccion)
  value_x, value_y = lista[idx]
  for i in range(pasos):
    h_x, h_y = colas[0]
    h_x += value_x
    h_y += value_y
    colas[0] = (h_x, h_y)
    for j in range(0, len(colas)-1):
      colas[j+1] = move_single_knot(colas[j], colas[j+1], j+1, positions, len(colas))
  return colas

def day9(path, knots):
  file = open(path, "r")
  pos = set()
  colas = []
  for i in range(knots):
    colas.append((0,0))
  for line in file:
    direccion, pasos = line.strip().split(" ")
    colas = move_knots_v2(colas, direccion, int(pasos), pos)
  return len(pos) + 1

print(day9("GarciaJonathan\data\day_09.txt", 2))
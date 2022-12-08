def day8_v1(path):
  file = open(path, "r")
  matrix = []
  for line in file:
    fila = []
    clean_line = line.strip()
    for i in range(len(clean_line)):
      fila.append(int(clean_line[i]))
    matrix.append(fila)
  return matrix

def is_visible(x,y, matrix):
  value = matrix[y][x]
  filas = len(matrix)
  columnas = len(matrix[0])
  for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
    tmp_x = x + dx
    tmp_y = y + dy
    direccion = True
    while (tmp_x >= 0 and tmp_y >= 0 and tmp_x < columnas and tmp_y < filas):
      if matrix[tmp_y][tmp_x] >= value:
        direccion = False
        break
      tmp_x = tmp_x + dx
      tmp_y = tmp_y + dy
      direccion = True
    if direccion:
      return True
  return False

def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

def scenic_value(x,y, matrix):
  value = matrix[y][x]
  filas = len(matrix)
  columnas = len(matrix[0])
  scene_value = []
  for dx, dy in [(0,1), (-1,0), (1,0), (0,-1)]:
    tmp_x = x + dx
    tmp_y = y + dy
    arboles = 1
    blocked = False
    while (tmp_x >= 0 and tmp_y >= 0 and tmp_x < columnas and tmp_y < filas):
      if matrix[tmp_y][tmp_x] >= value:
        blocked = True
        scene_value.append(arboles)
        break
      tmp_x = tmp_x + dx
      tmp_y = tmp_y + dy
      arboles += 1
    if (not blocked):
      scene_value.append(arboles-1)
  return multiplyList(scene_value)

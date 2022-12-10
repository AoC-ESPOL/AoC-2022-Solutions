def day10_v1(path):
  file = open(path, "r")
  view_cycles = []
  for i in range(0, 6):
    view_cycles.append(i * 40 + 20)
  x = 1
  i = 1
  r = 0
  total = 0
  for line in file:
    partes = line.strip().split(" ")
    if len(partes) == 2:
      values = int(partes[1])
      r = 2
      while (r > 0):
        if i in view_cycles:
          total += x * i
        i += 1
        r -= 1
      x += values
    else:
      if i in view_cycles:
        total += x * i
      i += 1
  return total

def draw_pixel(spr_pos, cycle, new_lines):
  index_row = cycle % 40
  res = ""
  if index_row == spr_pos or index_row == spr_pos+1 or index_row == spr_pos+2:
    res += "#"
  else:
    res += "."
  if cycle in new_lines:
    res += "\n"
  return res

def day10_v2(path):
  file = open(path, "r")
  new_lines = []
  for i in range(1,7):
    new_lines.append(i * 40)
  sprite_pos = 1
  cycle = 1
  r = 0
  res = ""
  for line in file:
    partes = line.strip().split(" ")
    if len(partes) == 2:
      values = int(partes[1])
      r = 2
      while (r > 0):
        res += draw_pixel(sprite_pos, cycle, new_lines)
        cycle += 1
        r -= 1
      sprite_pos += values
    else:
      res += draw_pixel(sprite_pos, cycle, new_lines)
      cycle += 1
  return res
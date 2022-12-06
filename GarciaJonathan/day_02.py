def dia2_p1(path):
  enemy_shape = ["A", "B", "C"]
  player_shape = ["X", "Y", "Z"]
  values = [1, 2, 3]
  file = open(path, "r")
  total = 0
  for line in file:
    enemy, player = line.strip().split(" ")
    idx_ene = enemy_shape.index(enemy)
    idx_ply = player_shape.index(player)
    act_round = values[idx_ply]
    if idx_ene == idx_ply:
      act_round += 3
    elif idx_ply == idx_ene + 1:
      act_round += 6
    elif idx_ply == 0 and idx_ene == 2:
      act_round += 6
    total += act_round
  return total

def dia2_p2(path):
  enemy_shape = ["A", "B", "C"]
  values = [1, 2, 3]
  file = open(path, "r")
  total = 0
  for line in file:
    enemy, player = line.strip().split(" ")
    idx_ene = enemy_shape.index(enemy)
    act_round = 0
    if player == "X":
      if idx_ene == 0:
        act_round += values[2]
      else:
        act_round += values[idx_ene-1]
    elif player == "Y":
      act_round += 3
      act_round += values[idx_ene]
    elif player == "Z":
      act_round += 6
      if idx_ene == 2:
        act_round += values[0]
      else:
        act_round += values[idx_ene+1]
    total += act_round

  return total
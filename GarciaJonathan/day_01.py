# Part 1

def get_most_elve(path):
  file = open(path, "r")
  max_value = 0
  curr = 0
  for line in file:
    if (line == "\n"):
      curr = 0
    else:
      curr += int(line.strip())
      max_value = max(curr, max_value)
  return max_value

# Part 2

def get_top_elve(path):
  file = open(path, "r")
  elve_calories = []
  max_value = 0
  curr = 0
  for line in file:
    if (line == "\n"):
      elve_calories.append(curr)
      curr = 0
    else:
      curr += int(line.strip())
      max_value = max(curr, max_value)
  elve_calories.sort(reverse=True)
  return sum(elve_calories[:3])

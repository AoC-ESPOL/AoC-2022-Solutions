from structures import Directorio, File

def day7_v1(path):
  file = open(path, "r")
  root = Directorio("/")
  actual_dir = root
  for line in file:
    if (line.startswith("$")):
      partes = line.split(" ")
      if len(partes) == 3:
        new_dir = partes[2].strip()
        if (new_dir == ".."):
          actual_dir = actual_dir.parent
        else:
          dirs = actual_dir.files
          for element in dirs:
            if type(element) == Directorio:
              if element.name == new_dir:
                actual_dir = element
                break
    elif (line.startswith("dir")):
      partes = line.split(" ")
      new_dir = partes[1].strip()
      actual_dir.files.append(Directorio(new_dir, actual_dir))
    else:
      peso, new_file = line.split(" ")
      actual_dir.files.append(File(new_file.strip(), int(peso)))
  return root

def getDirectoriesWeight(directorio):
  res = []
  total = getDirectoriesWeightHelper(directorio, res)
  return res, total

def getDirectoriesWeightHelper(directorio, res):
  current_weight = 0
  for element in directorio.files:
    if type(element) == File:
      current_weight += element.weight
    else:
      current_weight += getDirectoriesWeightHelper(element, res)

  if current_weight <= 100000:
    res.append(current_weight)

  return current_weight

a = day7_v1("GarciaJonathan\data\day_07.txt")
res, total = getDirectoriesWeight(a)
print(sum(res), total)

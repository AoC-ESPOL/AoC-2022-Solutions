def dia4_p1(path):
  file = open(path, "r")
  res = 0
  for line in file:
    first, second = line.split(",")
    first1, first2 = first.split("-")
    second1, second2 = second.split("-")

    if int(first1) <= int(second1) and int(first2) >= int(second2):
      res += 1
    elif int(second1) <= int(first1) and int(second2) >= int(first2):
      res += 1
  return res

def dia4_p2(ini, fin):
  res = []
  for element in range(fin-ini+1):
    tmp = element + ini
    res.append(tmp)
  return res

def rucksack2(path):
  file = open(path, "r")
  res = 0
  for line in file:
    first, second = line.split(",")
    first1, first2 = first.split("-")
    second1, second2 = second.split("-")

    set1 = set(sum_data(int(first1), int(first2)))
    set2 = set(sum_data(int(second1), int(second2)))

    if len(set1.intersection(set2)) > 0:
      res +=1

  return res
#DAVID STEVEN AUQUI MORA
#DAY 1 ADVENT OF CODE

#PART1
def max(list):
    max = list[0];
    for x in list:
        if x > max:
            max = x
    return max

file = input("Enter the name of the file that contains the calories of the elves including its extension: \n")

listOfCalories = []

list = open(file)
lines = list.readlines()
size = len(lines)

count = 0
cont = 0
for line in lines:
    line = line.replace("\n","")

    if line != "":
        count = count + int(line)

    if (line == "") or (cont+1 == size):
        listOfCalories.append(count)
        count = 0
    cont+=1
list.close()

max = max(listOfCalories)
name = listOfCalories.index(max) + 1

print("\nThe elf with the most calories is the elf "+str(name)+", with "+str(max)+" calories")

#PART2
listOfCaloriesCopy = listOfCalories.copy()
listOfCaloriesCopy.sort()
listOfCaloriesCopy.reverse()


countTotal = 0
for x in range(3):
    countTotal += listOfCaloriesCopy[x]

print("\nThe total calories of the 3 elves with the highest calories consumed is "+str(countTotal))
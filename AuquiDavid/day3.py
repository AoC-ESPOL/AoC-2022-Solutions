
#--- Part One ---
lowerLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
scoreLower = list(range(1,27))

capitalLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
scoreCapital = list(range(27,53))

file = open("input.txt")
lines = file.readlines()

score=0
for line in lines:
    line = line.replace("\n","")
    num = len(line)
    num = num/2
    list1 = line[:int(num)]
    list2 = line[int(num):]
    letter = ""
    for i in list1:
        if i in list2:
            letter = i

    if letter in lowerLetters:
        score+=scoreLower[lowerLetters.index(letter)]
    if letter in capitalLetters:
        score += scoreCapital[capitalLetters.index(letter)]
file.close()

print("--- Part One ---")
print(score)

#--- Part Two ---
scoreList = []

score2 = 0
list = []
counter = 0
for line in lines:
    line = line.replace("\n","")
    if counter < 3:
        list.append(line)
        if counter == 2:
            common1 = set(list[0]).intersection(list[1])
            for i in common1:
                if i in list[2]:
                    letter = i
            if letter in lowerLetters:
                score2 += scoreLower[lowerLetters.index(letter)]
            if letter in capitalLetters:
                score2 += scoreCapital[capitalLetters.index(letter)]
    counter += 1
    if counter == 3:
        counter = 0
        list=[]
print("\n--- Part Two ---")
print(score2)
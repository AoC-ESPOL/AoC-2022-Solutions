#DAVID STEVEN AUQUI MORA
#DAY 2 ADVENT OF CODE

#--- Part 1 ---
scores=[]
#Open the file
file = open("input.txt")
lines = file.readlines()

counter = 0
for line in lines:
    line = line.replace("\n","")
    line = line.split(" ")
    if line[0] == "A": #player 1 choose Rock
        if line[1] == "X": #player 2 choose Rock
            counter+=1 #because you choose rock
            counter+=3 #because it is a tie
        elif line[1] == "Y": #player 2 choose Paper
            counter+=2 #because you choose paper
            counter+=6 #because you won
        elif line[1] == "Z": #player 2 choose Scissors
            counter+=3 #because you choose scissors
            counter+=0 #because you lost

    elif line[0] == "B": #player 1 choose Paper
        if line[1] == "X": #player 2 choose Rock
            counter+=1 #because you choose rock
            counter+=0 #because you lost
        elif line[1] == "Y": #player 2 choose Paper
            counter+=2 #because you choose paper
            counter+=3 #because it is a tie
        elif line[1] == "Z": #player 2 choose Scissors
            counter+=3 #because you choose scissors
            counter+=6 #because you won

    elif line[0] == "C": #player 1 choose Scissors
        if line[1] == "X": #player 2 choose Rock
            counter+=1 #because you choose rock
            counter+=6 #because you won
        elif line[1] == "Y": #player 2 choose Paper
            counter+=2 #because you choose paper
            counter+=0 #because you won
        elif line[1] == "Z": #player 2 choose Scissors
            counter+=3 #because you choose scissors
            counter+=3 #because it is a tie
    scores.append(counter)
    counter = 0

file.close()
scoreTotal = sum(scores)
print("--- Part 1 ---")
print("You would get a total score of "+str(scoreTotal))

#--- Part 2 ---
scores2 = []
counter = 0
for line in lines:
    line = line.replace("\n","")
    line = line.split(" ")
    if line[0] == "A": #player 1 choose Rock
        if line[1] == "X": #you need to lose
            counter+=3 #because you choose scissors
            counter+=0
        elif line[1] == "Y": #you need to end the round in a draw
            counter+=1 #because you choose rock
            counter+=3
        elif line[1] == "Z": #you need to win
            counter+=2 #because you choose paper
            counter+=6

    elif line[0] == "B": #player 1 choose Paper
        if line[1] == "X":  # you need to lose
            counter += 1  # because you choose rock
            counter += 0
        elif line[1] == "Y":  # you need to end the round in a draw
            counter += 2  # because you choose paper
            counter += 3
        elif line[1] == "Z":  # you need to win
            counter += 3  # because you choose scissors
            counter += 6

    elif line[0] == "C": #player 1 choose Scissors
        if line[1] == "X":  # you need to lose
            counter += 2  # because you choose paper
            counter += 0
        elif line[1] == "Y":  # you need to end the round in a draw
            counter += 3  # because you choose scissors
            counter += 3
        elif line[1] == "Z":  # you need to win
            counter += 1  # because you choose rock
            counter += 6
    scores2.append(counter)
    counter = 0
scoreTotal2 = sum(scores2)
print("\n\n--- Part 2 ---")
print("Your total score would be "+str(scoreTotal2))
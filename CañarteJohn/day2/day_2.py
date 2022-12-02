

#X = 1          W = 6
#Y = 2          D = 3
#Z = 3          L = 0

lPrueba = ["A Y","B X","C Z"]
ltorneo = []

#dir = "/home/john/Desktop/input2"

doc = open("input2","r")

for l in doc:
    linea = l.strip()
    ltorneo.append(linea)
doc.close

def valueCal(c):
    if c == "A" or c == "X":
        return 1
    if c == "B" or c == "Y":
        return 2
    if c == "C" or c == "Z":
        return 3


def wCheck(a,b):
    if a == 1:
        if b != 2:
            return False
        else:
            return True
    if a == 2:
        if b != 3:
            return False
        else:
            return True
    if a == 3:
        if b != 1:
            return False
        else:
            return True

def roundScore(round):
    t = 0
    play = round.split(" ")
    p1 = valueCal(play[0])
    p2 = valueCal(play[1])
    
    if p1 == p2:
        return p2 + 3
    if wCheck(p1,p2):
        return p2 + 6
    else:
        return p2 + 0
    

def tScoreCal (lTor):
    ac = 0
    for r in lTor:
        ac += roundScore(r)
    return "El puntaje total es: "+str(ac)

print(tScoreCal(lPrueba))
print(tScoreCal(ltorneo))



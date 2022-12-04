

#A = 1         Z = W = 6
#B = 2         Y = D = 3
#C = 3         X = L = 0

lPrueba = ["A Y","B X","C Z"]
ltorneo = []

dir = "/home/john/Desktop/day2/input2"

doc = open(dir,"r")

for l in doc:
    linea = l.strip()
    ltorneo.append(linea)
doc.close

def valueCal(c):
    if c == "A" :
        return 1
    if c == "B" :
        return 2
    if c == "C" :
        return 3

def valCheck(a,b):
    if b == "Y":
        return a + 3
    if b == "Z":
        if a != 3:
            return a + 1 + 6
        else:
            return 1 + 6
    if b == "X":
        if a != 1:
            return a - 1 
        else: 
            return 3


def roundScore(round):

    play = round.split(" ")
    p1 = valueCal(play[0])
    p2 = play[1]
    return valCheck(p1,p2)
    
        
    
    
    

def tScoreCal (lTor):
    ac = 0
    for r in lTor:
        ac += roundScore(r)
    return "El puntaje total es: "+str(ac)

print(tScoreCal(lPrueba))
print(tScoreCal(ltorneo))



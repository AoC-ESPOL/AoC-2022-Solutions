#David Auqui

# DAY 8
# -- PART ONE --
file = open("input.txt")
lines = file.readlines()
file.close()

rows = 0
columns = 0
for line in lines:
    line = line.replace("\n", "")
    lines[columns] = line
    rows = len(line)
    columns+=1

receiver = 0

conti = 1
for i in lines[1:rows-1]:
    i = i.replace("\n", "")
    contj = 1
    for j in i[1:columns-1]:
        arr = 0
        abj = 0
        der = 0
        izq = 0

        #Arriba
        for z in lines[:conti]:
            if int(z[contj]) >= int(j):
                arr = 1
        #Abajo
        for z in lines[conti+1:]:
            if int(z[contj]) >= int(j):
                abj = 1
        #Derecha
        line = lines[conti]
        for k in line[contj+1:]:
            if int(k) >= int(j):
                der = 1
        #Izquierda
        line = lines[conti]
        for k in line[:contj]:
            if int(k) >= int(j):
                izq = 1

        if arr == 1 and abj == 1 and der == 1 and izq == 1:
            receiver += 1
        contj+=1
    conti+=1

total = ( rows * columns ) - receiver
print("-- PART ONE --")
print(total)


#-- PART TWO --

score = 0

conti = 1
for i in lines[1:rows-1]:

    i = i.replace("\n", "")
    contj = 1
    for j in i[1:columns-1]:
        #Arriba
        arr = 0
        cont = 1
        line = []
        for z in lines[:conti]:
            line.append(z[contj])
        for k in reversed(line):
            if int(k) >= int(j):
                if arr == 0:
                    arr = cont
            cont += 1
        if arr == 0:
            arr = cont-1

        #Abajo
        abj = 0
        cont = 1
        line = []
        for z in lines[conti+1:]:
            line.append(z[contj])
        for k in line:
            if int(k) >= int(j):
                if abj == 0:
                    abj = cont
            cont += 1
        if abj == 0:
            abj = cont-1

        #Derecha
        der = 0
        cont = 1
        line = lines[conti]
        for k in line[contj+1:]:
            if int(k) >= int(j):
                if der == 0:
                    der = cont
            cont += 1
        if der == 0:
            der = cont-1

        #Izquierda
        izq = 0
        cont = 1
        line = lines[conti]
        for k in reversed(line[:contj]):
            if int(k) >= int(j):
                if izq == 0:
                    izq = cont
            cont += 1
        if izq == 0:
            izq = cont-1

        total = arr * abj * der * izq

        if total >= score:
            score = total

        contj+=1
    conti+=1

print("\n-- PART TWO --")
print(score)

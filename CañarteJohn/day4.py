
listaP = []

doc = open('/home/john/Desktop/input','r')
for i in doc:
    linea = (i.strip()).split(',')
    listaP.append(linea)
doc.close()    


def contaR(lista):
    c = 0
    for l in lista:
        p1 = l[0].split('-')
        p2 = l[1].split('-')
        if (int(p1[0]) >= int(p2[0]) and int(p1[1]) <= int(p2[1])) or (int(p2[0]) >= int(p1[0]) and int(p2[1]) <= int(p1[1])):
            c += 1
    return c

#t=contaR(listaP)


#print('El total es: '+ str(t) )


def contarOver(lista):
    over = 0
    for l in lista:
        p1 = l[0].split('-')
        p2 = l[1].split('-')
        l1 = set([*range(int(p1[0]),int(p1[1])+1)])
        l2 = set([*range(int(p2[0]),int(p2[1])+1)])
        if (l1 & l2) != set():
            over +=1
    return over

tt= contarOver(listaP)
print('El total es: ' +str(tt))
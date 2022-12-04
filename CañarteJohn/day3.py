
listaP = ['vJrwpWtwJgWrhcsFMMfFFhFp',
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg',
'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
'ttgJtRGJQctTZtZT',
'CrZsJsPPZsGzwwsLwLmpwMDw']

listaR = []


doc = open('/home/john/Desktop/input','r')

for l in doc:
    linea = l.strip()
    listaR.append(linea)
doc.close

    


alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def getPriority(a):
    if (a in alpha):
        return alpha.index(a)+1
    else:
        return alpha.index(a.swapcase())+27




def totalError(lista):
    half = 0
    ac = 0
    for i in lista:
        half = int(len(i)/2)
        c1 = set(i[:half])
        c2 = set(i[half:])
        r = c1 & c2
        ac += getPriority(r.pop())
    return 'El total de prioridades es: '+ str(ac)        

#print(totalError(listaP))

#print(totalError(listaR))

def formarG(lista):
    grupos = []
    grupo = []
    for i in lista:
        grupo.append(i)
        if len(grupo) == 3:
            grupos.append(grupo)
            grupo = []
    return grupos


def badgeSearch(lista):
    ac=0
    listaG = formarG(lista)
    for i in listaG:
        c1 = set(i[0])
        c2 = set(i[1])
        c3 = set(i[2])
        r = c1 & c2 & c3
        ac += getPriority(r.pop())
    return 'El total de prioridades es: '+ str(ac)    

print(badgeSearch(listaP))    

print(badgeSearch(listaR))


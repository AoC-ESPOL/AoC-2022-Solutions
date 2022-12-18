with open("day_17.txt") as file:
    contenido = file.read().strip()

lines = [x for x in contenido.split('\n')]

final_c = {}
max_t = 0
i = 0
n = 0
add = 0

def izquierda(p):
    if any([x==0 for (x,y) in p]):
        return p
    return set([(x-1,y) for (x,y) in p])
def derecha(p):
    if any([x==6 for (x,y) in p]):
        return p
    return set([(x+1,y) for (x,y) in p])
def abajo(p):
    return set([(x,y-1) for (x,y) in p])
def arriba(p):
    return set([(x,y+1) for (x,y) in p])

def get_p(x, y): 
    D = set()
    if x==0:
        return set([(2,y), (3,y), (4,y), (5,y)])
    elif x==1:
        return set([(3, y+2), (2, y+1), (3,y+1), (4,y+1), (3,y)])
    elif x==2:
        return set([(2, y), (3,y), (4,y), (4,y+1), (4,y+2)])
    elif x==3:
        return set([(2,y),(2,y+1),(2,y+2),(2,y+3)])
    elif x==4:
        return set([(2,y+1),(2,y),(3,y+1),(3,y)])
    else:
        assert False

def mostrar(R):
    altura_max = max([y for (x,y) in R])
    for y in range(altura_max,0,-1):
        row = ''
        for x in range(7):
            if (x,y) in R:
                row += '#'
            else:
                row += ' '
        print(row)

c_p = set([(x,0) for x in range(7)])

def signature(R):
    maxY = max([y for (x,y) in R])
    return frozenset([(x,maxY-y) for (x,y) in R if maxY-y<=30])

part_2 = 1000000000000

while n<part_2:
    piece = get_p(n%5, max_t+4)
    while True:
        if contenido[i]=='<':
            piece = izquierda(piece)
            if piece & c_p:
                piece = derecha(piece)
        else:
            piece = derecha(piece)
            if piece & c_p:
                piece = izquierda(piece)
        i = (i+1)%len(contenido)
        piece = abajo(piece)
        if piece & c_p:
            piece = arriba(piece)
            c_p |= piece
            max_t = max([y for (x,y) in c_p])
            SR = (i, n%5, signature(c_p))
            if SR in final_c and n>=2022:
                (oldt, oldy) = final_c[SR]
                dy = max_t-oldy
                dt = n-oldt
                amt = (part_2-n)//dt
                add += amt*dy
                n += amt*dt
                assert n<=part_2
            final_c[SR] = (n,max_t)
            break
    n += 1
    if n==2022:
        print(max_t)
print(max_t+add)







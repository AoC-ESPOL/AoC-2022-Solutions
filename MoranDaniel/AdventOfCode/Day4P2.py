#Advent Of Code 2022
#Day 4 P1
#Daniel Moran

def Overlaps(a,b):
    if int(a[0]) <= int(a[1]) < int(b[0]) <= int(b[1]):
        return 0
    elif int(a[0]) <= int(a[1]) and int(b[0]) <= int(b[1]) and int(b[1]) < int(a[0]):
        return 0
    else:
        return 1


Today_input = open("Day4input.txt","r")

contador = 0

lineas = Today_input.readlines()

for linea in lineas:
    dividida = linea.strip().split(",")
    print(dividida)
    a, b = dividida[0], dividida[1]
    a1, b1 = a.split("-"), b.split("-")

    if Overlaps(a1, b1):
        print(1)
        contador+=1


print(contador)

'''
#dividida = ['2-7', '8-9']
#dividida = ['8-9', '2-2']
dividida = ['7-7', '3-8']
a, b = dividida[0], dividida[1]
a1, b1 = a.split("-"), b.split("-")
print(Overlaps(a1, b1))
'''
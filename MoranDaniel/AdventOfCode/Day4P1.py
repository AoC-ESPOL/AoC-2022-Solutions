#Advent Of Code 2022
#Day 4 P1
#Daniel Moran

def Contiene_a(a,b):
    if int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1]):
        return 1
    elif int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1]):
        return 1
    else:
        return 0


Today_input = open("Day4input.txt","r")

contador = 0

lineas = Today_input.readlines()

for linea in lineas:
    dividida = linea.strip().split(",")
    a, b = dividida[0], dividida[1]
    a1, b1 = a.split("-"), b.split("-")
    if Contiene_a(a1, b1):
        contador+=1

print(contador)


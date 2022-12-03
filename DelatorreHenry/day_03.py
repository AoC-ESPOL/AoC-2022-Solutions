import string
lowers = list(string.ascii_lowercase)
uppers = list(string.ascii_uppercase)
letras = lowers + uppers

total = 0
#PARTE 1
with open("input1.txt") as file:
  for line in file:
    mochila = line.strip()
    n_items = len(mochila)
    mitad = n_items//2
    item_1 = mochila[0:mitad]
    item_2 = mochila[mitad:]
    conjunto1 = set(list(item_1))
    conjunto2 = set(list(item_2))
    item_f = (conjunto1 & conjunto2)
    posicion = letras.index(list(item_f)[0])
    puntos = posicion + 1
    total += puntos
print(total)

#PARTE 2 
total = 0
with open("input1.txt") as file:
  contador = 1
  lineas = file.readlines()
  ult_item = len(lineas)-2
  for i in range(0,ult_item,3): 
    conjunto1 = set(list(lineas[i].strip()))
    conjunto2 = set(list(lineas[i+1].strip()))
    conjunto3 = set(list(lineas[i+2].strip()))
    item_f = (conjunto1 & conjunto2 & conjunto3)
    posicion = letras.index(list(item_f)[0])
    puntos = posicion + 1
    total += puntos
print(total)

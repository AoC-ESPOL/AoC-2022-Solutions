lista1 = ["R","G","J","B","T","V","Z"]
lista2 = ["J","R","V","L"]
lista3 = ["S","Q","F"]
lista4 = ["Z","H","N","L","F","V","Q","G"]
lista5 = ["R","Q","T","J","C","S","M","W"]
lista6 = ["S","W","T","C","H","F"]
lista7 = ["D","Z","C","V","F","N","J"]
lista8 = ["L","G","Z","D","W","R","F","Q"]
lista9 = ["J","B","W","V","P"]

carga = [lista1,lista2,lista3,lista4,lista5,lista6,lista7,lista8,lista9]
print(carga)

parte = input("INGRESE PARTE 1/2:")
with open("day_05.txt") as file:
  for line in file:
      move , charge , desde, lista1, a, lista2 = line.strip().split(" ")
      charge = int(charge)
      lista1 = int(lista1)-1
      lista2 = int(lista2)-1
      lista3 = carga[lista1].copy()
      lista3 = lista3[0:-charge]
      if parte=="1":
          carga[lista2].extend(carga[lista1][-charge:][::-1])
      elif parte=="2":
          carga[lista2].extend(carga[lista1][-charge:])
      carga[lista1] = lista3

for lista in carga:
    print(lista[-1])

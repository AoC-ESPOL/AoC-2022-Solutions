#PARTE 1
calorias = []
archivo = open("input.txt","r")
contador = 0
for line in archivo:
  linea = line.strip()
  if not linea == "":
    valor = float(linea)
    contador += valor
  else:
    calorias.append(contador)
    contador = 0
archivo.close()
print(max(calorias))

#PARTE 2

calorias.sort()
print(sum(calorias[-3:]))

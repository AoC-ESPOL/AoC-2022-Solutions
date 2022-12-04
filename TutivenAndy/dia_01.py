def algunaPalabra(palabras, frase):
    for p in palabras:
        if p in frase:
            return True

    return False
archivo=open("dia1.txt")
numeros=["1","2","3","4","5","6","7","8","9","0"]
suma=0
num=0
mayor=0
sumaTotal=0
lista=[]
for linea in archivo:
  if (algunaPalabra(numeros,linea)):
    suma+=int(linea)
  else:
    if (suma>mayor):
      mayor=suma
    num+=1
    lista.append(suma)
    suma=0
    
lista.sort()
print(lista[-1])
print(int(lista[-1])+int(lista[-2])+int(lista[-3]))
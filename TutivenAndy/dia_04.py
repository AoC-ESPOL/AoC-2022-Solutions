archivo=open("dia4.txt")
puntaje=0
puntaje2=0
puntos=0
suma=0
for linea in archivo:
  seccion1,seccion2=linea.split(",")
  inicio1,inicio2=seccion1.split("-")
  inicio3,inicio4=seccion2.split("-")
  conteo=len(range(int(inicio1),int(inicio2)+1))
  conteo2=len(range(int(inicio3),int(inicio4)+1))
  for cuenta in range(int(inicio1),int(inicio2)+1):
    if(cuenta in range(int(inicio3),int(inicio4)+1)):
      puntaje+=1
  for cuenta2 in range(int(inicio3),int(inicio4)+1):
    if(cuenta2 in range(int(inicio1),int(inicio2)+1)):
      puntaje2+=1
  if(puntaje>=1):
    puntos+=1
  elif(puntaje2>=1):
    puntos+=1
  if (puntaje==conteo2):
    suma+=1
  elif (puntaje2==conteo):
    suma+=1
  puntaje=0
  puntaje2=0
print(suma)
print(puntos)

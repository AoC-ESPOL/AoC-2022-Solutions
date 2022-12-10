archivo=open("dia2.txt")
puntaje=0
puntaje2=0
for linea in archivo:
  jugador1,jugador2=linea.split(" ")
  if (jugador1=="A" and jugador2=="X\n"):
    puntaje+=4
  elif(jugador1=="A" and jugador2=="Y\n"):
    puntaje+=8
  elif(jugador1=="A" and jugador2=="Z\n"):
    puntaje+=3
  elif(jugador1=="B" and jugador2=="X\n"):
    puntaje+=1
  elif(jugador1=="B" and jugador2=="Y\n"):
    puntaje+=5
  elif(jugador1=="B" and jugador2=="Z\n"):
    puntaje+=9
  elif(jugador1=="C" and jugador2=="X\n"):
    puntaje+=7
  elif(jugador1=="C" and jugador2=="Y\n"):
    puntaje+=2
  elif(jugador1=="C" and jugador2=="Z\n"):
    puntaje+=6
    
  if (jugador1=="A" and jugador2=="X\n"):
    puntaje2+=3
  elif(jugador1=="A" and jugador2=="Y\n"):
    puntaje2+=4
  elif(jugador1=="A" and jugador2=="Z\n"):
    puntaje2+=8
  elif(jugador1=="B" and jugador2=="X\n"):
    puntaje2+=1
  elif(jugador1=="B" and jugador2=="Y\n"):
    puntaje2+=5
  elif(jugador1=="B" and jugador2=="Z\n"):
    puntaje2+=9
  elif(jugador1=="C" and jugador2=="X\n"):
    puntaje2+=2
  elif(jugador1=="C" and jugador2=="Y\n"):
    puntaje2+=6
  elif(jugador1=="C" and jugador2=="Z\n"):
    puntaje2+=7
  
print(puntaje)
print(puntaje2)

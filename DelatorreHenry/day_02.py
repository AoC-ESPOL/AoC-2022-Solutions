#PARTE 1
oponente = ["A","B","C"]
me = ["X","Y","Z"]
opciones = ["Piedra", "Papel", "Tijera"]
valores = [1, 2 ,3]

score = 0


f = open("input.txt","r")
for line in f:
  c1, c2 = line.strip().split(" ")
  p1 = oponente.index(c1)
  p2 = me.index(c2)
  eleccion1 = opciones[p1]
  eleccion2 = opciones[p2]
  if eleccion1==eleccion2:
    condicion = 3
  elif (eleccion1=="Piedra") and (eleccion2=="Papel"):
    condicion = 6
  elif (eleccion1=="Papel") and (eleccion2=="Piedra"):
    condicion = 0
  elif (eleccion1=="Piedra") and (eleccion2=="Tijera"):
    condicion = 0
  elif (eleccion1=="Tijera") and (eleccion2=="Piedra"):
    condicion = 6
  elif (eleccion1=="Tijera") and (eleccion2=="Papel"):
    condicion = 0
  elif (eleccion1=="Papel") and (eleccion2=="Tijera"):
    condicion = 6
  formula = valores[p2] + condicion
  score += formula
f.close()

print(score)

#PARTE 2

oponente = ["A","B","C"]
valores = [1, 2 ,3]
me = ["X","Y","Z"]
condiciones = [0,3,6]
opciones = ["Piedra", "Papel", "Tijera"]

score = 0


f = open("input2.txt","r")
for line in f:
  c1, c2 = line.strip().split(" ")
  p1 = oponente.index(c1)
  p2 = me.index(c2)
  eleccion1 = opciones[p1]
  condicion = condiciones[p2]
  if c2=="Y":
    valor = valores[p1]
  elif c2=="X":
    if (eleccion1=="Papel"):
      valor = 1
    elif (eleccion1=="Piedra"):
      valor = 3
    elif (eleccion1=="Tijera"):
      valor = 2
  elif c2=="Z":
    if (eleccion1=="Piedra"):
      valor = 2
    elif (eleccion1=="Tijera"):
      valor = 1
    elif (eleccion1=="Papel"):
      valor = 3
  formula = valor + condicion
  score += formula
f.close()

print(score)

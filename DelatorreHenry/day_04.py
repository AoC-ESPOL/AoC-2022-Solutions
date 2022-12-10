#PARTE 1
contador = 0
archivo = open("entrada.txt","r")
for line in archivo:
  asignacion1, asignacion2 = line.strip().split(",")
  n1, n2 = asignacion1.strip().split("-")
  n3, n4 = asignacion2.strip().split("-")
  rango1 = list(range(int(n1),int(n2)+1))
  rango2 = list(range(int(n3),int(n4)+1))
  if((set(rango1) & set(rango2))== set(rango1)) or ((set(rango1) & set(rango2))== set(rango2)): 
    contador+= 1
archivo.close()
print(contador)

PARTE 2 
contador = 0
archivo = open("entrada.txt","r")
for line in archivo:
  asignacion1, asignacion2 = line.strip().split(",")
  n1, n2 = asignacion1.strip().split("-")
  n3, n4 = asignacion2.strip().split("-")
  rango1 = list(range(int(n1),int(n2)+1))
  rango2 = list(range(int(n3),int(n4)+1))
  estado = False
  for x in rango2:  
    if x in rango1:
      estado = True
  if estado:
    contador += 1
archivo.close()

print(contador)

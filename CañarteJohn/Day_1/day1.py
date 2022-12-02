

lCalorias = ["1000","2000","3000","","4000","","5000","6000","","7000","8000","9000","","10000"]

lCalorias2 = []

dir = "/home/john/Desktop/day1/input"

doc = open("input","r")

for l in doc:
    linea = l.strip()
    lCalorias2.append(linea)
doc.close


def elfoMasCalorias(list):
    ac = 0
    c = 1
    elfos =[]
    cal = []
    
    for i in list:
        if i != '':
            ac += int(i)
        else:
            elfos.append("Elfo"+str(c))
            c+= 1
            cal.append(ac)
            ac = 0
    indi = cal.index(max(cal))
    return "La mayor cantidad de calorias las tiene el "+elfos[indi]+" con "+str(cal[indi])+" calorias"
  

print(elfoMasCalorias(lCalorias))

print(elfoMasCalorias(lCalorias2))

        


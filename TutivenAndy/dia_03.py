
archivo=open("dia3.txt")
puntaje=0
suma=0
numero=0
suma2=0
for linea in archivo:
  numero+=1
  mitad=int(len(linea)/2)
  parte1a=linea[:mitad]
  parte2a=linea[mitad:]
  if("a" in parte1a and "a" in parte2a):
    suma+=1
  if("b" in parte1a and "b" in parte2a ):
    suma+=2
  if("c" in parte1a and "c" in parte2a ):
    suma+=3
  if("d" in parte1a and "d" in parte2a ):
    suma+=4
  if("e" in parte1a and "e" in parte2a ):
    suma+=5
  if("f" in parte1a and "f" in parte2a ):
    suma+=6
  if("g" in parte1a and "g" in parte2a ):
    suma+=7
  if("h" in parte1a and "h" in parte2a ):
    suma+=8
  if("i" in parte1a and "i" in parte2a ):
    suma+=9
  if("j" in parte1a and "j" in parte2a ):
    suma+=10
  if("k" in parte1a and "k" in parte2a ):
    suma+=11
  if("l" in parte1a and "l" in parte2a ):
    suma+=12
  if("m" in parte1a and "m" in parte2a ):
    suma+=13
  if("n" in parte1a and "n" in parte2a ):
    suma+=14
  if("o" in parte1a and "o" in parte2a ):
    suma+=15
  if("p" in parte1a and "p" in parte2a ):
    suma+=16
  if("q" in parte1a and "q" in parte2a ):
    suma+=17
  if("r" in parte1a and "r" in parte2a ):
    suma+=18
  if("s" in parte1a and "s" in parte2a ):
    suma+=19
  if("t" in parte1a and "t" in parte2a ):
    suma+=20
  if("u" in parte1a and "u" in parte2a ):
    suma+=21
  if("v" in parte1a and "v" in parte2a ):
    suma+=22
  if("w" in parte1a and "w" in parte2a ):
    suma+=23
  if("x" in parte1a and "x" in parte2a ):
    suma+=24
  if("y" in parte1a and "y" in parte2a ):
    suma+=25
  if("z" in parte1a and "z" in parte2a ):
    suma+=26
  if("A" in parte1a and "A" in parte2a ):
    suma+=27
  if("B" in parte1a and "B" in parte2a ):
    suma+=28
  if("C" in parte1a and "C" in parte2a ):
    suma+=29
  if("D" in parte1a and "D" in parte2a ):
    suma+=30
  if("E" in parte1a and "E" in parte2a ):
    suma+=31
  if("F" in parte1a and "F" in parte2a ):
    suma+=32
  if("G" in parte1a and "G" in parte2a ):
    suma+=33
  if("H" in parte1a and "H" in parte2a ):
    suma+=34
  if("I" in parte1a and "I" in parte2a ):
    suma+=35
  if("J" in parte1a and "J" in parte2a):
    suma+=36
  if("K" in parte1a and "K" in parte2a ):
    suma+=37
  if("L" in parte1a and "L" in parte2a):
    suma+=38
  if("M" in parte1a and "M" in parte2a ):
    suma+=39
  if("N" in parte1a and "N" in parte2a ):
    suma+=40
  if("O" in parte1a and "O" in parte2a ):
    suma+=41
  if("P" in parte1a and "P" in parte2a ):
    suma+=42
  if("Q" in parte1a and "Q" in parte2a):
    suma+=43
  if("R" in parte1a and "R" in parte2a):
    suma+=44
  if("S" in parte1a and "S" in parte2a ):
    suma+=45
  if("T" in parte1a and "T" in parte2a ):
    suma+=46
  if("U" in parte1a and "U" in parte2a ):
    suma+=47
  if("V" in parte1a and "V" in parte2a ):
    suma+=48
  if("W" in parte1a and "W" in parte2a ):
    suma+=49
  if("X" in parte1a and "X" in parte2a ):
    suma+=50
  if("Y" in parte1a and "Y" in parte2a ):
    suma+=51
  if("Z" in parte1a and "Z" in parte2a):
    suma+=52
  if (numero==1):
    parte1=linea
  elif(numero==2):
    parte2=linea
  elif(numero==3):
    tercero=linea
    if("a" in parte1 and "a" in parte2 and "a" in tercero):
      suma2+=1
    if("b" in parte1 and "b" in parte2 and "b" in tercero):
      suma2+=2
    if("c" in parte1 and "c" in parte2 and "c" in tercero):
      suma2+=3
    if("d" in parte1 and "d" in parte2 and "d" in tercero):
      suma2+=4
    if("e" in parte1 and "e" in parte2 and "e" in tercero):
      suma2+=5
    if("f" in parte1 and "f" in parte2 and "f" in tercero):
      suma2+=6
    if("g" in parte1 and "g" in parte2 and "g" in tercero):
      suma2+=7
    if("h" in parte1 and "h" in parte2 and "h" in tercero):
      suma2+=8
    if("i" in parte1 and "i" in parte2 and "i" in tercero):
      suma2+=9
    if("j" in parte1 and "j" in parte2 and "j" in tercero):
      suma2+=10
    if("k" in parte1 and "k" in parte2 and "k" in tercero):
      suma2+=11
    if("l" in parte1 and "l" in parte2 and "l" in tercero):
      suma2+=12
    if("m" in parte1 and "m" in parte2 and "m" in tercero):
      suma2+=13
    if("n" in parte1 and "n" in parte2 and "n" in tercero):
      suma2+=14
    if("o" in parte1 and "o" in parte2 and "o" in tercero):
      suma2+=15
    if("p" in parte1 and "p" in parte2 and "p" in tercero):
      suma2+=16
    if("q" in parte1 and "q" in parte2 and "q" in tercero):
      suma2+=17
    if("r" in parte1 and "r" in parte2 and "r" in tercero):
      suma2+=18
    if("s" in parte1 and "s" in parte2 and "s" in tercero):
      suma2+=19
    if("t" in parte1 and "t" in parte2 and "t" in tercero):
      suma2+=20
    if("u" in parte1 and "u" in parte2 and "u" in tercero):
      suma2+=21
    if("v" in parte1 and "v" in parte2 and "v" in tercero):
      suma2+=22
    if("w" in parte1 and "w" in parte2 and "w" in tercero):
      suma2+=23
    if("x" in parte1 and "x" in parte2 and "x" in tercero):
      suma2+=24
    if("y" in parte1 and "y" in parte2 and "y" in tercero):
      suma2+=25
    if("z" in parte1 and "z" in parte2 and "z" in tercero):
      suma2+=26
    if("A" in parte1 and "A" in parte2 and "A" in tercero):
      suma2+=27
    if("B" in parte1 and "B" in parte2 and "B" in tercero):
      suma2+=28
    if("C" in parte1 and "C" in parte2 and "C" in tercero):
      suma2+=29
    if("D" in parte1 and "D" in parte2 and "D" in tercero):
      suma2+=30
    if("E" in parte1 and "E" in parte2 and "E" in tercero):
      suma2+=31
    if("F" in parte1 and "F" in parte2 and "F" in tercero):
      suma2+=32
    if("G" in parte1 and "G" in parte2 and "G" in tercero):
      suma2+=33
    if("H" in parte1 and "H" in parte2 and "H" in tercero):
      suma2+=34
    if("I" in parte1 and "I" in parte2 and "I" in tercero):
      suma2+=35
    if("J" in parte1 and "J" in parte2 and "J" in tercero):
      suma2+=36
    if("K" in parte1 and "K" in parte2 and "K" in tercero):
      suma2+=37
    if("L" in parte1 and "L" in parte2 and "L" in tercero):
      suma2+=38
    if("M" in parte1 and "M" in parte2 and "M" in tercero):
      suma2+=39
    if("N" in parte1 and "N" in parte2 and "N" in tercero):
      suma2+=40
    if("O" in parte1 and "O" in parte2 and "O" in tercero):
      suma2+=41
    if("P" in parte1 and "P" in parte2 and "P" in tercero):
      suma2+=42
    if("Q" in parte1 and "Q" in parte2 and "Q" in tercero):
      suma2+=43
    if("R" in parte1 and "R" in parte2 and "R" in tercero):
      suma2+=44
    if("S" in parte1 and "S" in parte2 and "S" in tercero):
      suma2+=45
    if("T" in parte1 and "T" in parte2 and "T" in tercero):
      suma2+=46
    if("U" in parte1 and "U" in parte2 and "U" in tercero):
      suma2+=47
    if("V" in parte1 and "V" in parte2 and "V" in tercero):
      suma2+=48
    if("W" in parte1 and "W" in parte2 and "W" in tercero):
      suma2+=49
    if("X" in parte1 and "X" in parte2 and "X" in tercero):
      suma2+=50
    if("Y" in parte1 and "Y" in parte2 and "Y" in tercero):
      suma2+=51
    if("Z" in parte1 and "Z" in parte2 and "Z" in tercero):
      suma2+=52
    numero=0
print(suma)
print(suma2)
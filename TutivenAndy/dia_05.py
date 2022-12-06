#para el ejercicio 1 solo se tenia que cambiar la condicion del if, elif y las letras solo serian 4
letra1="b"
letra2="b"
letra3="b"
letra4="b"
letra5="b"
letra6="b"
letra7="b"
letra8="b"
letra9="b"
letra10="b"
letra11="b"
letra12="b"
letra13="b"
letra14="b"
cont=0
suma=0
archivo=open("dia6.txt")
for linea in archivo:
  
  for a in linea:
    cont+=1
    if(cont==1):
      letra1=a
      suma+=1
    elif(cont==2):
      letra2=a
      suma+=1
    elif (cont==3):
      letra3=a
      suma+=1
    elif(cont==4):
      letra4=a
      suma+=1
    elif(cont==5):
      letra5=a
      suma+=1
    elif (cont==6):
      letra6=a
      suma+=1
    elif(cont==7):
      letra7=a
      suma+=1
    elif(cont==8):
      letra8=a
      suma+=1
    elif (cont==9):
      letra9=a
      suma+=1
    elif(cont==10):
      letra10=a
      suma+=1
    elif(cont==11):
      letra11=a
      suma+=1
    elif (cont==12):
      letra12=a
      suma+=1
    elif(cont==13):
      letra13=a
      suma+=1
    elif(cont==2):
      letra2=a
      suma+=1
    elif (cont==3):
      letra3=a
      suma+=1
    elif(cont==14):
      letra14=a
      suma+=1
      cont=0
    if(letra1!=letra2 and letra1!=letra3 and letra1!=letra4 and letra1!=letra5 and letra1!=letra6 and letra1!=letra7 and letra1!=letra8 and letra1!=letra9 and letra1!=letra10 and letra1!=letra11 and letra1!=letra12 and letra1!=letra13 and letra1!=letra14 and letra2!=letra3 and letra2!=letra4 and letra2!=letra5 and letra2!=letra6 and letra2!=letra7 and letra2!=letra8 and letra2!=letra9 and letra2!=letra10 and letra2!=letra11 and letra2!=letra12 and letra2!=letra13 and letra2!=letra14 and letra3!=letra4 and letra3!=letra5 and letra3!=letra6 and letra3!=letra7 and letra3!=letra8 and letra3!=letra9 and letra3!=letra10 and letra3!=letra11 and letra3!=letra12 and letra3!=letra13 and letra3!=letra14 and letra4!=letra5 and letra4!=letra6 and letra4!=letra7 and letra4!=letra8 and letra4!=letra9 and letra4!=letra10 and letra4!=letra11 and letra4!=letra12 and letra4!=letra13 and letra4!=letra14 and letra5!=letra6 and letra5!=letra7 and letra5!=letra8 and letra5!=letra9 and letra5!=letra10 and letra5!=letra11 and letra5!=letra12 and letra5!=letra13 and letra5!=letra14 and letra6!=letra7 and letra6!=letra8 and letra6!=letra9 and letra6!=letra10 and letra6!=letra11 and letra6!=letra12 and letra6!=letra13 and letra6!=letra14 and letra7!=letra8 and letra7!=letra9 and letra7!=letra10 and letra7!=letra11 and letra7!=letra12 and letra7!=letra13 and letra7!=letra14 and letra8!=letra9 and letra8!=letra10 and letra8!=letra11 and letra8!=letra12 and letra8!=letra13 and letra8!=letra14 and letra9!=letra10 and letra9!=letra11 and letra9!=letra12 and letra9!=letra13 and letra9!=letra14 and letra10!=letra11 and letra10!=letra12 and letra10!=letra13 and letra10!=letra14 and letra11!=letra12 and letra11!=letra13 and letra11!=letra14 and letra12!=letra13 and letra12!=letra14 and letra13!=letra14):
      break
      
print(suma)
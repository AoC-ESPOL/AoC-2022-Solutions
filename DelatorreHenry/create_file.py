
for i in range(1,26):
    if i<10:
        file_name = "day_0"+str(i)+".py"
    else:
        file_name = "day_"+str(i)+".py"
    file = open(file_name,"w")
    file.write('with open("'+file_name[:-3]+".txt"+'") as file:\n')
    file.write('    contenido = file.read()\n')

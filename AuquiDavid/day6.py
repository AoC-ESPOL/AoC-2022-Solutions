#David Auqui

#DAY 6
#-- PART ONE --
file = open("input.txt")
lines = file.readlines()
file.close()

counter=0
cont = 4
for i in lines[0][3:]:
    block = 0
    list = lines[0][cont-4:cont]
    for j in list:
        times = list.count(j)
        if times != 1:
            block = 1
    if block == 1:
        cont+=1
    elif block == 0:
        counter=cont
print("-- DAY ONE --")
print(counter)

#-- PART TWO --
counter=0
cont = 14
for i in lines[0][14:]:
    block = 0
    list = lines[0][cont-14:cont]
    for j in list:
        times = list.count(j)
        if times != 1:
            block = 1
    if block == 1:
        cont+=1
    elif block == 0:
        counter=cont
print("\n-- DAY TWO --")
print(counter)

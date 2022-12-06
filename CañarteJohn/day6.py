
doc = open('/home/john/Desktop/input','r')

test = [1,2,3,4,5,6,7,7]


def findS(file):
    l=file.readline().strip()
    i=0
    j=3
    flag = True
    while (flag):
        packet = set(l[i:j+1])
        if(len(packet) == 4):
            return j + 1
        i += 1
        j += 1

def findM(file):
    l=file.readline().strip()
    i=0
    j=13
    flag = True
    while (flag):
        packet = set(l[i:j+1])
        if(len(packet) == 14):
            return j + 1
        i += 1
        j += 1

#print('Se procesaron: ' +str(findS(doc)) + ' caracteres')
print('Se procesaron: ' +str(findM(doc)) + ' caracteres')
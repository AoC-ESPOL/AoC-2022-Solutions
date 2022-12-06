
doc = open('/home/john/Desktop/input','r')


c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []
c8 = []
c9 = []
crates =[c1,c2,c3,c4,c5,c6,c7,c8,c9]


def searchHeader(file):
    flag = True
    while (flag):
        l = file.readline().replace(' ',"0").strip('\n')
        if l.isdigit():
            flag = False
    file.seek(0)
    return l


def searchCrate(c):
    for i in range (1,10):
        if c == str(i):
            return crates[i-1]


def loadCrates(file):
    header = searchHeader(file)
    l=''
    while (l != header):
        p = 0
        l = file.readline().replace(' ','0').strip('\n') 
        for c in l:
            if(c.isalpha()):
                searchCrate(header[p]).append(c)
            p += 1
                  
                 
    file.readline()


def movCrates(file):
    for c in crates:
        c.reverse()
    for l in file:
        line = l.strip().split(' ')
        for i in range(int(line[1])):         
            searchCrate(line[5]).append(searchCrate(line[3]).pop())

def topCrates(list):  
    l = []
    for c in crates:
        l.append(c.pop())
    return "".join(l)

def topCrates9001(list):
    l = []
    for c in crates:
        l.append(c[0])
    return "".join(l)

def movCrates9001(file):
    
    for l in file:
        line = l.strip().split(' ')
        searchCrate(line[5])[0:0] = searchCrate(line[3])[:int(line[1])]
        searchCrate(line[3])[:int(line[1])] = []
        


loadCrates(doc)
#movCrates(doc)
movCrates9001(doc)
#print('Las cajas en el top son:' + topCrates(crates))
print('Las cajas en la cima son:' + topCrates9001(crates))




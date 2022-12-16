lines = [line.strip() for line in open('day10.in')]

s1 = 0
x = 1
cicles = 0
list = [20,60,100,140,180,220,260]

for i in range(len(lines)):
    if lines[i]!="noop":
        _, ct = lines[i].split()
        cicles +=1
        if cicles in list:
            s1 = s1+(x*cicles)
        cicles +=1
        if cicles in list:
            s1 = s1+(x*cicles)
        x += int(ct)
    else:
        cicles +=1
        if cicles in list:
            s1 = s1+(x*cicles)
print(s1)
x = 1
cicles = 0
mat = [['x']*40,['x']*40,['x']*40,['x']*40,['x']*40,['x']*40]
for i in range(len(lines)):
    if lines[i]!="noop":
        _, ct = lines[i].split()
        cicles +=1
        chr = "."
        if not(abs(x-((cicles-1)%40)))>1:
            chr = "#"
        mat[(cicles-1)//40][(cicles-1)%40] = chr  
        cicles +=1
        chr = "."
        if not(abs(x-((cicles-1)%40)))>1:
            chr = "#"
        mat[(cicles-1)//40][(cicles-1)%40] = chr  
        x += int(ct)
    else:
        cicles +=1
        chr = "."
        if not(abs(x-((cicles-1)%40)))>1:
            chr = "#"
        mat[(cicles-1)//40][(cicles-1)%40] = chr  

s2 = ["".join(mat[i]) for i in [0,1,2,3,4,5]]
print("\n".join(s2))


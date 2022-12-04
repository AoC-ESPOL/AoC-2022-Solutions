lines = [line for line in open('day4.in')]
s1 = 0
s2 = 0
for line in lines:
    line = line.strip()
    x,y = line.split(',')
    x1,x2 = [int(x) for x in x.split("-")]
    y1,y2 = [int(y) for y in y.split("-")]
    if x1<=y1 and x2>=y2 or y1<=x1 and y2>=x2:
        s1+=1
    if y1<=x2 and y2>=x1:
        s2+=1 
print(s1)
print(s2)
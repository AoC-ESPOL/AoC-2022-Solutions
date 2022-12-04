lines = [line for line in open('day4.in')]
s1 = 0
s2 = 0
for line in lines:
    line = line.strip()
    x,y = line.split(',')
    x = x.split("-")
    y = y.split("-")
    if int(x[0]) <= int(y[0]) and int(y[1]) >= int(y[1]) or int(x[0]) >= int(y[0]) and int(x[1]) <= int(y[1]):
        s1+=1
    if int(y[0]) <= int(x[1]) and int(y[1]) >= int(x[0]):
        s2+=1 
print(s1)
print(s2)
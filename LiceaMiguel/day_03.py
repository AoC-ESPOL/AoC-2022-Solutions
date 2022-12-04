lettermin = lambda chr : 'a'<=chr<='z'
pointsMin = lambda chr : ord(chr)-ord('a') + 1
pointsMay = lambda chr : ord(chr)-ord('A') + 27

s1 = 0
for line in open('day3.in'):
    flag = True
    line = line.strip()
    p1,p2 = line[:len(line)//2],line[len(line)//2:]
    for chr in p1:
        if flag and (chr in p2):
            s1 += pointsMin(chr) if lettermin(chr) else pointsMay(chr)
            flag = False

s2 = 0
lines = [line for line in open('day3.in')]
idx = 0
while len(lines) > idx:
    flag = True
    for chr in lines[idx]:
        after = chr in lines[idx+1]
        afterafter = chr in lines[idx+2]
        if  after and afterafter and flag:
            s2 += pointsMin(chr) if lettermin(chr) else pointsMay(chr)
            flag = False
    idx +=3
print(s1)
print(s2)
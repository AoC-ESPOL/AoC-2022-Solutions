lines = [line for line in open('day25.in').read().splitlines()]

conversion = {'0':0,'1':1,'2':2,'-':-1,'=':2}

def from_snafu(s):
    n,mul = 0,1
    for d in s[::-1]:
        n+=conversion[d]*mul
        mul *=5
    return n
    
def to_snafu(num):
    s1 = ''
    while num > 0:
        num, place = divmod(num + 2, 5)
        s1 += '=-012'[place]
    return s1

sum = sum([from_snafu(line) for line in lines])
print(to_snafu(sum))
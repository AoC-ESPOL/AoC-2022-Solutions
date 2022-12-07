line = open('day6.in').read()

def find(line, before, rang):
    flag = False
    for i in range(len(line)):
        if (not flag) and i-before>=0 and len(set([line[i-j] for j in range(rang)]))==rang:
            return i+1

print(find(line,3,4))
print(find(line,13,14))
        
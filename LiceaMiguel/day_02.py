fr1 = {'X': 1, 'Y': 2, 'Z': 3}
sr1 = {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
        ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
        ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3}

fr2 = {'X': 0, 'Y': 3, 'Z': 6}
sr2 = {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
        ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
        ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1}

def round(opponent, me, fdict, sdict):
    p = 0
    p += fdict[me]
    p += sdict[(opponent, me)]
    return p

pr1 = 0
pr2 = 0
lines = [line for line in open('day2.in')]
for line in lines:
        line = line.strip()
        opponent, me = line.split()
        pr1 += round(opponent, me, fr1, sr1)
        pr2 += round(opponent, me, fr2, sr2)
print(pr1)
print(pr2)
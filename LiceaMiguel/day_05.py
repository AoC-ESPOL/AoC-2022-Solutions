from copy import deepcopy
lines = [line for line in open('day5.in')]
lines = lines[10:]

map1 = {
    1 : ["P","G","R","N"],
    2: ["C","D","G","F","L","B","T","J"],
    3 : ["V","S","M"],
    4 : ["P","Z","C","R","S","L"],
    5 : ["Q","D","W","C","V","L","S","P"],
    6 : ["S","M","D","W","N","T","C"],
    7 : ["P","W","G","D","H"],
    8 :["V","M","C","S","H","P","L","Z"],
    9 : ["Z","G","W","L","F","P","R"],
}

map2 = deepcopy(map1)


def movement(map,string, reverse=False):
    line = string.split("from")
    stacks = line[1].split("to")
    f,s = [int(stack.strip()) for stack in stacks]
    c = int(line[0].split(" ")[1])
    elements = []
    elements.extend(map[f][:c])
    elements = elements[::-1] if reverse else elements
    map[f]=map[f][c:]
    elements.extend(map[s])
    map[s] = elements
    
for line in lines:
    movement(map1,line,True)
    movement(map2,line)
s1 = ""
s2 = ""
for v,v2 in map1.values(),map2.values():
    s1+=v[0]

for v in map2.values():
    s2+=v[0]

print(s1)
print(s2)

lines = [line for line in open('day5.in')]
# lines = [line for line in open('day5test.in')]

map = {
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

# map = {
#     1:["N","Z"],
#     2:["D","C","M"],
#     3:["P"]
# }



lines = lines[10:]

def movement(map,string):
    line = string.split("from")
    stacks = line[1].split("to")
    f,s = [int(stack.strip()) for stack in stacks]
    c = int(line[0].split(" ")[1])
    elements = []
    elements.extend(map[f][:c])
    elements = elements[::-1]
    map[f]=map[f][c:]
    elements.extend(map[s])
    map[s] = elements
for line in lines:
    movement(map,line)
s1 = ""
for v in map.values():
    s1+=v[0]
print(s1)



def movement2(map,string):
    line = string.split("from")
    stacks = line[1].split("to")
    f,s = [int(stack.strip()) for stack in stacks]
    c = int(line[0].split(" ")[1])
    elements = []
    elements.extend(map[f][:c])
    map[f]=map[f][c:]
    elements.extend(map[s])
    map[s] = elements
map = {
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
for line in lines:
    movement2(map,line)
s2 = ""
for v in map.values():
    s2+=v[0]
print(s2)

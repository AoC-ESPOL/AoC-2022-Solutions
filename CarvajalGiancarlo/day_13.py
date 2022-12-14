print("\n¡AoC! - Day 13\n")

import ast

print('Part One')

file = open('input_day_13.txt', 'r')

packets = list(map(lambda x: ast.literal_eval(x.replace('\n', '')), filter(lambda x: x != '\n', file.readlines())))

def compare(listOne, listTwo):
    if isinstance(listOne, int) and isinstance(listTwo, int):
        if listTwo == listOne:
            return None
        return listTwo > listOne

    listOne = listOne if isinstance(listOne, list) else [listOne]
    listTwo = listTwo if isinstance(listTwo, list) else [listTwo]

    left_len = len(listOne)
    right_len = len(listTwo)

    for n in range(0, max(left_len, right_len)):
        if n > left_len - 1 and n <= right_len - 1:
            return True
        if n <= left_len - 1 and n > right_len - 1:
            return False
        comparison = compare(listOne[n], listTwo[n])
        if comparison == None:
            continue
        return comparison

result = 0

for n in range(0, len(packets) - 1, 2):
    if(compare(packets[n], packets[n+1])):
       result += (n//2 + 1)

print(f'Answer: {result}\n')

print('Part Two')

sorted_packets = [packets[0]]

def addPacket(packet):
    for n, p in enumerate(sorted_packets):
        if(compare(packet, p)):
            sorted_packets.insert(n, packet)
            return n

    sorted_packets.append(packet)
    return len(sorted_packets)


for n, p in enumerate(packets, 1):
    addPacket(p)

print(f'Answer: {addPacket([[2]]) * addPacket([[6]])}\n')
from collections import deque
from copy import deepcopy

lines = [line for line in open('day24.in').read().splitlines()]
flag_s1 = False

x = 0
while lines[0][x] == '#':
    x+=1

chars = ['>', 'v', '<', '^']

def replace_tuple_values(source, idx, new):
    return source[0:idx]+type(source)((new,))+source[idx+1:]

# matrix len
rows_len = len(lines)
columns_len = len(lines[0])

obstacles = {}
for i in range(1+(rows_len-2)*(columns_len-2)):
    obstacle_by_i = []
    for row in range(rows_len):
        for col in range(columns_len):
            lambda_matches = ['obstacle_by_i.append((row, 1+((col-1+i)%(columns_len-2))))','obstacle_by_i.append(((1+((row-1+i)%(rows_len-2))), col))','obstacle_by_i.append((row, 1+((col-1-i)%(columns_len-2))))','obstacle_by_i.append(((1+((row-1-i)%(rows_len-2))), col))']
            dict_matchs = zip(chars, lambda_matches)
            lambda_match = dict_matchs[(lines[row][col])]
            eval(lambda_match)()
    obstacles[i] = set(obstacle_by_i)

visited = set()
paths = deque([(0, x, 0, (False,False))])
obstacles_by_i = set()     
while paths:
    item = paths.popleft()
    if not(lines[item[0]][item[1]]!='#' and 0<=item[0]<rows_len and 0<=item[1]<columns_len):
        continue
    if item[0]==rows_len-1 and item[-2] and item[-1]:
        print(item[2])
        break
    if item[0]==rows_len-1 and (not flag_s1):
        print(item[2])
        flag_s1 = True
    item[-2] = True if item[0]==rows_len-1 else item[-2]
    item[-1] = True if item[0] and item[-2] else item[-1]
    if item in visited:
        continue
    visited.add(item)
    sub_item = (item[0],item[1])
    if sub_item not in obstacles[item[2]+1]:
        item_copy = deepcopy(item)
        paths.append(replace_tuple_values(item_copy,2,item_copy[2]+1))
    if (sub_item[0]+1,sub_item[1]) not in obstacles[item[2]+1]:
        item_copy = replace_tuple_values(deepcopy(item),0,item[0]+1)
        paths.append(replace_tuple_values(item_copy,2,item_copy[2]+1))
    if (sub_item[0]-1,sub_item[1]) not in obstacles[item[2]+1]:
        item_copy = replace_tuple_values(deepcopy(item),0,item[0]-1)
        paths.append(replace_tuple_values(item_copy,2,item_copy[2]+1))
    if (sub_item[0],sub_item[1]+1) not in obstacles[item[2]+1]:
        item_copy = replace_tuple_values(deepcopy(item),1,item[1]+1)
        paths.append(replace_tuple_values(item_copy,2,item_copy[2]+1))
    if (sub_item[0],sub_item[1]-1) not in obstacles[item[2]+1]:
        item_copy = replace_tuple_values(deepcopy(item),1,item[1]-1)
        paths.append(replace_tuple_values(item_copy,2,item_copy[2]+1))
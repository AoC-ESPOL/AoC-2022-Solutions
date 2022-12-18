from collections import deque
lines = [line for line in open('day18.in').read().split("\n")]

cubes_set = set()
for line in lines:
    x,y,z = [int(d) for d in line.split(',')]
    cubes_set.add((x,y,z))

def out_1(x,y,z):
    visited.clear()
    cube = (x,y,z)
    if cube in inside:
        return False
    elif cube in outside:
        return True
    queue_cube = [cube]
    d = deque(queue_cube)
    while d:
        cube = d.popleft()
        if cube in cubes_set or cube in visited:
            continue
        visited.add(cube)
        if len(visited)>0:
            for cube in visited:
                outside.add(cube)
            return True
        directions = [(x+1,y,z),(x,y+1,z),(x,y,z+1),
                    (x-1,y,z), (x,y-1,z), (x,y,z-1)]
        for direct in directions:
            d.append(direct)
        for direct in directions:
            d.append(direct)
    inside = tuple(list(inside)+list(visited))
    return False


s1 = 0
inside, outside, visited = set(),set(),set()
for cube in cubes_set:
    (x,y,z) = cube
    answers = [out_1(x+1,y,z),
        out_1(x,y+1,z), out_1(x,y,z+1),
        out_1(x-1,y,z), out_1(x,y-1,z),
        out_1(x,y,z-1)]
    s1+= sum(answers)

def out_2(x,y,z):
    visited.clear()
    cube = (x,y,z)
    if cube in inside:
        return False
    elif cube in outside:
        return True
    queue_cube = [cube]
    d = deque(queue_cube)
    while d:
        cube = d.popleft()
        if cube in cubes_set or cube in visited:
            continue
        visited.add(cube)
        if len(visited)>5000:
            for cube in visited:
                outside.add(cube)
            return True
        directions = [(x+1,y,z),(x,y+1,z),(x,y,z+1),
                    (x-1,y,z), (x,y-1,z), (x,y,z-1)]
        for direct in directions:
            d.append(direct)
        for direct in directions:
            d.append(direct)
    inside = tuple(list(inside)+list(visited))
    return False

print(s1)
inside, outside, visited = set(),set(),set()

s2 = 0
for cube in cubes_set:
    (x,y,z) = cube
    answers = [out_2(x+1,y,z),
        out_2(x,y+1,z), out_2(x,y,z+1),
        out_2(x-1,y,z), out_2(x,y-1,z),
        out_2(x,y,z-1)]
    s2+= sum(answers)
print(s2)
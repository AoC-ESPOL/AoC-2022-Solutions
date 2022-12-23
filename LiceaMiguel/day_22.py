lines = [x for x in open('day22.in').read().rstrip().split('\n')]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
characters = [">", "v", "<", "^"]
obstacle_board = [list(x) for x in lines[:-2]]

def fill_obstacle_board():
    for l in obstacle_board:
        while len(l) < max([len(x) for x in obstacle_board]):
            l.append(" ")

def init_index(obstacle_board):# if i need to start 
    return (0, obstacle_board[0].index("."))

fill_obstacle_board()
actual_pos = init_index(obstacle_board)
actual_dr = (0, 1)

movements = lines[-1].replace("L", " L ").replace("R", " R ")


def compute_coord(actual_pos, actual_dr):
    if len(actual_pos) == 2:
        return (actual_pos[0] + actual_dr[0], actual_pos[1] + actual_dr[1])
    return tuple(map(sum, zip(actual_pos, actual_dr)))

def directions_index0(x):
    if x[0] in range(0, 50):
        return ((- x[0] + 149, 99), (0, -1))
    elif x[0] in range(50, 100):
        return ((49, x[0] + 50), (-1, 0))
    elif x[0] in range(100, 150):
        return ((149 - x[0], 149), (0, -1))
    elif x[0] in range(150, 200):
        return ((149, x[0] - 100), (-1, 0))

def directions_index1(x):
    if x[1] in range(0, 50):
        return ((0, x[1] + 100), (1, 0))
    elif x[1] in range(50, 100):
        return ((100 + x[1], 49), (0, -1))
    elif x[1] in range(100, 150):
        return ((x[1] - 50, 99), (0, -1))

def directions_index2(x):
    if x[0] in range(0, 50):
        return ((- x[0] + 149, 0), (0, 1))
    elif x[0] in range(50, 100):
        return ((100, x[0] - 50), (1, 0))
    elif x[0] in range(100, 150):
        return ((149 - x[0], 50), (0, 1))
    elif x[0] in range(150, 200):
        return ((0, x[0] - 100), (1, 0))

def directions_index3(x):
    if x[1] in range(0, 50):
        return ((x[1] + 50, 50), (0, 1))
    elif x[1] in range(50, 100):
        return ((100 + x[1], 0), (0, 1))
    elif x[1] in range(100, 150):
        return ((199, x[1] - 100), (-1, 0))

def cube_movement(actual_pos, actual_dr):
    x = compute_coord(actual_pos, actual_dr)
    if x[0] in range(len(obstacle_board)) and x[1] in range(len(obstacle_board[0])) and obstacle_board[x[0]][x[1]] != " ":
        return (x, actual_dr)
    elif actual_dr == directions[0]:
        return directions_index0(x)
    elif actual_dr == directions[1]:
        return directions_index1(x)
    elif actual_dr == directions[2]:
        return directions_index2(x)
    elif actual_dr == directions[-1]:
        return directions_index3(x)

for movement in movements.split(" "):
    if movement == "R":
        actual_dr = directions[(directions.index(actual_dr) + 1) % 4]
    elif movement == "L":
        actual_dr = directions[(directions.index(actual_dr) + 3) % 4]
    else:
        for i in range(int(movement)):
            next_pos, next_dr = cube_movement(actual_pos, actual_dr)
            next_x, next_x = next_pos
            if obstacle_board[next_x][next_x] == ".":
                actual_pos,actual_dr = next_pos, next_dr

print(sum([1000 * (actual_pos[0]+1),
           4 * (actual_pos[1] + 1),
           directions.index(actual_dr)]))

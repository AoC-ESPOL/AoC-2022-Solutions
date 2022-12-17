import numpy as np

def get_data(file):
    try:
        with open(file, 'r') as file:
            lines  = file.readlines()
            grid = []
            for line in lines:
                arrow = []
                for i in list(line.strip()):
                    arrow.append(int(i))
                grid.append(arrow)
            return grid
    except FileNotFoundError:
        print('File not found')

# x: row, y: column
def isVisible(x, y, grid):
    visible = False

    element = grid[x,y]
    fila = grid[x,:]

    left = fila[:y]

    if left.size > 0:
        to_the_left = list(filter(lambda left_element: left_element >= element, left))
        visible = visible or not to_the_left

    rigth = fila[y+1:]
    if rigth.size > 0:
        to_the_rigth = list(filter(lambda rigth_element: rigth_element >= element, rigth))
        visible = visible or not to_the_rigth

    columna = grid[:,y].transpose()

    top = columna[:x]
    if top.size > 0:
        to_the_top = list(filter(lambda top_element: top_element >= element, top))
        visible = visible or not to_the_top

    bottom = columna[x+1:]
    if bottom.size > 0:
        to_the_bottom = list(filter(lambda bottom_element: bottom_element >= element, bottom))
        visible = visible or not to_the_bottom

    return visible

def count_visible_trees(grid):

    grid = np.array(grid)
    # considerar bordes
    borders = 2 * (len(grid[:,0]) + len(grid[0,:])) - 4
    # internal_grid = grid[1:-1, 1:-1]


    count = 0
    count += borders

    for arrow in range(1, len(grid[:,0]) - 1):
        for column in range(1, len(grid[0,:]) - 1):
            # Descartar árbol con altura 0?
            # if grid[arrow, column]:
            if isVisible(arrow, column, grid):
                count += 1
    return count


def get_scenic_score(x, y, grid):
    scenic_score = 1

    element = grid[x, y]

    fila = grid[x, :]

    left = fila[:y]

    to_the_left = 0
    for i in left[::-1]:
        to_the_left += 1
        if i >= element:
            break
    if to_the_left:
        scenic_score *= to_the_left


    rigth = fila[y + 1:]
    to_the_rigth = 0
    for i in rigth:
        to_the_rigth += 1
        if i >= element:
            break

    if to_the_rigth:
        scenic_score *= to_the_rigth


    columna = grid[:, y].transpose()

    top = columna[:x]
    to_the_top = 0
    for i in top[::-1]:
        to_the_top += 1
        if i >= element:
            break

    if to_the_top:
        scenic_score *= to_the_top


    bottom = columna[x + 1:]
    to_the_bottom= 0
    for i in bottom:
        to_the_bottom += 1
        if i >= element:
            break

    if to_the_bottom:
        scenic_score *= to_the_bottom

    return scenic_score

def get_best_tree(grid):
    best = 0
    grid = np.array(grid)

    for arrow in range(len(grid[:, 0])):
        for column in range(len(grid[0, :])):
            score = get_scenic_score(arrow, column, grid)
            if score > best:
                best = score
    return best

# PART 1
print(count_visible_trees(get_data("input.txt")))

# PART 2
print(get_best_tree(get_data("input.txt")))

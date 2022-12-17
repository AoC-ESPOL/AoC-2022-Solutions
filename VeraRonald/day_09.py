def execute_series_of_motions(file):
    try:
        with open(file, 'r') as file:
            lines  = file.readlines()

            positions = {
                "s": [0, 0],
                "H": [0, 0],
                "T": [0, 0],
            }

            visited_positions_tail = {tuple(positions["T"])}

            for line in lines:

                line = line.strip()
                direction, size = line.split()

                for i in range(int(size)):
                    new_positions = move(positions, direction)

                    for key, value in new_positions.items():
                        positions[key] = value

                    visited_positions_tail.add(tuple(positions["T"]))

            return visited_positions_tail
    except FileNotFoundError:
        print('File not found')

def move(positions, direction):
    new_positions = {"H": positions["H"], "T":positions["T"]}

    motion = define_motion(direction)

    if direction == "L" or direction == "R":
        new_positions["H"][0] += motion
    else:
        new_positions["H"][1] += motion

    if not are_they_touching(positions):

        # En la misma fila? avance horizontal
        if new_positions["H"][0] == new_positions["T"][0]:
            if new_positions["T"][1] < new_positions["H"][1]:
                new_positions["T"][1] += define_motion("R")
            else:
                new_positions["T"][1] += define_motion("L")
        # En la misma columna? avance vertical
        elif new_positions["H"][1] == new_positions["T"][1]:
            if new_positions["T"][0] < new_positions["H"][0]:
                new_positions["T"][0] += define_motion("U")
            else:
                new_positions["T"][0] += define_motion("D")
        # Ninguna? avance diagonal
        else:
            # arriba <-> derecha
            if (new_positions["H"][0] == new_positions["T"][0]+1 and
                new_positions["H"][1] == new_positions["T"][1]+2) or \
                    (new_positions["H"][0] == new_positions["T"][0]+2 and
                     new_positions["H"][1] == new_positions["T"][1]+1):
                new_positions["T"][1] += 1
                new_positions["T"][0] += 1
            # abajo <-> derecha
            elif (new_positions["H"][0] == new_positions["T"][0]+2  and
                  new_positions["H"][1] == new_positions["T"][1]-1) or \
                    (new_positions["H"][0] == new_positions["T"][0]+1 and
                     new_positions["H"][1] == new_positions["T"][1]-2):
                new_positions["T"][1] -= 1
                new_positions["T"][0] += 1
            # abajo <-> izquierda
            if (new_positions["H"][0] == new_positions["T"][0]-1  and
                  new_positions["H"][1] == new_positions["T"][1]-2) or \
                    (new_positions["H"][0] == new_positions["T"][0]-2 and
                     new_positions["H"][1] == new_positions["T"][1]-1):
                new_positions["T"][1] -= 1
                new_positions["T"][0] -= 1
            # arriba <-> izquierda
            if (new_positions["H"][0] == new_positions["T"][0]-2  and
                  new_positions["H"][1] == new_positions["T"][1]+1) or \
                    (new_positions["H"][0] == new_positions["T"][0]-1 and
                     new_positions["H"][1] == new_positions["T"][1]+2):
                new_positions["T"][1] += 1
                new_positions["T"][0] -= 1

    return new_positions

def define_motion(direction):
    if direction == "L" or direction == "D":
        return -1
    else:
        return 1

def are_they_touching(positions):
    touching = False

    grid = [
        [(positions["H"][0] - 1 , positions["H"][1] + 1), (positions["H"][0], positions["H"][1] + 1), (positions["H"][0] + 1 , positions["H"][1] + 1)],
        [(positions["H"][0] - 1, positions["H"][1]), (positions["H"][0], positions["H"][1]), (positions["H"][0] + 1, positions["H"][1])],
        [(positions["H"][0] - 1 , positions["H"][1] -1), (positions["H"][0], positions["H"][1] - 1), (positions["H"][0] + 1 , positions["H"][1] - 1)],
    ]

    for arrow in range(3):
        for column in range(3):
            position = grid[arrow][column]
            if position == tuple(positions["T"]):
                touching = True
                break

    return touching

# PART 1
print(len(execute_series_of_motions("input.txt")))
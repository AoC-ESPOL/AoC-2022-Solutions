def execute_series_of_motions(file, knots_number):
    try:
        with open(file, 'r') as file:
            lines  = file.readlines()

            # start
            s = [0, 0]

            positions = {
                "H": [0, 0],
                "T": [0, 0],
            }

            visited_positions_tail = {tuple(positions["T"])}

            temporary_positions = [[s, s] for i in range(knots_number-1)]

            for line in lines:

                line = line.strip()
                direction, size = line.split()

                for i in range(int(size)):
                    for j in range(knots_number - 1):

                        positions["H"] = temporary_positions[j][0]
                        positions["T"] = temporary_positions[j][1]

                        if j == 0:
                            new_positions = give_initial_move(positions.copy(), direction)
                            for key, value in new_positions.items():
                                positions[key] = value

                        new_positions = move(positions.copy())
                        for key, value in new_positions.items():
                            positions[key] = value.copy()

                        temporary_positions[j] = [positions["H"], positions["T"]]

                        if j != len(range(knots_number - 1)) - 1:
                            temporary_positions[j + 1][0] = temporary_positions.copy()[j][1]

                    visited_positions_tail.add(tuple(positions["T"]))

            return visited_positions_tail
    except FileNotFoundError:
        print('File not found')

def give_initial_move(positions, direction):
    new_positions = {"H": positions["H"].copy(), "T": positions["T"].copy()}
    # print("1", new_positions, end=" ")
    motion = define_motion(direction)

    if direction == "L" or direction == "R":
        new_positions["H"][0] += motion
    else:
        new_positions["H"][1] += motion

    # print("2", new_positions, end=" ")
    return new_positions


def move(positions):
    new_positions = positions.copy()

    if not are_they_touching(new_positions):
        new_positions = correct_separation_distance(new_positions)

    # print("3", new_positions)

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

def correct_separation_distance(updated_positions):

    new_positions = updated_positions.copy()

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
        if (new_positions["H"][0] == new_positions["T"][0] + 1 and
            new_positions["H"][1] == new_positions["T"][1] + 2) or \
                (new_positions["H"][0] == new_positions["T"][0] + 2 and
                 new_positions["H"][1] == new_positions["T"][1] + 1) or \
                    (new_positions["H"][0] == new_positions["T"][0] + 2 and
                     new_positions["H"][1] == new_positions["T"][1] + 2):
            new_positions["T"][1] += 1
            new_positions["T"][0] += 1
        # abajo <-> derecha
        elif (new_positions["H"][0] == new_positions["T"][0] + 2 and
              new_positions["H"][1] == new_positions["T"][1] - 1) or \
                (new_positions["H"][0] == new_positions["T"][0] + 1 and
                 new_positions["H"][1] == new_positions["T"][1] - 2) or \
                    (new_positions["H"][0] == new_positions["T"][0] + 2 and
                     new_positions["H"][1] == new_positions["T"][1] - 2):
            new_positions["T"][1] -= 1
            new_positions["T"][0] += 1
        # abajo <-> izquierda
        if (new_positions["H"][0] == new_positions["T"][0] - 1 and
            new_positions["H"][1] == new_positions["T"][1] - 2) or \
                (new_positions["H"][0] == new_positions["T"][0] - 2 and
                 new_positions["H"][1] == new_positions["T"][1] - 1) or \
                    (new_positions["H"][0] == new_positions["T"][0] - 2 and
                     new_positions["H"][1] == new_positions["T"][1] - 2):
            new_positions["T"][1] -= 1
            new_positions["T"][0] -= 1
        # arriba <-> izquierda
        if (new_positions["H"][0] == new_positions["T"][0] - 2 and
            new_positions["H"][1] == new_positions["T"][1] + 1) or \
                (new_positions["H"][0] == new_positions["T"][0] - 1 and
                 new_positions["H"][1] == new_positions["T"][1] + 2) or \
                    (new_positions["H"][0] == new_positions["T"][0] - 2 and
                     new_positions["H"][1] == new_positions["T"][1] + 2):
            new_positions["T"][1] += 1
            new_positions["T"][0] -= 1

    return new_positions

# PART 1
print(len(execute_series_of_motions("input.txt", 2)))

# PART 2
print(len(execute_series_of_motions("input.txt", 10)))
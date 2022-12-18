def check_cube(cube, cubes):
    exposed = 6
    for other in cubes:
        if cube == other:
            continue
        else:
            if (
                (
                    abs(cube[0] - other[0]) == 1
                    and cube[1] == other[1]
                    and cube[2] == other[2]
                )
                or (
                    abs(cube[1] - other[1]) == 1
                    and cube[0] == other[0]
                    and cube[2] == other[2]
                )
                or (
                    abs(cube[2] - other[2]) == 1
                    and cube[1] == other[1]
                    and cube[0] == other[0]
                )
            ):
                exposed -= 1

    return exposed


def part_one(cubes):
    sides = 0

    for cube in cubes:
        sides += check_cube(cube, cubes)

    return sides


def part_two(cubes):
    min_x = 10000000
    min_y = 10000000
    min_z = 10000000
    max_x = 0
    max_y = 0
    max_z = 0
    for cube in cubes:
        min_x = min(min_x, cube[0])
        min_y = min(min_y, cube[1])
        min_z = min(min_z, cube[2])

        max_x = max(max_x, cube[0])
        max_y = max(max_y, cube[1])
        max_z = max(max_z, cube[2])

    min_x -= 1
    min_y -= 1
    min_z -= 1
    max_x += 1
    max_y += 1
    max_z += 1

    hit_side = 0
    start = (min_x, min_y, min_z)
    queue = [start]
    visited = set()
    cubes = set(cubes)
    while len(queue) > 0:
        curr = queue.pop(0)

        if curr in visited:
            continue

        visited.add(curr)

        for amt in [1, -1]:
            for d in [(0, 0, amt), (0, amt, 0), (amt, 0, 0)]:
                new_val = (curr[0] + d[0], curr[1] + d[1], curr[2] + d[2])

                if new_val in cubes:
                    hit_side += 1
                elif (
                    new_val not in visited
                    and new_val[0] >= min_x
                    and new_val[0] <= max_x
                    and new_val[1] >= min_y
                    and new_val[1] <= max_y
                    and new_val[2] >= min_z
                    and new_val[2] <= max_z
                ):
                    queue.append(new_val)

    return hit_side


with open("day_18.txt") as file:
    contenido = [tuple(int(x) for x in l.strip().split(",")) for l in file.readlines()]
    print(part_one(contenido))
    print(part_two(contenido))

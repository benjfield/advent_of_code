from advent.runner import register
import re

@register(17, 2020, 1, True)
def conway_cubes_1(split_text):
    active_cubes = set()

    for y, line in enumerate(split_text):
        for x, value in enumerate(line):
            if value == "#":
                active_cubes.add((x, y, 0))

    for i in range(6):
        cube_neighbours = {} 
        for cube in active_cubes:
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    for z in [-1, 0, 1]:
                        neighbour = (cube[0] + x, cube[1] + y, cube[2] + z)
                        if neighbour != cube:
                            cube_neighbours[neighbour] = cube_neighbours.get(neighbour, 0) + 1
                        else:
                            cube_neighbours[neighbour] = cube_neighbours.get(neighbour, 0)


        for key, value in cube_neighbours.items():
            if key in active_cubes:
                if value != 2 and value != 3:
                    active_cubes.remove(key)
            else:
                if value == 3:
                    active_cubes.add(key)

    return len(active_cubes)


@register(17, 2020, 2, True)
def conway_cubes_2(split_text):
    active_cubes = set()

    for y, line in enumerate(split_text):
        for x, value in enumerate(line):
            if value == "#":
                active_cubes.add((x, y, 0, 0))

    for i in range(6):
        cube_neighbours = {} 
        for cube in active_cubes:
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    for z in [-1, 0, 1]:
                        for w in [-1, 0, 1]:
                            neighbour = (cube[0] + x, cube[1] + y, cube[2] + z, cube[3] + w)
                            if neighbour != cube:
                                cube_neighbours[neighbour] = cube_neighbours.get(neighbour, 0) + 1
                            else:
                                cube_neighbours[neighbour] = cube_neighbours.get(neighbour, 0)


        for key, value in cube_neighbours.items():
            if key in active_cubes:
                if value != 2 and value != 3:
                    active_cubes.remove(key)
            else:
                if value == 3:
                    active_cubes.add(key)

    return len(active_cubes)
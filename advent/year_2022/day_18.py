from advent.runner import register

@register(18, 2022, 1, True)
def boiling_boulders_1(split_text):
    cubes = set()
    for line in split_text:
        cubes.add(tuple([int(x) for x in line.split(",")]))

    surface_area = 0
    for cube in cubes:
        for adjustment in [-1, 1]:
            for neighbour in[
                (cube[0] + adjustment, cube[1], cube[2]),
                (cube[0], cube[1] + adjustment, cube[2]),
                (cube[0], cube[1], cube[2] + adjustment)
            ]:
                if neighbour not in cubes:
                    surface_area += 1
    
    return surface_area

@register(18, 2022, 2, True)
def boiling_boulders_2(split_text):
    cubes = set()
    min_x = 100
    max_x = 0
    min_y = 100
    max_y = 0
    min_z = 100
    max_z = 0

    for line in split_text:
        cube = tuple([int(x) for x in line.split(",")])

        if cube[0] < min_x:
            min_x = cube[0]
        if cube[0] > max_x:
            max_x = cube[0]

        if cube[1] < min_y:
            min_y = cube[1]
        if cube[1] > max_y:
            max_y = cube[1]

        if cube[2] < min_z:
            min_z = cube[2]
        if cube[2] > max_z:
            max_z = cube[2]

        cubes.add(tuple([int(x) for x in line.split(",")]))


    neighbours = {}
    for cube in cubes:
        for adjustment in [-1, 1]:
            for neighbour in[
                (cube[0] + adjustment, cube[1], cube[2]),
                (cube[0], cube[1] + adjustment, cube[2]),
                (cube[0], cube[1], cube[2] + adjustment)
            ]:
                if neighbour not in cubes:
                    neighbours[neighbour] = neighbours.get(neighbour, 0) + 1

    outside_neighbours = set()
    inside_neighbours = set()

    for original_neighbour in neighbours.keys():
        if original_neighbour not in outside_neighbours or original_neighbour not in inside_neighbours:
            neighbour_neighbours = [original_neighbour]
            neighbour_neighbours_set = {original_neighbour}
            neighbour_index = 0
            try:
                while neighbour_index < len(neighbour_neighbours):
                    for adjustment in [-1, 1]:
                        for neighbour in[
                            (neighbour_neighbours[neighbour_index][0] + adjustment, neighbour_neighbours[neighbour_index][1], neighbour_neighbours[neighbour_index][2]),
                            (neighbour_neighbours[neighbour_index][0], neighbour_neighbours[neighbour_index][1] + adjustment, neighbour_neighbours[neighbour_index][2]),
                            (neighbour_neighbours[neighbour_index][0], neighbour_neighbours[neighbour_index][1], neighbour_neighbours[neighbour_index][2] + adjustment)
                        ]:
                            if neighbour in outside_neighbours:
                                raise Exception
                            elif neighbour[0] > max_x or neighbour[0] < min_x or neighbour[1] > max_y or neighbour[1] < min_y or neighbour[2] > max_z or neighbour[2] < min_z:
                                raise Exception
                            
                            if neighbour not in neighbour_neighbours_set and neighbour not in cubes:
                                neighbour_neighbours.append(neighbour)
                                neighbour_neighbours_set.add(neighbour)

                    neighbour_index += 1
                            
                for neighbour in neighbour_neighbours:
                    inside_neighbours.add(neighbour)
            except:
                for neighbour in neighbour_neighbours:
                    outside_neighbours.add(neighbour)

    surface_area = 0
    for neighbour, neighbour_count in neighbours.items():
        if neighbour in outside_neighbours:
            surface_area += neighbour_count

    return surface_area
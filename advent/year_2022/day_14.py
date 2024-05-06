from advent.runner import register

@register(14, 2022, 1, True)
def regolith_reservoir_1(split_text):
    bottom = 0
    filled_spaces = set()

    for line in split_text:
        coords_split = line.split(" -> ")
        for i in range(1, len(coords_split)):
            first_coord = [int(x) for x in coords_split[i - 1].split(",")]
            second_coord = [int(x) for x in coords_split[i].split(",")]

            if first_coord[0] > second_coord[0]:
                x_change = -1
            else:
                x_change = 1

            if first_coord[1] > second_coord[1]:
                y_change = -1
            else:
                y_change = 1

            for x in range(first_coord[0], second_coord[0] + x_change, x_change):
                for y in range(first_coord[1], second_coord[1] + y_change, y_change):
                    if y > bottom:
                        bottom = y
                    filled_spaces.add((x, y))

    count = 0
    while True:
        x = 500
        y = 0
        placed = False
        while not placed:
            if y > bottom:
                return count
            
            if (x, y + 1) not in filled_spaces:
                y = y + 1
            elif (x - 1, y + 1) not in filled_spaces:
                x = x - 1
                y = y + 1
            elif (x + 1, y + 1) not in filled_spaces:
                x = x + 1
                y = y + 1
            else:
                placed = True

        count += 1
        filled_spaces.add((x, y))

@register(14, 2022, 2, True)
def regolith_reservoir_2(split_text):
    bottom = 0
    filled_spaces = set()

    for line in split_text:
        coords_split = line.split(" -> ")
        for i in range(1, len(coords_split)):
            first_coord = [int(x) for x in coords_split[i - 1].split(",")]
            second_coord = [int(x) for x in coords_split[i].split(",")]

            if first_coord[0] > second_coord[0]:
                x_change = -1
            else:
                x_change = 1

            if first_coord[1] > second_coord[1]:
                y_change = -1
            else:
                y_change = 1

            for x in range(first_coord[0], second_coord[0] + x_change, x_change):
                for y in range(first_coord[1], second_coord[1] + y_change, y_change):
                    if y > bottom:
                        bottom = y
                    filled_spaces.add((x, y))

    count = 0
    while True:
        x = 500
        y = 0
        placed = False
        while not placed:
            if y > bottom:
                placed = True
            elif (x, y + 1) not in filled_spaces:
                y = y + 1
            elif (x - 1, y + 1) not in filled_spaces:
                x = x - 1
                y = y + 1
            elif (x + 1, y + 1) not in filled_spaces:
                x = x + 1
                y = y + 1
            else:
                placed = True

        count += 1
        if x == 500 and y == 0:
            return count
        else:
            filled_spaces.add((x, y))
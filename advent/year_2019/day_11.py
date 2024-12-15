from advent.runner import register
from advent.year_2019.computer import computer_from_string
from advent.utils.direction import Direction

@register(11, 2019, 1)
def paint_1(text):
    computer = computer_from_string(text)

    current_direction = Direction.UP

    finished = False
    x = 0
    y = 0
    colour_coords = {}

    while not finished:
        colour = colour_coords.get((x, y), 0)
        finished, output = computer.process([colour])
        if len(output) != 2:
            raise Exception("Incorrect response")
        colour_coords[(x, y)] = output[0]
        if output[1] == 0:
            current_direction = current_direction.rotate(clockwise=False)
        else:
            current_direction = current_direction.rotate(clockwise=True)

        x, y = current_direction.move_forward_x_and_y(x, y)

    return len(colour_coords)

@register(11, 2019, 2)
def paint_2(text):
    computer = computer_from_string(text)

    current_direction = Direction.UP

    finished = False
    x = 0
    y = 0
    colour_coords = {(0, 0): 1}
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    while not finished:
        colour = colour_coords.get((x, y), 0)
        finished, output = computer.process([colour])
        if len(output) != 2:
            raise Exception("Incorrect response")
        colour_coords[(x, y)] = output[0]
        if output[1] == 0:
            current_direction = current_direction.rotate(clockwise=False)
        else:
            current_direction = current_direction.rotate(clockwise=True)

        x, y = current_direction.move_forward_x_and_y(x, y)

        min_x = min(x, min_x)
        max_x = max(x, max_x)
        min_y = min(y, min_y)
        max_y = max(y, max_y)

    registration_paint = []

    for y in range(min_y, max_y + 1):
        registration_paint.append([])
        for x in range(min_x, max_x + 1):
            registration_paint[-1].append(" ")

    for key, value in colour_coords.items():
        if value == 1:
            x = key[0]
            y = key[1]
            registration_paint[y - min_y][x - min_x] = "I"

    for row in registration_paint:
        print("".join(row))
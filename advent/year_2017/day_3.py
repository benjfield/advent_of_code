import re
from advent.runner import register
import math
from advent.utils.direction import Direction

@register(3, 2017, 1, False)
def spiral_memory_1(text):
    number = int(text)
    square_root = int(math.sqrt(number))

    if square_root%2 == 0:
        square_root += 1
    elif square_root ** 2 != number:
        square_root += 2

    corner = square_root ** 2

    distance_to_center = int((square_root - 1)/2)

    distance_from_corner = (corner - number) % (square_root - 1)

    distance_from_center_of_row = abs(distance_from_corner - distance_to_center)

    return distance_from_center_of_row + distance_to_center
    
@register(3, 2017, 2, False)
def spiral_memory_2(text):
    number = int(text)
    x = 0
    y = 0

    memory = {(0, 0): 1}

    distance = 1
    while True:
        for direction, additional in [
            (Direction.RIGHT, 0),
            (Direction.UP, 0),
            (Direction.LEFT, 1),
            (Direction.DOWN, 1)
        ]:
            for i in range(distance + additional):
                x, y = direction.move_forward_x_and_y(x, y)

                sum = 0
                for x_change in [-1, 0, 1]:
                    for y_change in [-1, 0, 1]:
                        sum += memory.get((x + x_change, y + y_change), 0)

                if sum > number:
                    return sum
                
                memory[(x, y)] = sum

        distance += 2

            


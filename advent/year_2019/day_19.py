from advent.runner import register
from advent.year_2019.computer import computer_from_string, process
from advent.utils.direction import Direction, Rotation
from advent.utils.path_finding import Node
import copy
import time

@register(19, 2019, 1)
def tractor_1(text, grid_size=50):
    computer = computer_from_string(text)
    start = time.time()
    total = 0
    for x in range(grid_size):
        for y in range(grid_size):
            computer.reset()
            finished, output = process(computer,[x, y])
            if output[0] == 1:
                #print(f"x {x} y {y}")
                total += 1

    end = time.time()
    print(end - start)
    return total

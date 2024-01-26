from advent.runner import register
from advent.year_2019.computer import Computer
from advent.utils.direction import Direction

@register(17, 2019, 1)
def ascii_1(text):
    computer = Computer(text)

    finished, output = computer.process()

    scaffold = [[]]

    added = 0
    for ascii in output:
        if ascii == 10:
            if added > 0:
                scaffold.append([])
                added = 0
        else:
            scaffold[-1].append(chr(ascii))
            added += 1

    if added == 0:
        scaffold = scaffold[:-1]

    alignment = 0

    for y, row in enumerate(scaffold):
        for x, value in enumerate(row):
            if value == "#":
                if x > 0 and x < (len(row) - 1) and y > 0 and y < (len(scaffold) - 1):
                    if scaffold[y-1][x] == "#" and scaffold[y+1][x] == "#" and scaffold[y][x-1] == "#" and scaffold[y][x+1] == "#":
                        alignment += x*y

    return alignment

@register(17, 2019, 2)
def ascii_2(text):
    computer = Computer(text)

    finished, output = computer.process()

    scaffold = [[]]

    added = 0
    for ascii in output:        
        if ascii == 10:
            if added > 0:
                scaffold.append([])
                added = 0
        else:
            scaffold[-1].append(chr(ascii))
            added += 1

    if added == 0:
        scaffold = scaffold[:-1]

    current_x = 0
    current_y = 0
    scaffold_node = {}
    for y, row in enumerate(scaffold):
        for x, value in enumerate(row):
            if value == "#":

                if x > 0 and x < (len(row) - 1) and y > 0 and y < (len(scaffold) - 1):
                    if scaffold[y-1][x] == "#" and scaffold[y+1][x] == "#" and scaffold[y][x-1] == "#" and scaffold[y][x+1] == "#":
                        junctions[(x, y)] = {Direction.UP: }

    return alignment
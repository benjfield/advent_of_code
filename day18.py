from aocd import get_data
import re
from copy import deepcopy
def dig_1(text):
    dig_instructions = []
    for digs in text.split("\n"):
        match = re.match(r"([R|D|L|U]) (\d+) .*", digs)
        dig_instructions.append({
            "direction": match.group(1),
            "distance": int(match.group(2))
        })

    total_dug = 0

    dig_pivots = {}    

    x = 0
    y = 0

    lowest_x = 0
    largest_x = 0
    lowest_y = 0
    largest_y = 0

    for dig_instruction in dig_instructions:
        if dig_instruction["direction"] == "U":
            y -= dig_instruction["distance"]
        elif dig_instruction["direction"] == "D":
            y += dig_instruction["distance"]
        elif dig_instruction["direction"] == "R":
            x += dig_instruction["distance"]
        elif dig_instruction["direction"] == "L":
            x -= dig_instruction["distance"]

        lowest_x = min(x, lowest_x)
        largest_x = max(x, largest_x)
        lowest_y = min(y, lowest_y)
        largest_y = max(y, largest_y)

    start_x = 0 - lowest_x
    start_y = 0 - lowest_y

    dig_tiles = []

    for y in range(largest_y - lowest_y + 1):
        dig_tiles.append([])
        for x in range(largest_x - lowest_x + 1):
            dig_tiles[-1].append(False)

    x = start_x
    y = start_y

    for row in dig_tiles:
        print(row)
        
    for dig_instruction in dig_instructions:
        if dig_instruction["direction"] == "U":
            for i in range(dig_instruction["distance"]):
                dig_tiles[y - i][x] = True
            y -= dig_instruction["distance"]
        elif dig_instruction["direction"] == "D":
            for i in range(dig_instruction["distance"]):
                dig_tiles[y + i][x] = True
            y += dig_instruction["distance"]
        elif dig_instruction["direction"] == "R":
            for i in range(dig_instruction["distance"]):
                dig_tiles[y][x + i] = True
            x += dig_instruction["distance"]
        elif dig_instruction["direction"] == "L":
            for i in range(dig_instruction["distance"]):
                dig_tiles[y][x - i] = True
            x -= dig_instruction["distance"]

    inside_dig_tiles = deepcopy(dig_tiles)

    for y, row in enumerate(dig_tiles):
        inside = False            
        previous_left = False
        previous_right = False
        for x, tile in enumerate(row):
            if not tile:
                if inside:
                    inside_dig_tiles[y][x] = True
                previous_right = False
                previous_left = False
            else:
                left = False
                right = False

                if y >= 1 and dig_tiles[y - 1][x]:
                    left = True

                if y <= len(dig_tiles) - 2 and dig_tiles[y + 1][x]:
                    right = True

                if right and left:
                    inside = not inside
                elif not (previous_left and previous_right):
                    if (previous_left and right) or (previous_right and left):
                        inside = not inside
                if right or left:
                    previous_left = left
                    previous_right = right

    total_dug = 0

    for row in inside_dig_tiles:
        print(row)
        for tile in row:
            if tile:
                total_dug += 1

    return total_dug
          
dig_text = get_data(day=18, year=2023)     
print(dig_1(dig_text))



        

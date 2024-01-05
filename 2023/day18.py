from aocd import get_data
import re
from copy import deepcopy
def naive_dig_1(text):
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

    total_dug = 0

    for i, row in enumerate(inside_dig_tiles):
        row_dug = 0
        for tile in row:
            if tile:
                total_dug += 1

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
        for tile in row:
            if tile:
                total_dug += 1

    return total_dug

def add_to_dig_pivots(dig_pivots, pivot, top, bottom):
    pivots_to_remove = []
    pivots_to_add = []
    current_top = top

    for i, possible_pivot in enumerate(dig_pivots):
        possible_top = max(possible_pivot["top"], current_top)

        if bottom < possible_top:
            break

        possible_bottom = min(possible_pivot["bottom"], bottom)

        if possible_bottom >= possible_top:
            if current_top < possible_top:
                pivots_to_add.append({
                    "top": current_top,
                    "bottom": possible_top - 1,
                    "pivots": [pivot]
                })
            elif possible_pivot["top"] < current_top:
                pivots_to_add.append({
                    "top": possible_pivot["top"],
                    "bottom": current_top - 1,
                    "pivots": possible_pivot["pivots"]

                })
                possible_pivot["bottom"] = possible_top - 1
            
            pivots_to_remove.append(i)

            pivots_to_add.append({
                "top": possible_top,
                "bottom": possible_bottom,
                "pivots": possible_pivot["pivots"] + [pivot]
            })          

            if possible_pivot["bottom"] > possible_bottom:
                pivots_to_add.append({
                    "top": possible_bottom + 1,
                    "bottom": possible_pivot["bottom"],
                    "pivots": possible_pivot["pivots"]
                }) 
                break
            
            current_top = possible_bottom + 1
     
    if current_top <= bottom:
        pivots_to_add.append({
            "top": current_top,
            "bottom": bottom,
            "pivots": [pivot]
        })

    if len(pivots_to_remove) == 0:
        if len(dig_pivots) == 0:
            return pivots_to_add
        elif pivots_to_add[-1]["top"] < dig_pivots[0]["top"]:
            return pivots_to_add + dig_pivots
        return dig_pivots + pivots_to_add
    elif pivots_to_remove[-1] < len(dig_pivots) - 1:
        return dig_pivots[:pivots_to_remove[0]] + pivots_to_add + dig_pivots[pivots_to_remove[-1] + 1: ] 
    else:
        return dig_pivots[:pivots_to_remove[0]] + pivots_to_add


def process_dig_instructions(dig_instructions):
    total_dug = 0

    dig_pivots = []

    x = 0
    y = 0

    previous_x = 0

    for i, dig in enumerate(dig_instructions):
        if dig["direction"] == "U" or dig["direction"] == "D":
            if dig_instructions[i-2]["direction"] != dig["direction"]:
                dig_pivots = add_to_dig_pivots(dig_pivots, {
                    "left": min(x, previous_x),
                    "right": max(x, previous_x),
                    "contain": False
                }, y, y)
            else:
                dig_pivots = add_to_dig_pivots(dig_pivots, {
                    "left": min(x, previous_x),
                    "right": max(x, previous_x),
                    "contain": True
                }, y, y)
            
            if dig["direction"] == "U":
                if dig["distance"] > 1:
                    dig_pivots = add_to_dig_pivots(dig_pivots, {
                        "left": x,
                        "right": x,
                        "contain": True
                    }, y - dig["distance"] + 1, y - 1)

                y -= dig["distance"]
            else:
                if dig["distance"] > 1:
                    dig_pivots = add_to_dig_pivots(dig_pivots, {
                        "left": x,
                        "right": x,
                        "contain": True
                    }, y + 1, y + dig["distance"] - 1)

                y += dig["distance"]
                
        elif dig["direction"] == "R":
            previous_x = x
            x += dig["distance"]
        else:
            previous_x = x
            x -= dig["distance"]

        total_dug += dig["distance"]

    inside_dig = 0

    for pivot_details in dig_pivots:
        def sort_by_left(map):
            return map["left"]
        
        pivot_points = pivot_details["pivots"]

        pivot_points.sort(key=sort_by_left)

        row_count = 0

        inside=False
        for i in range(len(pivot_points) - 1):
            if inside == False and not pivot_points[i]["contain"]:
                pass
            elif inside == True and pivot_points[i]["contain"]:
                inside = not inside
            else:
                if pivot_points[i]["right"] >= pivot_points[i+1]["left"]:
                    raise Exception("panic")
                row_count += pivot_points[i+1]["left"] - pivot_points[i]["right"] - 1
                if pivot_points[i]["contain"]:
                    inside = not inside

        inside_dig += row_count * abs(pivot_details["bottom"] - pivot_details["top"] + 1)

    return total_dug + inside_dig

def dig_1(text):
    dig_instructions = []
    for digs in text.split("\n"):
        match = re.match(r"([R|D|L|U]) (\d+) .*", digs)
        dig_instructions.append({
            "direction": match.group(1),
            "distance": int(match.group(2))
        })

    return process_dig_instructions(dig_instructions)

def dig_2(text):
    dig_instructions = []
    for digs in text.split("\n"):
        match = re.match(r"[R|D|L|U] \d+ \(#(.{5})(.)\)", digs)

        direction = ""
        if match.group(2) == "0":
            direction = "R"
        elif match.group(2) == "1":
            direction = "D"
        elif match.group(2) == "2":
            direction = "L"
        else:
            direction = "U"

        dig_instructions.append({
            "direction": direction,
            "distance": int(match.group(1), 16)
        })

    return process_dig_instructions(dig_instructions)   
  
dig_text = get_data(day=18, year=2023)  


        

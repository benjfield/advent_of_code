import re
from aocd import get_data

def check_adjacent(text_lines, row, start, end):
    adjacent = ""

    start = max(start - 1, 0)
    end = min(end + 2, len(text_lines[row]))

    if row > 0:
        adjacent += text_lines[row-1][start:end]
    adjacent += text_lines[row][start:end]
    if row < len(text_lines) - 1:
        adjacent += text_lines[row+1][start:end]

    return re.search("[^a-zA-Z0-9\.\s]", adjacent) is not None

def parts_1(text):
    total_parts = 0
    text_lines = text.split("\n")
    for i, line in enumerate(text_lines):
        j = 0
        while j < len(line):
            number_match = re.match("^(\d+).*", line[j:])
            if number_match:
                number = number_match.group(1)
                number_length = len(str(number))
                if check_adjacent(text_lines, i, j, j + number_length - 1):
                    total_parts += int(number)
                j += number_length + 1
            else:
                j += 1
    
    return total_parts

def add_part_to_adjacent_gears(text_lines, row, start, end, number, gears):
    start = max(start - 1, 0)
    end = min(end + 2, len(text_lines[row]))

    start_row = max(0, row - 1)
    end_row = min(len(text_lines) , row + 2)

    for y in range(start_row, end_row):
        for x in range(start, end):
            if text_lines[y][x] == "*":
                gears[f"{y}_{x}"] = gears.get(f"{y}_{x}", []) + [number]

    return gears

def parts_2(text):
    gears = {}
    text_lines = text.split("\n")
    for i, line in enumerate(text_lines):
        j = 0
        while j < len(line):
            number_match = re.match("^(\d+).*", line[j:])
            if number_match:
                number = number_match.group(1)
                number_length = len(str(number))
                add_part_to_adjacent_gears(text_lines, i, j, j + number_length - 1, int(number), gears)
                j += number_length + 1
            else:
                j += 1
    
    total_gear_ratio = 0
    for gears in gears.values():
        if len(gears) == 2:
            total_gear_ratio += gears[0] * gears[1]

    return total_gear_ratio


parts_text = get_data(day=3, year=2023)
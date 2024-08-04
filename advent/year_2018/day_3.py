import re
from advent.runner import register

@register(3, 2018, 1, True)
def fabric_slice_1(split_text):
    coords = {}
    for line in split_text:
        parsed_regex = re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)

        start_x = int(parsed_regex.group(2))
        x_length = int(parsed_regex.group(3))
        start_y = int(parsed_regex.group(4))
        y_length = int(parsed_regex.group(5))

        for x in range(start_x, start_x + x_length):
            for y in range(start_y, start_y + y_length):
                coord = (x, y)
                coords[coord] = coords.get(coord, 0) + 1
                
        print(len(coords))
        exit()

    total = 0
    for value in coords.values():
        if value > 1:
            total +=1

    return total
from advent.runner import register
import re

@register(5, 2021, 1)
def vents_1(text):
    text_by_line = text.split("\n")

    vents = {}

    for line in text_by_line:
        matched_line = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line)

        x_1 = int(matched_line.group(1))
        x_2 = int(matched_line.group(3))
        y_1 = int(matched_line.group(2))
        y_2 = int(matched_line.group(4))

        if x_1 == x_2 or y_1 == y_2:
            for x in range(min(x_1, x_2), max(x_1, x_2) + 1):
                for y in range(min(y_1, y_2), max(y_1, y_2)+ 1):
                    key = 1000 * x + y
                    vents[key] = vents.get(key, 0) + 1

    count = 0
    for value in vents.values():
        if value > 1:
            count += 1

    return count

@register(5, 2021, 2)
def vents_2(text):
    text_by_line = text.split("\n")

    vents = {}

    for line in text_by_line:
        matched_line = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line)

        x_1 = int(matched_line.group(1))
        x_2 = int(matched_line.group(3))
        y_1 = int(matched_line.group(2))
        y_2 = int(matched_line.group(4))

        if x_1 == x_2 or y_1 == y_2:
            for x in range(min(x_1, x_2), max(x_1, x_2) + 1):
                for y in range(min(y_1, y_2), max(y_1, y_2)+ 1):
                    key = 1000 * x + y
                    vents[key] = vents.get(key, 0) + 1
        else:
            min_x = min(x_1, x_2)
            max_x = max(x_1, x_2)
            min_y = min(y_1, y_2)
            for i in range(max_x - min_x + 1):
                if (min_x == x_1 and min_y == y_1) or (min_x == x_2 and min_y ==y_2):
                    key = 1000 * (min_x + i) + (min_y + i)
                else:
                    key = 1000 * (max_x - i) + (min_y + i)
                vents[key] = vents.get(key, 0) + 1

    count = 0
    for value in vents.values():
        if value > 1:
            count += 1

    return count
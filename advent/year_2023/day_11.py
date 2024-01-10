import re
from advent.runner import register

@register(11, 2023, 1)
def stars_1(text):
    return stars_2(text, 2)

@register(11, 2023, 2)
def stars_2(text, empty_multiplier):
    empty_rows = []
    star_map = []
    for i, line in enumerate(text.split("\n")):
        star_map.append(line)
        if re.search(r"#", line) is None:
            empty_rows.append(i)

    empty_columns = []

    i = 0
    for i in range(len(star_map[0])):
        no_hashes = True
        for star_row in star_map:
            if star_row[i] == "#":
                no_hashes = False
                break

        if no_hashes:
            empty_columns.append(i)

    stars = []

    for y, star_row in enumerate(star_map):
        for x, star in enumerate(star_row):
            if star == "#":
                stars.append({
                        "x": x,
                        "y": y,
                    })
    
    total_distance = 0

    for i, star in enumerate(stars):
        for other_star in stars[i+1:]:
            empty_rows_or_columns = 0
            for row in empty_rows:
                if row > min(star["y"], other_star["y"]):
                    if row < max(star["y"], other_star["y"]):
                        empty_rows_or_columns += 1
                    else:
                        break
            for column in empty_columns:
                if column > min(star["x"], other_star["x"]):
                    if column < max(star["x"], other_star["x"]):
                        empty_rows_or_columns += 1
                    else:
                        break

            total_distance += abs(other_star["x"] - star["x"]) + abs(other_star["y"] - star["y"]) + (empty_multiplier-1) * empty_rows_or_columns

    return total_distance
from advent.runner import register
from advent.utils.split_text import create_char_grid
from advent.utils.grid import Grid



@register(4, 2025, 1, False)
def forklift_1(text):
    grid = create_char_grid(text)

    paper_rolls = set()
    removed_coords = []

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "@":
                paper_rolls.add((x, y))

    for x, y in paper_rolls:
        count = 0
        for x_change in [-1, 0, 1]:
            for y_change in [-1, 0, 1]:
                if x_change != 0 or y_change != 0:
                    coords = (x + x_change, y + y_change)
                    if coords in paper_rolls:
                            count += 1
        if count < 4:
            removed_coords.append((x, y))

    return len(removed_coords)

@register(4, 2025, 2, False)
def forklift_2(text):
    grid = create_char_grid(text)

    paper_rolls = set()
    removed_coords = []
    total_removed = 0
    found_none_last_run = False

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "@":
                paper_rolls.add((x, y))

    while not found_none_last_run:
        for x, y in paper_rolls:
            count = 0
            for x_change in [-1, 0, 1]:
                for y_change in [-1, 0, 1]:
                    if x_change != 0 or y_change != 0:
                        coords = (x + x_change, y + y_change)
                        if coords in paper_rolls:
                            count += 1
            if count < 4:
                removed_coords.append((x, y))

        total_removed += len(removed_coords)
        paper_rolls.difference_update(removed_coords)
        if len(removed_coords) == 0:
            found_none_last_run = True
        removed_coords = []       

    return total_removed
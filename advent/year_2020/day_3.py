from advent.runner import register
import re

@register(3, 2020, 1, True)
def toboggan_1(split_text):
    map = []
    for line in split_text:
        map.append([])
        for char in line:
            if char == "#":
                map[-1].append(True)
            else:
                map[-1].append(False)

    y = 0
    x = 0
    tree_count = 0

    while y < len(map):
        if map[y][x]:
            tree_count += 1
        x = (x + 3) % len(map[0])
        y += 1
        
    return tree_count

@register(3, 2020, 2, True)
def toboggan_2(split_text):
    map = []
    for line in split_text:
        map.append([])
        for char in line:
            if char == "#":
                map[-1].append(True)
            else:
                map[-1].append(False)

    total_tree_count = 1

    toboggans = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    for toboggan in toboggans:
        y = 0
        x = 0
        tree_count = 0
        while y < len(map):
            if map[y][x]:
                tree_count += 1
            x = (x + toboggan[0]) % len(map[0])
            y += toboggan[1]
        total_tree_count *= tree_count
        
    return total_tree_count
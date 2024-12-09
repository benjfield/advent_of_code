from advent.runner import register
from collections import defaultdict
import itertools

@register(1, 2024, 1, True)
def hysteria_1(text):
    list_1 = []
    list_2 = []
    for line in text:
        split = line.split()
        list_1.append(int(split[0]))
        list_2.append(int(split[1]))

    list_1.sort()
    list_2.sort()

    total_distance = 0

    for val_1, val_2 in itertools.zip_longest(list_1, list_2):
        total_distance += abs(val_2 - val_1)

    return total_distance

@register(1, 2024, 2, True)
def hysteria_2(text):
    list_1 = []
    list_2 = defaultdict(lambda: 0)
    for line in text:
        split = line.split()
        list_1.append(int(split[0]))
        list_2[int(split[1])] += 1

    similarity = 0

    for key in list_1:
        similarity += key * list_2[key]

    return similarity
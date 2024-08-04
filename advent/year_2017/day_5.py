import re
from advent.runner import register

@register(5, 2017, 1, True)
def maze_1(text):
    numbers = [int(x) for x in text]

    index = 0
    i = 0
    while True:
        old_index = index
        index += numbers[index]
        numbers[old_index] += 1
        i += 1
        if index >= len(numbers) or index < 0:
            return i

@register(5, 2017, 2, True)
def maze_2(text):
    numbers = [int(x) for x in text]

    index = 0
    i = 0
    while True:
        old_index = index
        index += numbers[index]
        if numbers[old_index] >= 3:
            numbers[old_index] -= 1
        else:
         numbers[old_index] += 1
        i += 1
        if index >= len(numbers) or index < 0:
            return i
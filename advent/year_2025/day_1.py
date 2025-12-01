from advent.runner import register
from collections import defaultdict
import itertools

@register(1, 2025, 1, True)
def safe_lock_1(text):
    value = 50

    count = 0

    for rotate in text:
        rotation = rotate[0]
        amount = int(rotate[1:])

        if rotation == "L":
            value -= amount
        else:
            value += amount

        value = value %100

        if value == 0:
            count += 1

    return count

@register(1, 2025, 2, True)
def safe_lock_2(text):
    value = 50

    count = 0
    prior_was_zero = False

    for rotate in text:
        rotation = rotate[0]
        amount = int(rotate[1:])

        if rotation == "L":
            value -= amount
        else:
            value += amount

        if value >= 100 :
            count += value // 100
            value = value %100
        elif value < 0:
            if prior_was_zero:
                count += abs((value - 1) // 100) -1
            else:
                count += abs((value - 1) // 100)
            value = value %100
        elif value == 0:
            count += 1
            value = value %100

        if value == 0:
            prior_was_zero = True
        else:
            prior_was_zero = False

    return count
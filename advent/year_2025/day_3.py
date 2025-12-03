from advent.runner import register
from collections import defaultdict
import itertools

class FoundDigit(Exception):
    pass

@register(3, 2025, 1, True)
def batteries_1(text):
    total = 0

    for line in text:
        battery_index = defaultdict(list)

        for index, char in enumerate(list(line)):
            battery_index[int(char)].append(index)

        min_index = -1
        digits = ""

        for count in reversed(range(2)):
            try:
                for i in reversed(range(10)):
                    for index in battery_index[i]:
                        if index > min_index and index < len(line) - count:
                            digits += str(i)
                            min_index = index
                            raise FoundDigit
            except FoundDigit:
                pass
        
        total += int(digits)

    return total

@register(3, 2025, 2, True)
def batteries_2(text):
    total = 0

    for line in text:
        battery_index = defaultdict(list)

        for index, char in enumerate(list(line)):
            battery_index[int(char)].append(index)

        min_index = -1
        digits = ""

        for count in reversed(range(12)):
            try:
                for i in reversed(range(10)):
                    for index in battery_index[i]:
                        if index > min_index and index < len(line) - count:
                            digits += str(i)
                            min_index = index
                            raise FoundDigit
            except FoundDigit:
                pass
        
        total += int(digits)

    return total
import re
from advent.runner import register
import itertools

@register(2, 2017, 1, True)
def corrupt_checksum_1(text):
    total = 0    
    for line in text:
        numbers = [int(x) for x in line.split()]

        total += max(numbers) - min(numbers)

    return total

@register(2, 2017, 2, True)
def corrupt_checksum_2(text):
    total = 0    
    for line in text:
        numbers = [int(x) for x in line.split()]

        for number_1, number_2 in itertools.product(numbers, numbers):
            if number_1 != number_2:
                if number_1%number_2 == 0:
                    total += int(number_1/number_2)

    return total
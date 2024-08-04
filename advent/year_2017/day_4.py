import re
from advent.runner import register

@register(4, 2017, 1, True)
def passphrase_1(text):
    total_valid = 0

    for line in text:
        words = line.split()
        if len(set(words)) == len(words):
            total_valid += 1

    return total_valid

@register(4, 2017, 2, True)
def passphrase_2(text):
    total_valid = 0

    for line in text:
        words = [str(sorted(list(x))) for x in line.split()]
        if len(set(words)) == len(words):
            total_valid += 1

    return total_valid
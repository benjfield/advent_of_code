import re
from advent.runner import register

@register(1, 2017, 1, True)
def inverse_captcha_1(text):
    total = 0
    text = list(text[0])
    for i, digit in enumerate(text):
        if int(digit) >= 10:
            raise Exception
        if digit == text[i-1]:
            total += int(digit)

    return total

@register(1, 2017, 2, True)
def inverse_captcha_2(text):
    total = 0
    text = list(text[0])
    for i, digit in enumerate(text):
        if int(digit) >= 10:
            raise Exception
        if digit == text[i-int(len(text)/2)]:
            total += int(digit)

    return total
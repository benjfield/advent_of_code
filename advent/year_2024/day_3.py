from advent.runner import register
import re

@register(3, 2024, 1, False)
def mull_1(text):
    total = 0
    for match in re.finditer(r"mul\((\d+)\,(\d+)\)", text):
        total += int(match.group(1)) * int(match.group(2))

    return total

@register(3, 2024, 2, False)
def mull_2(text):

    commands = text.split("don't()")

    total = 0
    for match in re.finditer(r"mul\((\d+)\,(\d+)\)", commands[0]):
        total += int(match.group(1)) * int(match.group(2))

    for command in commands[1:]:
        valid_command = str.partition(command, "do()")[2]

        for match in re.finditer(r"mul\((\d+)\,(\d+)\)", valid_command):
            total += int(match.group(1)) * int(match.group(2))

    return total
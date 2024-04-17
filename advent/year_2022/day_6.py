from advent.runner import register
import math
import re

def check_line_for_marker(line, length_to_check=4):
    letters = {}
    for letter in line[:length_to_check]:
        letters[letter] = letters.get(letter, 0) + 1

    if len(letters) == length_to_check:
        return length_to_check

    for i in range(length_to_check, len(line)):
        letters[line[i - length_to_check]] -= 1
        if letters[line[i - length_to_check]] == 0:
            del letters[line[i - length_to_check]]
        letters[line[i]] = letters.get(line[i], 0) + 1
        
        if len(letters) == length_to_check:
            return i + 1

@register(6, 2022, 1, True)
def tuning_trouble_1(split_text):
    min_value = len(split_text[0])
    
    for line in split_text:
        marker = check_line_for_marker(line, 4)

        if marker < min_value:
            min_value = marker
    
    return min_value

@register(6, 2022, 2, True)
def tuning_trouble_2(split_text):
    min_value = len(split_text[0])
    
    for line in split_text:
        marker = check_line_for_marker(line, 14)

        if marker < min_value:
            min_value = marker
    
    return min_value
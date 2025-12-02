from advent.runner import register
from collections import defaultdict
import itertools

@register(2, 2025, 1, False)
def invalid_id_1(text):
    total = 0

    for string_range in text.split(","):
        number_range = string_range.split("-")
        for i in range(int(number_range[0]), int(number_range[1]) + 1):
            i_str = str(i)
            if len(i_str) % 2 == 0:
                split_length = len(i_str) // 2

                if i_str[:split_length] == i_str[split_length:]:
                    total += i

    return total

@register(2, 2025, 2, False)
def invalid_id_2(text):
    total = 0

    for string_range in text.split(","):
        number_range = string_range.split("-")
        for i in range(int(number_range[0]), int(number_range[1]) + 1):
            i_str = str(i)

            max_length = len(i_str) // 2

            for length in range(1, max_length + 1):
                initial_substring = i_str[:length]
                
                valid_repeat = True
                for start in range(length, len(i_str), length):
                    if start + length == len(i_str):
                        if i_str[start:] != initial_substring:
                            valid_repeat = False
                            break
                    else:
                        if i_str[start:start + length] != initial_substring:
                            valid_repeat = False
                            break
                if valid_repeat:
                    total += i
                    break

    return total
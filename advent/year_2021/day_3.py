from advent.runner import register
import math
@register(3, 2021, 1)
def binary_power_1(text):
    text_by_line = text.split("\n")

    counts = [ 0 for x in range(len(text_by_line[0])) ]

    for i, line in enumerate(text_by_line):
        for j, char in enumerate(line):
            if char == "1":
                counts[j] += 1

    first_number_string = ""

    for count in counts:
        if count > int(len(text_by_line) / 2):
            first_number_string += "1"
        else:
            first_number_string += "0"
            
    max_number = (2 ** len(counts)) - 1

    first_number = int(first_number_string, 2)

    return first_number * (max_number - first_number)


def get_values_with_bit(initial_values, index, most_common=True):
    count = 0

    for value in initial_values:
        if value[index] == "1":
            count += 1

    if count >= math.ceil(len(initial_values)/2):
        if most_common:
            bit_to_test = "1"
        else:
            bit_to_test = "0"
    else:
        if most_common:
            bit_to_test = "0"
        else:
            bit_to_test = "1"

    approved_values = []

    for value in initial_values:
        if value[index] == bit_to_test:
            approved_values.append(value)
        
    return approved_values


@register(3, 2021, 2)
def binary_power_2(text):
    text_by_line = text.split("\n")

    most_common_values = text_by_line.copy()
    index = 0

    while len(most_common_values) > 1:
        most_common_values = get_values_with_bit(most_common_values, index)
        index += 1

    least_common_values = text_by_line.copy()
    index = 0

    while len(least_common_values) > 1:
        least_common_values = get_values_with_bit(least_common_values, index, False)
        index += 1

    return int(most_common_values[0], 2) * int(least_common_values[0], 2)
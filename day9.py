import re
from aocd import get_data
from itertools import pairwise


def calculate_diff_value(sequence, start_not_finish):
    diff_list = [y - x for x, y in pairwise(sequence)]

    all_zeros = True
    for diff in diff_list:
        if diff != 0:
            all_zeros = False
            break

    if all_zeros:
        return 0
    elif start_not_finish:
        return diff_list[0] - calculate_diff_value(diff_list, start_not_finish)
    else:
        return diff_list[-1] + calculate_diff_value(diff_list, start_not_finish)

def parse_sequence_text(text):
    sequences = []

    for line in text.split("\n"):
        this_sequence = []
        for number in re.findall(r"(-?\d+)", line):
            this_sequence.append(int(number))
        sequences.append(this_sequence)
    
    return sequences   

def sequence_1(text):
    sequences = parse_sequence_text(text)
    new_values_sum = 0

    for sequence in sequences:
        new_values_sum += sequence[-1] + calculate_diff_value(sequence, False)

    return new_values_sum

def sequence_2(text):
    sequences = parse_sequence_text(text)
    new_values_sum = 0

    for sequence in sequences:
        new_values_sum += sequence[0] - calculate_diff_value(sequence, True)

    return new_values_sum

sequence_text = get_data(day=9, year=2023)
print(sequence_2(sequence_text))


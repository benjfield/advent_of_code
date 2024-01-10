import re
from functools import cache
from advent.runner import register

@cache
def find_match(string, broken_group_counts):
    if len(broken_group_counts) == 1:
        count = 0
        possible_places = string.split(".")
        found_earlier_hash = False 
        for place in possible_places:
            found_hash, count_to_add = get_terminal_count(broken_group_counts[0], place)
            if not found_earlier_hash:
                count += count_to_add
                if found_hash:
                    found_earlier_hash = True
                    count = count_to_add
            elif found_hash:
                return 0
        return count
    else:
        next_count_list = broken_group_counts[1:]

        count = 0
        possible_space = len(string) - (sum(broken_group_counts) + len(broken_group_counts) - 1) + 1
        i = 0
        first_hash = possible_space
        start_dot_check = 0
        found_hash = False
        while i < min(possible_space, first_hash + 1):
            found_dot = False
            for j in range(start_dot_check, broken_group_counts[0]):
                if string[i+j] == ".":
                    i = i + j + 1
                    start_dot_check = 0
                    found_dot=True
                    break
                if not found_hash and string[i+j] == "#":
                    found_hash = True
                    first_hash = i + j
            if not found_dot:
                start_dot_check = broken_group_counts[0] - 1
                if string[i + broken_group_counts[0]] != "#":
                    count += find_match(string[i+broken_group_counts[0]+1:], next_count_list)
                i += 1

        return count

@cache
def get_terminal_count(needed_length, string):
    first_char = -1
    last_char = -1
    for i, char in enumerate(string):
        if char == "#":
            last_char = i
            if first_char == -1:
                first_char = i

    if first_char == -1:
        return False, max(len(string) - needed_length + 1, 0)
    else:
        max_size = min(len(string), first_char + needed_length)
        min_size = max(0, last_char - needed_length + 1)

        return True, max((max_size - min_size) - needed_length + 1, 0)

def get_initial_data(text):
    spring_errors = []
    for line in text.split("\n"):
        springs = re.match(r"([\.#\?]+)", line).group(1)

        broken_group_counts = []

        for broken_group in re.findall(r"(\d+)", line):
            broken_group_counts.append(int(broken_group))

        spring_errors.append({
            "springs": springs,
            "counts": broken_group_counts,
        })
    return spring_errors


def strip_strings(spring_errors):
    for error in spring_errors:
        error["springs"] = error["springs"].strip(".")

@register(12, 2023, 1)
def springs_1(text):
    spring_errors = get_initial_data(text)
    error_count = 0

    strip_strings(spring_errors)

    for error in spring_errors:
        match_count = find_match(error["springs"], tuple(error["counts"]))
        error_count += match_count

    return error_count

@register(12, 2023, 2)
def springs_2(text):
    spring_errors = get_initial_data(text)
    error_count = 0

    for error in spring_errors:
        springs_array = []
        counts = []

        for i in range(5):
            springs_array.append(error["springs"])
            counts += (error["counts"]) 

        error["springs"] = "?".join(springs_array)
        error["counts"] = counts

    strip_strings(spring_errors)

    for i, error in enumerate(spring_errors):
        match_count = find_match(error["springs"], tuple(error["counts"]))
        error_count += match_count

    return error_count
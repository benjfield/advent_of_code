from advent.runner import register
from advent.utils.split_text import split_text, Split
from dataclasses import dataclass
import math
from functools import cache
from collections import defaultdict

from time import perf_counter

def split_int(number: int) -> list[int]:
    digits = math.ceil(math.log10(number + 1)) 
    if digits > 0 and digits %2 == 0:
        part_1 = number // (10 ** (digits // 2))
        part_2 = number - (part_1 * (10 ** (digits // 2)))

        return [part_1, part_2]
    return[number]

@cache
def split_stone(stone):
    if stone == 0:
        return [1]
    else:
        stone_str = str(stone)
        if len(stone_str) % 2 == 0:
            length = len(stone_str) // 2
            return [int(stone_str[:length]), int(stone_str[length:])]
        else:
            return [stone * 2024]

def split_count(stone_count):
    result = defaultdict(int)
    for stone, count in stone_count.items():
        for result_stone in split_stone(stone):
            result[result_stone] += count

    return result

@cache
def split_stone_memoisation(stone, count_remaining):
    if count_remaining == 0:
        return 1
    else:
        count_remaining -= 1
        if stone == 0:
            return split_stone(1, count_remaining)
        else:
            stone_str = str(stone)
            if len(stone_str) % 2 == 0:
                length = len(stone_str) // 2
                count_1 = split_stone(int(stone_str[:length]), count_remaining)
                count_2 = split_stone(int(stone_str[length:]), count_remaining)

                return count_1 + count_2
            else:
                return split_stone(stone * 2024, count_remaining)

@register(11, 2024, 1)
def func_1(text):
    stones = {int(x): 1 for x in text.split(" ")}

    for i in range(25):
        stones = split_count(stones)

    count = 0 
    for stone_count in stones.values():
        count += stone_count 

    return count

@register(11, 2024, 2)
def func_2(text):
    stones = {int(x): 1 for x in text.split(" ")}

    start = perf_counter()
    for i in range(75):
        stones = split_count(stones)
    stop = perf_counter()
    print(stop - start)

    start = perf_counter()
    count = 0 
    for stone_count in stones.values():
        count += stone_count 
    stop = perf_counter()
    print(stop - start)

    return count
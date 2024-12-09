from advent.runner import register
import math
from itertools import combinations
from dataclasses import dataclass

@register(9, 2024, 1, False)
def func_1(text):
    positions = []

    id = 0
    for i, char in enumerate(text):
        length = int(char)

        if i%2 == 1:
            positions += [None] * length
        else:
            positions += [id] * length
            id += 1

    checksum = 0
    j = len(positions) - 1
    i = 0
    while i <= j:
        if positions[i] is None:
            while j > i:
                moved = False
                if positions[j] is not None:
                    checksum += i * positions[j]
                    moved = True
                j -= 1
                if moved:
                    break
        else:
            checksum += i * positions[i]
        i += 1

    return checksum

@dataclass
class Gap:
    length: int
    start: int

@dataclass
class File:
    length: int
    start: int
    id: int

@register(9, 2024, 2, False)
def func_2(text):
    gaps = []
    files = []

    current_start = 0
    id = 0
    for i, char in enumerate(text):
        length = int(char)
        if i%2 == 1:
            gaps.append(Gap(
                length,
                current_start,
            ))
        else:
            files.append(File(
                length,
                current_start,
                id
            ))

            id += 1

        current_start += length

    for file in reversed(files):
        for gap in gaps:
            if file.length <= gap.length and file.start > gap.start:
                file.start = gap.start
                gap.start = gap.start + file.length
                gap.length -= file.length
                break

    checksum = 0
    for file in files:
        checksum += (((file.length - 1) *(file.length ))//2 + file.length * file.start) * file.id

    return checksum

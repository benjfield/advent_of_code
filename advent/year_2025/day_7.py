from typing import Self
from advent.runner import register
from advent.utils.split_text import create_char_grid
from advent.utils.grid import Grid
from dataclasses import dataclass
from functools import cache

@register(7, 2025, 1, True)
def splitter_1(text):
    splitters = []    
    beams = set()
    for i, char in enumerate(text[0]):
        if char == "S":
            beams.add(i)
    
    for line in text[1:]:
        splitters.append(set())
        for j, char in enumerate(line):
            if char == "^":
                splitters[-1].add(j)

    splitters = [x for x in splitters if len(x) > 0]

    split_count = 0

    for row_splitters in splitters:
        new_beams = set()
        for beam in beams:
            if beam in row_splitters:
                split_count += 1
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
            else:
                new_beams.add(beam)
        beams = new_beams

    return split_count


all_splitters = None

@cache
def recursive_splitters_2(beam_value, level):
    if level == len(all_splitters) - 1:
        if beam_value in all_splitters[level]:
            return 2
        else:
            return 1
    else:
        if beam_value in  all_splitters[level]:
            return recursive_splitters_2(
                beam_value-1,
                level + 1,
            ) + recursive_splitters_2(
                beam_value + 1,
                level + 1,
            )
        else:
            return recursive_splitters_2(
                beam_value,
                level + 1,
            )
        
#Alternative would be the same approach as before but with a dict of counts, this would be faster but above is fine.
@register(7, 2025, 2, True)
def splitter_2(text):
    splitters = []    
    for i, char in enumerate(text[0]):
        if char == "S":
            beam_value = i
    
    for line in text[1:]:
        splitters.append(set())
        for j, char in enumerate(line):
            if char == "^":
                splitters[-1].add(j)

    global all_splitters
    all_splitters = [x for x in splitters if len(x) > 0]

    return recursive_splitters_2(
        beam_value=beam_value,
        level=0,
    )
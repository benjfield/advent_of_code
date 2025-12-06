from typing import Self
from advent.runner import register
from advent.utils.split_text import create_char_grid
from advent.utils.grid import Grid
from dataclasses import dataclass

@dataclass
class Range:
    min_value: int
    max_value: int

    @classmethod
    def from_range_text(cls: Self, range_text: str) -> Self:
        range_split = range_text.split("-")
        return cls(
            min_value=int(range_split[0]), 
            max_value=int(range_split[1]),
        )

    def within(self: Self, value: int) -> bool:
        return value >= self.min_value and value <= self.max_value
    
    def add_other_range(self: Self, other_range: Self) -> Self:
        if other_range.max_value < self.min_value or other_range.min_value > self.max_value:
            return other_range
        
        self.max_value = max(self.max_value, other_range.max_value)
        self.min_value = min(self.min_value, other_range.min_value)

        return None
    
    def size(self: Self):
        return self.max_value - self.min_value + 1

@register(5, 2025, 1, True)
def fresh_1(text):
    is_fresh_range = True
    fresh_ranges = []
    fresh_count = 0

    for line in text:
        if line == "":
            is_fresh_range = False
        elif is_fresh_range:
            fresh_ranges.append(Range.from_range_text(line))
        else:
            ingredient = int(line)
            for fr in fresh_ranges:
                if fr.within(ingredient):
                    fresh_count += 1
                    break

    return fresh_count

@register(5, 2025, 2, True)
def fresh_2(text):
    fresh_ranges = []

    for line in text:
        if line == "":
            break
        else:
            fresh_ranges.append(Range.from_range_text(line))

    ranges_unchanged = False
    while not ranges_unchanged:
        new_ranges = []
        for fr in fresh_ranges:
            for nr in new_ranges:
                fr = nr.add_other_range(fr)
                if fr is None:
                    break

            if fr is not None:
                new_ranges.append(fr)

        if len(new_ranges) == len(fresh_ranges):
            ranges_unchanged = True
        fresh_ranges = new_ranges

    fresh_count = 0
    for fr in fresh_ranges:
        fresh_count += fr.size()      

    return fresh_count
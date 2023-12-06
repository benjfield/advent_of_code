from day3 import *

test_text = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
def test_parts_1():
    assert parts_1(test_text) == 4361

def test_parts_2():
    assert parts_2(test_text) == 467835
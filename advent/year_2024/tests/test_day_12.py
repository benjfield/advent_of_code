from advent.year_2024.day_12 import *

text = '''AAAA
BBCD
BBCC
EEEC'''

def test_func_1_1():
    text = '''AAAA
BBCD
BBCC
EEEC'''

    assert func_1(text) == 140


def test_func_1_2():
    text = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''

    assert func_1(text) == 1930


def test_func_2_1():
    text = '''AAAA
BBCD
BBCC
EEEC'''

    assert func_2(text) == 80

def test_func_2_2():
    text = '''EEEEE
EXXXX
EEEEE
EXXXX
EEEEE'''

    assert func_2(text) == 236

def test_func_2_3():
    text = '''AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA'''

    assert func_2(text) == 32 + 28 * 12

def test_func_2_4():
    text = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''

    assert func_2(text) == 1206
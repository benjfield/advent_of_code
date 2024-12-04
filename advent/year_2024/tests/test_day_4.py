from advent.year_2024.day_4 import *


text = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''.split("\n")

def test_func_1():
    assert func_1(text) == 18

def test_mull_2():
    assert func_2(text) == 9
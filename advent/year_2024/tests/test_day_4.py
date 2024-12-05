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

def test_wordsearch_1():
    assert wordsearch_1(text) == 18

def test_wordsearch_2():
    assert wordsearch_2(text) == 9
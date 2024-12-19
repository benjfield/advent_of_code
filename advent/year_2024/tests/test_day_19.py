from advent.year_2024.day_19 import *

text_1 = '''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb'''

def test_func_1():
    assert func_1(text_1) == 6

def test_func_2():
    assert func_2(text_1) == 16

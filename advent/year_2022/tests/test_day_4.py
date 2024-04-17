from advent.year_2022.day_4 import *

text = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''.split("\n")

def test_camp_cleanup_1():
    assert camp_cleanup_1(text) == 2

def test_camp_cleanup_2():
    assert camp_cleanup_2(text) == 4
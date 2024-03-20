from advent.year_2020.day_2 import *

text = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''.split("\n")

def test_password_report_1():
    assert password_report_1(text) == 2

def test_password_report_2():
    assert password_report_2(text) == 1
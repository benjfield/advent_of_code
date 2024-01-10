from advent.year_2023.day_1 import *
def test_calibrate_1():
    question_text = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""

    assert calibrate_1(question_text) == 142

def test_calibrate_2():
    question_text = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

    assert calibrate_2(question_text) == 281
from advent.year_2021.day_1 import *

def test_sonar_1():
    text = '''199
200
208
210
200
207
240
269
260
263'''
    assert sonar_1(text) == 7

def test_sonar_2():
    text = '''199
200
208
210
200
207
240
269
260
263'''
    assert sonar_2(text) == 5
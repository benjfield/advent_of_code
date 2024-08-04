from advent.year_2017.day_2 import *

text_1 = '''5 1 9 5
7 5 3
2 4 6 8'''.split("\n")

def test_corrupt_checksum_1():
    assert corrupt_checksum_1(text_1) == 18
    
text_2 = '''5 9 2 8
9 4 7 3
3 8 6 5'''.split("\n")

def test_corrupt_checksum_2():
    assert corrupt_checksum_2(text_2) == 9
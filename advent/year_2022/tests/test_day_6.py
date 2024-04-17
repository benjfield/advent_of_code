from advent.year_2022.day_6 import *

def test_tuning_trouble_1_1():
    assert tuning_trouble_1(["mjqjpqmgbljsphdztnvjfqwrcgsmlb"]) == 7

def test_tuning_trouble_1_2():
    assert tuning_trouble_1(["bvwbjplbgvbhsrlpgdmjqwftvncz"]) == 5
    
def test_tuning_trouble_1_3():
    assert tuning_trouble_1(["nppdvjthqldpwncqszvftbrmjlhg"]) == 6
from advent.year_2023.day_9 import *

test_text="""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""    

def test_sequence_1():
    assert sequence_1(test_text) == 114

def test_sequence_1_2():
    test_text="""7 10 23 68 188 460 1016 2078 4010 7382 13028 22062 35793 55452 81611 113136 145473 168018 160269 86400 -112166"""    
    assert sequence_1(test_text) == -526676

def test_sequence_1_3():
    test_text="""9 15 36 90 202 414 817 1611 3207 6404 12720 25069 49235 97138 193942 392967 805641 1659073 3402208 6894216 13727420"""    
    assert sequence_1(test_text) == 26763778

def test_sequence_1_4():
    test_text="""-3 -1 10 39 110 277 661 1525 3403 7298 14962 29268 54680 97822 168141 278652 446745 695025 1052146 1553589 2242322"""    
    assert sequence_1(test_text) == 3169267
    
def test_sequence_2():
    assert sequence_2(test_text) == 2
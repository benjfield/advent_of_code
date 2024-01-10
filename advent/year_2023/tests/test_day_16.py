from advent.year_2023.day_16 import *

test_text=r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""  

def test_energise_1():
    assert energise_1(test_text) == 46
    
def test_energise_2():
    assert energise_2(test_text) == 51
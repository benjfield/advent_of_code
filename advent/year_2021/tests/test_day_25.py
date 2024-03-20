from advent.year_2021.day_25 import *

def test_amphipod_1():
    text = '''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>'''
    assert cucumber_1(text) == 58
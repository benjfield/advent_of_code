from advent.year_2022.day_25 import *

text = '''1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122'''.split("\n")

def test_full_of_hot_air_1():
    assert full_of_hot_air_1(text) == "2=-1=0"
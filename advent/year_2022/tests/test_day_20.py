from advent.year_2022.day_20 import *

text = '''1
2
-3
3
-2
0
4'''.split("\n")

def test_grove_positioning_system_1():
    assert grove_positioning_system_1(text) == 3

def test_grove_positioning_system_2():
    assert grove_positioning_system_2(text) == 1623178306

text_2='''8
2
32
-41
6
29
-4
6
-8
8
-3
-8
3
-5
0
-1
2
1
10
-9'''.split("\n")

#def test_grove_positioning_system_1_2():
#    assert grove_positioning_system_1(text_2) == [0, -1, -8, -41, -8, 2, -4, 1, -5, -3, 2, 8, 6, 6, 29, 32, 10, 3, -9, 8]
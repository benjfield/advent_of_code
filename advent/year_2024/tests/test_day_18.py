from advent.year_2024.day_18 import *

text_1 = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''

def test_func_1():
    assert func_1(text_1, 12, 6) == 22

def test_func_2():
    assert func_2(text_1, 6) == (6, 1)

from advent.year_2021.day_15 import *

def test_chiton_1():
    text = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''

    assert chiton_1(text) == 40

def test_chiton_2():
    text = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''

    assert chiton_2(text) == 315
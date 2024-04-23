from advent.year_2022.day_8 import *

text = '''30373
25512
65332
33549
35390'''.split("\n")

def test_treetop_tree_house_1():
    assert treetop_tree_house_1(text) == 21
    
def test_treetop_tree_house_2():
    assert treetop_tree_house_2(text) == 8
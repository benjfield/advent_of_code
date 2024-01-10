from advent.year_2023.day_15 import *

test_text="""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""    

def test_hash_1():
    assert hash_1(test_text) == 1320
    
def test_hash_2():
    assert hash_2(test_text) == 145
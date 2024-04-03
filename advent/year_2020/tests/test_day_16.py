from advent.year_2020.day_16 import *

def test_ticket_translation_1():
    text = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''.split("\n")
    
    assert ticket_translation_1(text) == 71
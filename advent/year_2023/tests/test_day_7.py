from advent.year_2023.day_7 import *

test_text="""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

test_text_2="""A833A 309
Q33J3 205
55KK5 590
K4457 924
Q3QT3 11
QJK32 349
96659 162
955A9 851
33888 311
57JJ7 721"""

def test_poker_1():    
    assert poker_1(test_text) == 6440

def test_poker_1_2():
    assert poker_1(test_text_2) == 349 + 2 * 924 + 3 * 721 + 4 * 851 + 5 * 162 + 6 * 11 + 7 * 309 + 8 * 205 + 9 * 311 + 10 * 590

def test_poker_2():    
    assert poker_2(test_text) == 5905
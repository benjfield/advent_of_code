from advent.year_2021.day_21 import *

def test_dice_roll_1():
    text = '''Player 1 starting position: 4
Player 2 starting position: 8'''
    assert dice_roll_1(text) == 739785
    
def test_dice_roll_2():
    text = '''Player 1 starting position: 4
Player 2 starting position: 8'''
    assert dice_roll_2(text) == 444356092776315
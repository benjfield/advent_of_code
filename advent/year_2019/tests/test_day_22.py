from advent.year_2019.day_22 import *

def test_deck_new_stack():
    deck = Deck(size=10)

    deck.new_stack()

    assert deck.cards == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    
def test_deck_cut_1():
    deck = Deck(size=10)

    deck.cut(3)

    assert deck.cards == [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
        
def test_deck_cut_2():
    deck = Deck(size=10)

    deck.cut(-4)

    assert deck.cards == [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]

def test_deck_deal():
    deck = Deck(size=10)

    deck.deal(3)

    assert deck.cards == [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]

def test_deck_deal():
    deck = Deck(size=10)

    deck.deal(3)

    assert deck.cards == [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]

def test_commands_1():
    text = '''deal with increment 7
deal into new stack
deal into new stack'''

    deck = Deck(10)

    deck.run_commands(text)

    assert deck.cards == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]

def test_commands_2():
    text = '''cut 6
deal with increment 7
deal into new stack'''

    deck = Deck(10)

    deck.run_commands(text)

    assert deck.cards == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]
    
def test_commands_3():
    text = '''deal with increment 7
deal with increment 9
cut -2'''

    deck = Deck(10)

    deck.run_commands(text)

    assert deck.cards == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]

def test_commands_4():
    text = '''deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1'''

    deck = Deck(10)

    deck.run_commands(text)

    assert deck.cards == [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]

def test_shuffle_1():
    text = '''deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1'''

    shuffle_1(text, 10, 4) == 5
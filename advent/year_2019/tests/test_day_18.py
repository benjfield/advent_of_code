from advent.year_2019.day_18 import *
from cProfile import Profile
from pstats import SortKey, Stats


def test_keys_1_1():
    text = '''#########
#b.A.@.a#
#########'''

    assert keys_1(text) == 8
    
def test_keys_1_2():
    text = '''########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################'''

    assert keys_1(text) == 86
        
def test_keys_1_3():
    text = '''########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################'''

    assert keys_1(text) == 132
            
def test_keys_1_4():
    text = '''#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################'''
    #with Profile() as profile:
    #    print(f"{keys_1(text)}")
    #    (
    #        Stats(profile)
    #        .strip_dirs()
    #        .sort_stats(SortKey.TIME)
    #        .print_stats()
    #    )
    #assert False
    #assert keys_1(text) == 136
                
def test_keys_1_5():

    text = '''########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################'''

    assert keys_1(text) == 81

def test_keys_2_1():
    text = '''#######
#a.#Cd#
##...##
##.@.##
##...##
#cB#.b#
#######'''

    assert keys_2(text, False) == 8
from advent.year_2019.day_1 import *

def test_mass_1_1():
    assert mass_1("12") == 2
    
def test_mass_1_2():
    assert mass_1("14") == 2
    
def test_mass_1_3():
    assert mass_1("1969") == 654
    
def test_mass_1_4():
    assert mass_1("100756") == 33583
    
def test_mass_2_1():
    assert mass_2("14") == 2  

def test_mass_2_2():
    assert mass_2("1969") == 966
        
def test_mass_2_3():
    assert mass_2("100756") == 50346
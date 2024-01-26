from advent.year_2019.day_16 import *

def test_fft_1_1():
    text='''12345678'''

    assert fft_1(text, 1) == "48226158"

def test_fft_1_2():
    text='''12345678'''

    assert fft_1(text, 2) == "34040438"
    
def test_fft_1_3():
    text='''12345678'''

    assert fft_1(text, 3) == "03415518"

def test_fft_1_4():
    text='''12345678'''

    assert fft_1(text, 4) == "01029498"
    
def test_fft_1_5():
    text='''80871224585914546619083218645595'''

    assert fft_1(text) == "24176176"

def test_fft_1_6():
    text='''19617804207202209144916044189917'''

    assert fft_1(text) == "73745418"
    
def test_fft_1_7():
    text='''69317163492948606335995924319873'''

    assert fft_1(text) == "52432133"
        
def test_fft_2_1():
    text='''03036732577212944063491565474664'''

    assert fft_2(text) == "84462026"
            
def test_fft_2_2():
    text='''02935109699940807407585447034323'''

    assert fft_2(text) == "78725270"
                
def test_fft_2_3():
    text='''03081770884921959731165446850517'''

    assert fft_2(text) == "53553731"
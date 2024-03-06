from advent.year_2021.day_16 import *

def test_initial_process():
    text = '''D2FE28'''

    assert initial_process(text) == "110100101111111000101000"

def test_process_packet_type_4():
    text = '''110100101111111000101000'''

    assert process_packet(text, 0) == (2021, "", 6)
    
def test_process_packet_type_6_length_type_0():
    text = '''00111000000000000110111101000101001010010001001000000000'''

    assert process_packet(text, 0) == (1, "", 9)
        
def test_process_packet_type_3_length_type_1():
    text = '''11101110000000001101010000001100100000100011000001100000'''

    assert process_packet(text, 0) == (3, "", 14)
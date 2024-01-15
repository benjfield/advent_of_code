from advent.year_2019.computer import Computer

def test_boost_1_1():
    this_computer = Computer("109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99")
    assert this_computer.process() == (True, [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
    
def test_boost_1_2():
    this_computer = Computer("1102,34915192,34915192,7,4,7,99,0")
    assert this_computer.process() == (True, [1219070632396864])
        
def test_boost_1_3():
    this_computer = Computer("104,1125899906842624,99")
    assert this_computer.process() == (True, [1125899906842624])
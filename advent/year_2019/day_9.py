from advent.runner import register
from advent.year_2019.computer import Computer

@register(9, 2019, 1)
def boost_1(text):
    this_computer = Computer(text)

    results = this_computer.process([1])

    if results[0] and len(results[1]) == 1:
        return results[1][0]
    else:
        raise Exception("Incorrect response")
    
@register(9, 2019, 2)
def boost_2(text):
    this_computer = Computer(text)

    results = this_computer.process([2])

    if results[0] and len(results[1]) == 1:
        return results[1][0]
    else:
        raise Exception("Incorrect response")
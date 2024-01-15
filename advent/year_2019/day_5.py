from advent.runner import register
from advent.year_2019.computer import Computer

@register(5, 2019, 1)
def state_1(text):
    this_computer = Computer(text)

    finished, outputs = this_computer.process(1)

    for check in outputs[:-1]:
        if check != 0:
            raise Exception("Diagnostic failed")

    return outputs[-1]

@register(5, 2019, 2)
def state_1(text):
    this_computer = Computer(text)

    finished, outputs = this_computer.process(5)

    for check in outputs[:-1]:
        if check != 0:
            raise Exception("Diagnostic failed")

    return outputs[-1]
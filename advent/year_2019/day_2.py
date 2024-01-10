from advent.runner import register
from advent.year_2019.computer import Computer

@register(2, 2019, 1)
def state_1(text):
    this_computer = Computer(text)

    this_computer.state[1] = 12
    this_computer.state[2] = 2

    this_computer.process()

    return this_computer.state[0]

@register(2, 2019, 2)
def state_2(text):
    for noun in range(100):
        for verb in range(100):
            this_computer = Computer(text)

            this_computer.state[1] = noun
            this_computer.state[2] = verb

            this_computer.process()

            if this_computer.state[0] == 19690720:
                return 100 * noun + verb
            
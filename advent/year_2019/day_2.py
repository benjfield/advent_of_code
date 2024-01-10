from advent.runner import register
class Computer:
    def __init__(self, state):
        self.state = [ int(x) for x in state.split(",") ]
        self.process_index = 0

    def process(self):
        for i in range(0, len(self.state), 4):
            if self.state[i] == 1:
                self.state[self.state[i+3]] = self.state[self.state[i+1]] + self.state[self.state[i+2]]
            elif self.state[i] == 2:
                self.state[self.state[i+3]] = self.state[self.state[i+1]] * self.state[self.state[i+2]]
            elif self.state[i] == 99:
                break
            else:
                raise Exception("Unknown")

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
            
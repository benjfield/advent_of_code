from advent.runner import register
from advent.year_2019.computer import computer_from_string, process
import itertools

@register(7, 2019, 1)
def amp_1(text):
    this_computer = computer_from_string(text)

    max_output = 0
    for input in itertools.permutations([0,1,2,3,4]):
        output = [0]
        for setting in input:
            this_computer.reset()
            finished, output = process(this_computer, [setting, output[0]])
        if output[0] > max_output:
            max_output = output[0]

    return max_output
    
@register(7, 2019, 2)
def amp_2(text):
    max_output = 0
    computers = []
    for i in range(5):
        computers.append(computer_from_string(text))

    for setting_permutation in itertools.permutations([5,6,7,8,9]):
        for computer in computers:
            computer.reset()

        finished = False
        first_run = True
        output = [0]
        while not finished:
            for i, this_setting in enumerate(setting_permutation):
                if first_run:
                    input = [this_setting, output[0]]
                else:
                    input = output
                finished, output = process(computers[i], input)
            first_run = False
        if output[0] > max_output:
            max_output = output[0]

    return max_output

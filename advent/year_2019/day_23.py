from advent.runner import register
from advent.year_2019.computer import computer_from_string, process, print_output_as_ascii
import copy

@register(23, 2019, 1)
def springboard_1(text):
    computers = []
    messages = []
    blank_messages = []
    for i in range(50):
        computer = computer_from_string(text)
        computers.append(computer)
        messages.append([i])
        blank_messages.append([])

    while True:
        next_messages = copy.deepcopy(blank_messages)

        for i, queue in enumerate(messages):
            if len(queue) == 0:
                input = [-1]
            else:
                input = queue
            finished, output = process(computers[i], input)
            
            for index in range(0, len(output), 3):
                if output[index] == 255:
                    return output[index+2]
                next_messages[output[index]].append(output[index + 1])
                next_messages[output[index]].append(output[index + 2])

        messages = next_messages

@register(23, 2019, 2)
def springboard_1(text):
    computers = []
    messages = []
    blank_messages = []
    for i in range(50):
        computer = computer_from_string(text)
        computers.append(computer)
        messages.append([i])
        blank_messages.append([])

    nat_x = 0
    nat_y = 0

    prior_y = set()

    next_len = 50

    while True:
        next_messages = copy.deepcopy(blank_messages)

        if next_len == 0:
            messages[0] = [nat_x, nat_y]
            if nat_y in prior_y:
                return nat_y
            prior_y.add(nat_y)

        next_len = 0
        for i, queue in enumerate(messages):
            if len(queue) == 0:
                input = [-1]
            else:
                input = queue
            finished, output = process(computers[i], input)
            
            for index in range(0, len(output), 3):
                if output[index] == 255:
                    nat_x = output[index + 1]
                    nat_y = output[index + 2]
                else:
                    next_messages[output[index]].append(output[index + 1])
                    next_messages[output[index]].append(output[index + 2])
                next_len += 1
        
        messages = next_messages
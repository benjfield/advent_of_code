from advent.runner import register
from advent.year_2019.computer import computer_from_string, process, print_output_as_ascii
import cmd

@register(25, 2019, 1)
def droid_1(text):
    computer = computer_from_string(text)

    this_input = []

    while True:
        finished, output = process(computer, this_input)

        print_output_as_ascii(output)
        cmd_input = input()

        this_input = [ ord(char) for char in cmd_input ]
        this_input.append(10)

    return
            

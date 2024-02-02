
from advent.runner import register
from advent.year_2019.computer import computer_from_string, process, print_output_as_ascii

@register(21, 2019, 1)
def springboard_1(text):
    computer = computer_from_string(text)

    commands = [
        #Hole at A
        "NOT A J",
        #Hole at a or b
        "NOT B T",
        "OR T J",
        #Hole at a or b or c
        "NOT C T",
        "OR T J",
        #has 4
        "AND D J",
        "WALK"
    ]

    input = []
    
    for command in commands:
        for letter in command:
            input.append(ord(letter))
        input.append(10)

    finished, output = process(computer, input)

    return print_output_as_ascii(output)

@register(21, 2019, 2)
def springboard_1(text):
    computer = computer_from_string(text)

    commands = [
        #Hole at A
        "NOT A J",
        #Hole at a or b
        "NOT B T",
        "OR T J",
        #Hole at a or b or c
        "NOT C T",
        "OR T J",
        "AND D J",
        
        #5 and 6 or 9
        "NOT J T",
        "OR I T",
        "OR F T",
        "AND E T",
        
        #or 8
        "OR H T",

        #has 4 and 8
        "AND T J",

        "RUN"
    ]

    input = []
    
    for command in commands:
        for letter in command:
            input.append(ord(letter))
        input.append(10)

    finished, output = process(computer, input)

    return print_output_as_ascii(output)
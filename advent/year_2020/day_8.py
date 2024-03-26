from advent.runner import register
from enum import Enum

@register(8, 2020, 1, True)
def handheld_halting_1(split_text):
    acc = 0
    i = 0
    visited = set()
    while True:
        line = split_text[i]
        visited.add(i)
        split_line = line.split(" ")
        number = int(split_line[1])
        match split_line[0]:
            case "acc":
                acc += number
                i += 1
            case "jmp":
                i += number
            case "nop":
                i += 1

        if i in visited:
            return acc

class Command(Enum):
    ACC = 0
    JMP = 1
    NOP = 2

    def switch(self):
        if self == Command.ACC:
            return self
        elif self == Command.JMP:
            return self.NOP
        else:
            return self.JMP

    @classmethod
    def get_command(cls, command_string):
        match command_string:
            case "acc":
                return cls.ACC
            case "jmp":
                return cls.JMP
            case "nop":
                return cls.NOP

@register(8, 2020, 2, True)
def handheld_halting_2(split_text):
    rules = []
    indexes_to_switch = []

    for i, line in enumerate(split_text):
        split_line = line.split(" ")
        command = Command.get_command(split_line[0])
        rules.append((command, int(split_line[1])))
        if command != Command.ACC:
            indexes_to_switch.append(i)

    for index_to_switch in indexes_to_switch:
        acc = 0
        i = 0
        visited = set()
        while i not in visited:
            rule = rules[i]
            if i == index_to_switch:
                command = rule[0].switch()
            else:
                command = rule[0]
            number = rule[1]
            visited.add(i)

            match command:
                case Command.ACC:
                    acc += number
                    i += 1
                case Command.JMP:
                    i += number
                case Command.NOP:
                    i += 1

            if i >= len(rules):
                return acc

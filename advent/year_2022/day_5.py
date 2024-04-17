from advent.runner import register
import math
import re

def build_stacks(split_text):    
    stacks = []
    for i, line in enumerate(split_text):
        if len(line) == 0:
            start_of_instructions = i + 1
            break
        else:
            if line[1] != "1":
                for j in range(math.ceil(len(line)/4)):
                    if i == 0:
                        stacks.append([])
                    if line[4 * j + 1] != " ":
                        stacks[j].append(line[4 * j + 1])

    for stack in stacks:
        stack.reverse()

    return stacks, start_of_instructions

@register(5, 2022, 1, True)
def supply_stacks_1(split_text):
    stacks, start_of_instructions = build_stacks(split_text)

    for instruction in split_text[start_of_instructions:]:
        parsed_instruction = re.search(r"move (\d+) from (\d+) to (\d+)", instruction)

        source_stack = int(parsed_instruction.group(2)) - 1
        destination_stack = int(parsed_instruction.group(3)) - 1

        number_of_times = int(parsed_instruction.group(1))

        for i in range(number_of_times):
            value = stacks[source_stack].pop()
            stacks[destination_stack].append(value)

    result = ""
    for stack in stacks:
        result += stack[-1]

    return result

@register(5, 2022, 2, True)
def supply_stacks_2(split_text):
    stacks, start_of_instructions = build_stacks(split_text)

    for instruction in split_text[start_of_instructions:]:
        parsed_instruction = re.search(r"move (\d+) from (\d+) to (\d+)", instruction)

        source_stack = int(parsed_instruction.group(2)) - 1
        destination_stack = int(parsed_instruction.group(3)) - 1

        number_of_times = int(parsed_instruction.group(1))

        stacks[destination_stack] += stacks[source_stack][-1 * number_of_times:]
        stacks[source_stack] = stacks[source_stack][:-1 * number_of_times]

    result = ""
    for stack in stacks:
        result += stack[-1]

    return result
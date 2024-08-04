import re
from advent.runner import register

@register(6, 2017, 1, False)
def realloc_1(text, length = 16):
    memory = [0 for _ in range(length)]
    for i, value in enumerate(text.split()):
        print(i, value)
        memory[i] = int(value)

    print(memory)

    states = set(tuple(memory))

    realloc_count = 0
    while True:
        max = 0
        index = 0
        for i, value in enumerate(memory): 
            if value > max:
                max = value
                index = i
            
        memory[index] = 0

        for i in range(index + 1, index + max + 1):
            memory[i%len(memory)] += 1

        realloc_count += 1

        state = tuple(memory)
        print(memory)
    
        if state in states:
            return realloc_count
        states.add(state)  
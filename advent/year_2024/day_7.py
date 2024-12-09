from advent.runner import register
import math

@register(7, 2024, 1, True)
def func_1(text):
    total = 0

    for line in text:
        split_by_colon = line.split(": ")
        answer = int(split_by_colon[0])
          
        values = [int(x) for x in split_by_colon[1].split(" ")]
        
        for combo in range(2**(len(values) - 1)):
            this_answer = values[0]

            for i in range(len(values) - 1):
                if combo & 2**i:
                    this_answer *= values[i + 1]
                else:
                    this_answer += values[i + 1]

            if this_answer == answer:
                total += answer
                break

    return total

@register(7, 2024, 2, True)
def func_2(text):
    total = 0

    for line in text:
        split_by_colon = line.split(": ")
        answer = int(split_by_colon[0])
          
        values = [int(x) for x in split_by_colon[1].split(" ")]
         
        answers = [values[0]]
        for i in range(1, len(values)):
            new_answers = []
            for a in answers:
                if a <= answer:
                    new_answers.append(a + values[i])
                    new_answers.append(a * values[i])
                    new_answers.append(a * 10**math.ceil(math.log10(values[i] + 1)) + values[i] )
            answers = new_answers

        for pot_answer in answers:
            if pot_answer == answer:
                total += answer
                break

    return total

def func_2_2(text):
    total = 0

    for line in text:
        split_by_colon = line.split(": ")
        answer = int(split_by_colon[0])
          
        values = [int(x) for x in split_by_colon[1].split(" ")]
        
        for combo in range(3**(len(values) - 1)):
            this_answer = values[0]

            for i in range(len(values) - 1):
                index = 3 ** (len(values) - (2 + i))

                enum = combo // index
                combo = combo % index

                if enum == 2:
                    this_answer *= 10**math.ceil(math.log10(values[i + 1] + 1))
                    this_answer += values[i + 1]
                elif enum == 1:
                    this_answer *= values[i + 1]
                else:
                    this_answer += values[i + 1]
                
                if this_answer > answer:
                    break

            if this_answer == answer:
                total += answer
                break

    return total
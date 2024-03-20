from advent.runner import register

@register(24, 2021, 1)
def monad_1(text):    
    monad_details = get_monad_details(text)

    final_answers = check_inputs(monad_details)

    return final_answers[-1]

@register(24, 2021, 2)
def monad_2(text):    
    monad_details = get_monad_details(text)

    final_answers = check_inputs(monad_details)

    return final_answers[-1]

def monad(initial_z, input, divisor, additive_1, additive_2):
    if initial_z % 26 == input - additive_1:
        return int(initial_z / divisor)
    else:
        return 26 * int(initial_z / divisor) + input + additive_2
    
def monad_reverse(final_z, input, divisor, additive_1, additive_2):
    possible_numbers = []
    initial_modulo = input - additive_1
    if initial_modulo >= 0 and initial_modulo <= 25:
        number = final_z * divisor
        for i in range(divisor):
            if (number + i) % 26 == initial_modulo:
                possible_numbers.append(number + i)

    number = final_z - (input + additive_2)
    
    if number % 26 == 0:
        number = int(number / 26) * divisor
        for i in range(divisor):
            if (number + i) % 26 != initial_modulo:
                possible_numbers.append(number + i)

    return list(possible_numbers)

def get_monad_details(text):
    split_text = text.split("\n")
    monad_details = []
    for i in range(0, len(split_text), 18):
        divisor = int(split_text[i + 4].split(" ")[2])
        additive_1 = int(split_text[i + 5].split(" ")[2])
        additive_2 = int(split_text[i + 15].split(" ")[2])

        monad_details.append((divisor, additive_1, additive_2))
    
    return monad_details

def process_rules_monad(monad_details, model_number):
    model_number_string = str(model_number)
    z = 0
    for i, details in enumerate(monad_details):
        z = monad(z, int(model_number_string[i]), details[0], details[1], details[2])

    return z

def build_answers(all_answers, initial_z, digit):
    ten_multiplier = (10 ** (13 - digit))
    these_numbers = []
    for answer in all_answers[(initial_z, digit)]:
        answer_number = answer[0] * ten_multiplier
        if digit == 13:
            these_numbers.append(answer_number)
        else:
            for sub_answer in build_answers(all_answers, answer[1], digit + 1):
                these_numbers.append(sub_answer + answer_number)
    return these_numbers

def check_inputs(monad_details):
    all_answers = {}

    backwards_answers = {0}
    for digit in range(13, -1, -1):
        print(digit)
        next_answers = set()
        for final_z in backwards_answers:
            for input in range(1, 10):
                possible_initials = monad_reverse(final_z, input, monad_details[digit][0], monad_details[digit][1], monad_details[digit][2])
                for initial in possible_initials:
                    next_answers.add(initial)
                    answer_key = (initial, digit)
                    answer_answer = (input, final_z)
                    if answer_key in all_answers:
                        all_answers[answer_key].append(answer_answer)
                    else:
                        all_answers[answer_key] = [answer_answer]
        backwards_answers = next_answers

    final_answers = build_answers(all_answers, 0, 0)

    final_answers.sort()

    return final_answers

def process_rules_naive(text, model_number):
    split_text = text.split("\n")

    data = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    model_number_string = str(model_number)

    model_index = 0
    for i, line in enumerate(split_text):
        instruction = line.split(" ")

        if len(instruction) == 3:
            if instruction[2] in data.keys():
                second_variable = data[instruction[2]]
            else:
                second_variable = int(instruction[2])
        match instruction[0]:
            case "inp":
                data[instruction[1]] = int(model_number_string[model_index])
                model_index += 1
            case "add":
                data[instruction[1]] += second_variable
            case "mul":
                data[instruction[1]] *= second_variable
            case "div":
                data[instruction[1]] = int(data[instruction[1]]/second_variable)
            case "mod":
                data[instruction[1]] = data[instruction[1]] % second_variable
            case "eql":
                if data[instruction[1]] == second_variable:
                    data[instruction[1]] = 1
                else:
                    data[instruction[1]] = 0

    return data["z"]

            


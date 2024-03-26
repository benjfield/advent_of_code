from advent.runner import register

def find_invalid_number(numbers, preamble):
    check = set()
    for i in range(preamble):
        check.add(numbers[i])

    for i in range(preamble, len(numbers)):
        valid_number = False
        for j in range(0, preamble):
            number_to_test = numbers[i] - numbers[i - j]

            if number_to_test in check:
                valid_number = True
                check.remove(numbers[i - preamble])
                check.add(numbers[i])
                break

        if not valid_number:
            return numbers[i], i

@register(9, 2020, 1, True)
def encoding_error_1(split_text, preamble=25):
    numbers = [int(x) for x in split_text]

    number, i = find_invalid_number(numbers, preamble)

    return number

        
@register(9, 2020, 2, True)
def encoding_error_2(split_text, preamble=25):
    numbers = [int(x) for x in split_text]

    invalid_number, invalid_number_index = find_invalid_number(numbers, preamble)

    for length in range(2, invalid_number_index + 1):
        for i in range(0, invalid_number_index - length):
            test = sum(numbers[i:i+length])

            if test == invalid_number:
                return max(numbers[i:i+length]) + min(numbers[i:i+length])
from advent.runner import register

@register(16, 2019, 1)
def fft_1(text, passes=100):
    number_array = [ int(x) for x in text ]

    for pass_number in range(passes):
        for i in range(len(number_array)):
            total = 0
            index = i
            while index < len(number_array):
                j = 0
                while j < i + 1:
                    calc_index = index + j
                    if calc_index >= len(number_array):
                        break
                    else:
                        total += number_array[calc_index]
                    j += 1
                index += 4 * (i + 1)

            index = i + 2 * (i+1)
            while index < len(number_array):
                j = 0
                while j < i + 1:
                    calc_index = index + j
                    if calc_index >= len(number_array):
                        break
                    else:
                        total -= number_array[calc_index]
                    j += 1
                index += 4 * (i + 1)

            number_array[i] = (abs(total))%10
    print(text)
    print("".join([ str(x) for x in number_array]))
    return "".join([ str(x) for x in number_array[:8]])

@register(16, 2019, 2)
def fft_2(text, passes=100):
    initial_number_array = [ int(x) for x in text ]

    number_array = []
    for i in range(10000):
        number_array += (initial_number_array)

    starting_point = int("".join([ str(x) for x in number_array[:7]]))

    if starting_point < len(number_array)/2:
        raise Exception("Not implemented")

    calced_numbers = []

    for number in range(0, 8):
        total = 0
        prior_multiplier = 1
        for index, number in enumerate(number_array[starting_point+number:]):
            if index == 0:
                total += number
            else:
                prior_multiplier = prior_multiplier * (passes + index -1) // (index)

                total += prior_multiplier * number

        calced_numbers.append(total%10) 

    return "".join([ str(x) for x in calced_numbers])
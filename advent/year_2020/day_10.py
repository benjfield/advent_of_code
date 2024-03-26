from advent.runner import register
import functools

def check_voltage(numbers, used_adapters):
    if len(numbers) == 0:
        return used_adapters
    else:
        these_numbers = numbers.copy()
        while used_adapters[-1] >= numbers[-1] -3:
            next_number = these_numbers.pop()
            these_used_adapters = used_adapters.copy()
            these_used_adapters.append(next_number)

            returned_used_adapters = check_voltage(these_numbers, these_used_adapters)
            if returned_used_adapters is not None:
                return returned_used_adapters

        return None  

@register(10, 2020, 1, True)
def adapter_array_1(split_text):
    numbers = [int(x) for x in split_text]

    numbers.sort(reverse=True)

    used_adapters = check_voltage(numbers, [0])

    diff_1 = 0
    diff_3 = 1

    for i in range(len(used_adapters) - 1):
        diff = used_adapters[i + 1] - used_adapters[i]
        if diff == 3:
            diff_3 += 1
        elif diff == 1:
            diff_1 += 1
        else:
            raise Exception
    
    return diff_1 * diff_3

@functools.cache
def check_adapter_counts(numbers, index):
    if index == len(numbers) - 1:
        return 1
    else:
        this_index = index + 1
        total = 0
        while this_index < len(numbers) and numbers[index] >= numbers[this_index] -3:
            total += check_adapter_counts(numbers, this_index)

            this_index += 1

        return total 
    
@register(10, 2020, 2, True)
def adapter_array_2(split_text):
    numbers = [int(x) for x in split_text]

    numbers.sort()

    numbers = [0] + numbers

    return check_adapter_counts(tuple(numbers), 0)
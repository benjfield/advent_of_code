from advent.runner import register

@register(23, 2020, 1, True)
def crab_cups_1(split_text):
    numbers = [int(x) for x in split_text[0]]
    
    current_cup = 0
    for move_count in range(100):
        number_1 = numbers[(current_cup + 1) % 9]
        number_2 = numbers[(current_cup + 2) % 9]
        number_3 = numbers[(current_cup + 3) % 9]

        target_number = numbers[current_cup] - 1
        if target_number == 0:
            target_number = 9
            
        while target_number == number_1 or target_number == number_2 or target_number == number_3:
            target_number = target_number - 1
            if target_number == 0:
                target_number = 9

        for j in range(4, 9):
            index = (current_cup + j) % 9
            
            if numbers[index] == target_number:
                for i in range(1, j - 2):
                    destination_index = (current_cup + i) % 9
                    source_index = (current_cup + i + 3) % 9
                    numbers[destination_index] = numbers[source_index]
                
                numbers[(current_cup + j - 2) % 9] = number_1
                numbers[(current_cup + j - 1) % 9] = number_2
                numbers[(current_cup + j) % 9] = number_3     

        current_cup = (current_cup + 1) % 9

    total = 0
    for i, value in enumerate(numbers):
        if value == 1:
            for j in range(1, 9):
                total += numbers[(i + j) % 9] * 10 ** (8 - j)
            return total

@register(23, 2020, 2, True)
def crab_cups_2(split_text):
    numbers = [int(x) for x in split_text[0]]
    
    number_to_next = []

    for i in range(1000001):
        number_to_next.append(i + 1)

    for i in range(len(numbers) - 1):
        number_to_next[numbers[i]] = numbers[i + 1]

    #Could save a lot of memory by doing this implicitly in a dict but this should be slightly faster
    number_to_next[numbers[-1]] = 10
    
    number_to_next[1000000] = numbers[0]

    current_cup = numbers[0]
    for move_count in range(10000000):
        number_1 = number_to_next[current_cup]
        number_2 = number_to_next[number_1]
        number_3 = number_to_next[number_2]

        target_number = current_cup - 1
        if target_number == 0:
            target_number = 1000000
            
        while target_number == number_1 or target_number == number_2 or target_number == number_3:
            target_number = target_number - 1
            if target_number == 0:
                target_number = 1000000
        
        number_to_next[current_cup] = number_to_next[number_3]

        original_target = number_to_next[target_number]

        number_to_next[target_number] = number_1
        
        number_to_next[number_3] = original_target

        current_cup = number_to_next[current_cup]
    
    number_1 = number_to_next[1]
    number_2 = number_to_next[number_1]

    return number_1 * number_2
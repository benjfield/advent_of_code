from advent.runner import register

@register(5, 2020, 1, True)
def binary_boarding_1(split_text):
    max_seat_number = 0
    for line in split_text:
        line = line.replace("F", "0")
        line = line.replace("B", "1")
        line = line.replace("R", "1")
        line = line.replace("L", "0")

        seat_number = int(line, 2)
        if seat_number > max_seat_number:
            max_seat_number = seat_number

    return max_seat_number
    
@register(5, 2020, 2, True)
def binary_boarding_2(split_text):
    seat_numbers = []
    for line in split_text:
        line = line.replace("F", "0")
        line = line.replace("B", "1")
        line = line.replace("R", "1")
        line = line.replace("L", "0")

        seat_numbers.append(int(line, 2))
    
    seat_numbers.sort()

    for i in range(len(seat_numbers) - 1):
        if seat_numbers[i] == seat_numbers[i + 1] - 2:
            return seat_numbers[i] + 1
from advent.runner import register

def check_passcode_1(passcode):
    double = False
    last_number = 0

    for number in passcode:
        int_number = int(number)
        if int_number >= last_number:
            if int_number == last_number:
                double = True
            last_number = int_number
        else:
            return False

    if double:
        return True
    else:
        return False
    
@register(4, 2019, 1)
def passcode_1(text):
    split_text = text.split("-")
    count = 0
    for passcode in range(int(split_text[0]), int(split_text[1]) + 1):
        if check_passcode_1(str(passcode)):
            count += 1

    return count

def check_passcode_2(passcode):
    counts = {}
    last_number = 0

    for number in passcode:
        int_number = int(number)
        if int_number >= last_number:
            counts[int_number] = counts.get(int_number, 0) + 1
            last_number = int_number
        else:
            return False

    for value in counts.values():
        if value == 2:
            return True
    return False
    
@register(4, 2019, 2)
def passcode_2(text):
    split_text = text.split("-")
    count = 0
    for passcode in range(int(split_text[0]), int(split_text[1]) + 1):
        if check_passcode_2(str(passcode)):
            count += 1

    return count
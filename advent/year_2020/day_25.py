from advent.runner import register

@register(25, 2020, 1, True)
def combo_breaker_1(split_text):
    door_public_key = int(split_text[0])
    card_public_key = int(split_text[1])
    
    value = 1
    subject = 7
    loop_size = 0
    while True:
        loop_size += 1

        value = (value * subject) % 20201227

        if value == door_public_key:
            value_2 = 1
            for i in range(loop_size):
                value_2 = value_2 * card_public_key % 20201227
            return value_2
        elif value == card_public_key:
            value_2 = 1
            for i in range(loop_size):
                value_2 = value_2 * door_public_key % 20201227
            return value_2




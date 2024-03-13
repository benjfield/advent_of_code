from advent.runner import register
import itertools
rolls = [
    6,
    5,
    4,
    3,
    2,
    1,
    0,
    9,
    8,
    7
]

def get_start_position(text):
    split_text = text.split("\n")

    position_1 = int(split_text[0].split(": ")[1]) - 1
    position_2 = int(split_text[1].split(": ")[1]) - 1

    return position_1, position_2

@register(21, 2021, 1)
def dice_roll_1(text):
    roll = 0

    position_1, position_2 = get_start_position(text)

    total_1 = 0
    total_2 = 0

    while True:
        position_1 += rolls[roll % 10]
        position_1 = position_1 % 10
        total_1 += position_1 + 1
        roll += 1

        if total_1 >= 1000:
            return total_2 * roll * 3
        else:
            position_2 += rolls[roll % 10]
            position_2 = position_2 % 10
            total_2 += position_2 + 1
            roll += 1

            if total_2 >= 1000:
                return total_1 * roll * 3

def build_quantum_rolls():
    quantum_rolls = {}
    for roll_1 in range(1, 4):
        for roll_2 in range(1, 4):
            for roll_3 in range(1, 4):
                roll_total = roll_1 + roll_2 +roll_3
                quantum_rolls[roll_total] = quantum_rolls.get(roll_total, 0) + 1
    return quantum_rolls

def build_dice_universes(
        quantum_rolls,
        position,
        score,
        roll_number,
        count,
        final_scores,
    ):
    this_roll_number = roll_number + 1
    for roll_total, roll_count in quantum_rolls.items():
        this_position = position + roll_total
        if this_position > 10:
            this_position -= 10
        this_score = score + this_position

        this_count = count * roll_count

        if this_score >= 21:
            final_scores[this_roll_number] = final_scores.get(this_roll_number, 0) + this_count
        else:
            build_dice_universes(
                quantum_rolls,
                this_position,
                this_score,
                this_roll_number,
                this_count,
                final_scores
            )

@register(21, 2021, 2)
def dice_roll_2(text):
    position_1, position_2 = get_start_position(text)
    position_1 += 1
    position_2 += 1


    universes_1 = {}
    universes_2 = {}

    quantum_rolls = build_quantum_rolls()

    build_dice_universes(
        quantum_rolls,
        position_1,
        0,
        0,
        1,
        universes_1
    )

    build_dice_universes(
        quantum_rolls,
        position_2,
        0,
        0,
        1,
        universes_2
    )   

    winning_universes_1 = 0
    
    losing_universes_2 = {}

    #Could also sum up all greater numbers?
    for i in range(1, max(max(universes_1.keys()), max(universes_2.keys())) + 1):
        if i - 1 not in universes_2:
            if i - 1 not in losing_universes_2:
                losing_universes_2[i] = 27 ** (i - 1)
            else:
                losing_universes_2[i] = losing_universes_2[i - 1] * 27
        else:
            if i - 1 not in losing_universes_2:
                losing_universes_2[i] = 27 ** (i - 1) - universes_2[i - 1]
            else:
                losing_universes_2[i] = losing_universes_2[i - 1] * 27 - universes_2[i - 1]

    for number_of_rolls, number_of_universes in universes_1.items():
        winning_universes_1 += number_of_universes * losing_universes_2[number_of_rolls]

    losing_universes_1 = {}

    for i in range(1, max(max(universes_1.keys()), max(universes_2.keys())) + 1):
        if i not in universes_1:
            if i - 1 not in losing_universes_1:
                losing_universes_1[i] = 27 ** (i)
            else:
                losing_universes_1[i] = losing_universes_1[i - 1] * 27
        else:
            if i - 1 not in losing_universes_1:
                losing_universes_1[i] = 27 ** (i) - universes_1[i]
            else:
                losing_universes_1[i] = losing_universes_1[i - 1] * 27 - universes_1[i]

    winning_universes_2 = 0

    for number_of_rolls, number_of_universes in universes_2.items():
        winning_universes_2 += number_of_universes * losing_universes_1[number_of_rolls]

    return max(winning_universes_1, winning_universes_2)

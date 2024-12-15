from advent.utils.direction import Direction
from advent.runner import register

@register(9, 2022, 1, True)
def rope_bridge_1(split_text):
    head_x_position = 0
    head_y_position = 0

    tail_x_position = 0
    tail_y_position = 0

    tail_positions = set()

    for line in split_text:
        split_line = line.split(" ")

        direction = Direction.direction_from_letter(split_line[0])

        for i in range(int(split_line[1])):
            head_x_position, head_y_position = direction.move_forward_x_and_y(head_x_position, head_y_position)

            x_diff = head_x_position - tail_x_position
            y_diff = head_y_position - tail_y_position

            if (abs(x_diff) >= 2 and abs(y_diff) >= 1) or (abs(x_diff) >= 1 and abs(y_diff) >= 2):
                diff_to_test = 1
            else:
                diff_to_test = 2

            if x_diff >= diff_to_test:
                tail_x_position += 1
            elif x_diff <= -diff_to_test:
                tail_x_position -= 1
            if y_diff >= diff_to_test:
                tail_y_position += 1
            elif y_diff <= -diff_to_test:
                tail_y_position -= 1

            tail_positions.add((tail_x_position, tail_y_position))

    return len(tail_positions)

@register(9, 2022, 2, True)
def rope_bridge_2(split_text):
    knots = []
    for i in range(10):
        knots.append(
            {
                "x_position": 0,
                "y_position": 0
            }
        )

    tail_positions = set()

    for line in split_text:
        split_line = line.split(" ")

        direction = Direction.direction_from_letter(split_line[0])

        for i in range(int(split_line[1])):
            for i, tail_knot in enumerate(knots):
                if i == 0:
                    x_position, y_position = direction.move_forward_x_and_y(tail_knot["x_position"], tail_knot["y_position"])
                    tail_knot["x_position"] = x_position
                    tail_knot["y_position"] = y_position
                else:
                    head_knot = knots[i - 1]
                    x_diff = head_knot["x_position"] - tail_knot["x_position"] 
                    y_diff = head_knot["y_position"] - tail_knot["y_position"] 

                    if (abs(x_diff) >= 2 and abs(y_diff) >= 1) or (abs(x_diff) >= 1 and abs(y_diff) >= 2):
                        diff_to_test = 1
                    else:
                        diff_to_test = 2

                    if x_diff >= diff_to_test:
                        tail_knot["x_position"]  += 1
                    elif x_diff <= -diff_to_test:
                        tail_knot["x_position"]  -= 1
                    if y_diff >= diff_to_test:
                        tail_knot["y_position"]  += 1
                    elif y_diff <= -diff_to_test:
                        tail_knot["y_position"]  -= 1

                    if i == 9:
                        tail_positions.add((tail_knot["x_position"], tail_knot["y_position"] ))

    return len(tail_positions)
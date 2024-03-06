from advent.runner import register
import re

def parse_target(text):
    matched_text = re.match(r"target area: x=(-{0,1}\d+)..(-{0,1}\d+), y=(-{0,1}\d+)..(-{0,1}\d+)", text)

    return int(matched_text.group(1)), int(matched_text.group(2)), int(matched_text.group(3)), int(matched_text.group(4))

@register(17, 2021, 1)
def trick_shot_1(text):
    x_min, x_max, y_min, y_max  = parse_target(text)

    if y_min < 0:
        return abs(y_min) - 1
    else:
        raise NotImplementedError
    
@register(17, 2021, 2)
def trick_shot_2(text):
    x_min, x_max, y_min, y_max  = parse_target(text)

    viable_x = {}

    all_viable_times = set()

    for x in range(x_max + 1):
        viable_times = set()

        for t in range(0, x + 1):
            end_result = (x * ( x + 1 ) - (x - t) * ( (x - t) + 1)) / 2

            if end_result >= x_min and end_result <= x_max:
                viable_times.add(t)

                if t == x:
                    for i in range(x, abs(y_min) * 2 + 1):
                        viable_times.add(i)

        if len(viable_times) > 0:
            viable_x[x] = viable_times

        all_viable_times = all_viable_times.union(viable_times)

    viable_y = {}

    for t in all_viable_times:
        viable_ys = set()
        for y in range(y_min, abs(y_min)):
            if y > 0:
                time_to_use = t - (2 * y + 1)
                
                if time_to_use > 0:
                    end_result = ((y + time_to_use) * (y + time_to_use + 1) - (y) * (y + 1)) / 2

                    if end_result >= abs(y_max) and end_result <= abs(y_min):
                        viable_ys.add(y)
            else:
                y_to_use = abs(y)    

                end_result = ((y_to_use + t - 1) * (y_to_use + t) - (y_to_use - 1) * (y_to_use)) / 2

                if end_result >= abs(y_max) and end_result <= abs(y_min):
                    viable_ys.add(y)

        viable_y[t] = viable_ys

    total = 0
    for x, times in viable_x.items():
        possible_ys = set()
        for time in times:
            possible_ys = possible_ys.union(viable_y[time])

        total += len(possible_ys)

    return total
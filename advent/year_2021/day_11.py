from advent.runner import register
@register(11, 2021, 1)
def octopus_1(text):
    octopii = {}

    split_text = text.split("\n")

    max_y = len(split_text)
    max_x = len(split_text[0])

    for y, line in enumerate(split_text):
        for x, num in enumerate(line):
            octopii[(x, y)] = int(num)

    flash_total = 0
    for i in range(100):
        octopii_to_run = list(octopii.keys())
        flashed = set()
        while len(octopii_to_run) > 0:
            next_octopii = []
            for octopus in octopii_to_run:
                if octopus not in flashed:
                    if octopii[octopus] == 9:
                        octopii[octopus] = 0
                        flashed.add(octopus)
                        for potential_octopus in [
                            (octopus[0] - 1, octopus[1]), 
                            (octopus[0] + 1, octopus[1]), 
                            (octopus[0], octopus[1] - 1), 
                            (octopus[0], octopus[1] + 1),
                            (octopus[0] - 1, octopus[1] - 1), 
                            (octopus[0] - 1, octopus[1] + 1), 
                            (octopus[0] + 1, octopus[1] - 1), 
                            (octopus[0] + 1, octopus[1] + 1)
                        ]:
                            if potential_octopus[0] >= 0 and potential_octopus[0] < max_x and potential_octopus[1] >= 0 and potential_octopus[1] < max_y:
                                next_octopii.append(potential_octopus)
                    else:
                        octopii[octopus] += 1

            octopii_to_run = next_octopii
        flash_total += len(flashed)
    
    return flash_total

@register(11, 2021, 2)
def octopus_2(text):
    octopii = {}

    split_text = text.split("\n")

    max_y = len(split_text)
    max_x = len(split_text[0])

    for y, line in enumerate(split_text):
        for x, num in enumerate(line):
            octopii[(x, y)] = int(num)

    i = 1
    while True:
        octopii_to_run = list(octopii.keys())
        flashed = set()
        while len(octopii_to_run) > 0:
            next_octopii = []
            for octopus in octopii_to_run:
                if octopus not in flashed:
                    if octopii[octopus] == 9:
                        octopii[octopus] = 0
                        flashed.add(octopus)
                        for potential_octopus in [
                            (octopus[0] - 1, octopus[1]), 
                            (octopus[0] + 1, octopus[1]), 
                            (octopus[0], octopus[1] - 1), 
                            (octopus[0], octopus[1] + 1),
                            (octopus[0] - 1, octopus[1] - 1), 
                            (octopus[0] - 1, octopus[1] + 1), 
                            (octopus[0] + 1, octopus[1] - 1), 
                            (octopus[0] + 1, octopus[1] + 1)
                        ]:
                            if potential_octopus[0] >= 0 and potential_octopus[0] < max_x and potential_octopus[1] >= 0 and potential_octopus[1] < max_y:
                                next_octopii.append(potential_octopus)
                    else:
                        octopii[octopus] += 1

            octopii_to_run = next_octopii
        if len(flashed) == len(octopii):
            return i
        i += 1
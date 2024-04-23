from advent.runner import register

@register(10, 2022, 1, True)
def cathode_ray_tube_1(split_text):
    register = 1
    cycle_count = 1

    total = 0

    for line in split_text:
        split_line = line.split(" ")

        if split_line[0] == "addx":
            if cycle_count % 40 == 20:
                total += cycle_count * register

            cycle_count += 1
            
        if cycle_count % 40 == 20:
            total += cycle_count * register
        
        cycle_count += 1
        
        if split_line[0] == "addx":
            register += int(split_line[1])

    return total

def process_cycle(register, cycle_count, screen):
    register_to_check = cycle_count % 40 - 1

    if register_to_check == 0:
        screen.append([])

    if register - register_to_check >= -1 and register - register_to_check <= 1:
        screen[-1].append("#")
    else:
        screen[-1].append(".")

@register(10, 2022, 2, True)
def cathode_ray_tube_2(split_text):
    register = 1
    cycle_count = 1
    screen = []

    for line in split_text:
        split_line = line.split(" ")

        if split_line[0] == "addx":
            process_cycle(register, cycle_count, screen)

            cycle_count += 1
            
        process_cycle(register, cycle_count, screen)
        
        cycle_count += 1
        
        if split_line[0] == "addx":
            register += int(split_line[1])

    joined_screen = []

    for line in screen:
        joined_screen.append("".join(line))

    for line in joined_screen:
        print(line)
    print("")

    return joined_screen
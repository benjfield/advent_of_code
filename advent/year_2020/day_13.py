from advent.runner import register
from advent.utils.modulo import chinese_remainder_theorem

@register(13, 2020, 1, True)
def shuttle_search_1(split_text):
    arrival_time = int(split_text[0])

    busses = split_text[1].split(",")

    next_bus = 0
    time_to_next_bus = arrival_time * 100
    for bus in busses:
        if bus != "x":
            bus_time = int(bus)
            time_to_bus = bus_time - (arrival_time % bus_time)

            if time_to_bus < time_to_next_bus:
                next_bus = bus_time
                time_to_next_bus = time_to_bus

    return time_to_next_bus * next_bus

@register(13, 2020, 2, True)
def shuttle_search_2(split_text):
    busses = split_text[1].split(",")

    bus_dict = {}
    for i, bus in enumerate(busses):
        if bus != "x":
            bus_dict[int(bus)] = int(bus) - i

    return chinese_remainder_theorem(bus_dict)

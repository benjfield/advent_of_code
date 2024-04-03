from advent.runner import register
import re

@register(16, 2020, 1, True)
def ticket_translation_1(split_text):
    valid_numbers = set()

    invalid_number_total = 0
    line_type = 0
    for line in split_text:
        if len(line) > 0:
            if line == "your ticket:" or line == "nearby tickets:":
                line_type += 1
            else:
                if line_type == 0:
                    parsed_line = re.search(r"(.*): (\d+)-(\d+) or (\d+)-(\d+)", line)
                    for bottom, top in [(parsed_line.group(2), parsed_line.group(3)), (parsed_line.group(4), parsed_line.group(5))]:
                        for number in range(int(bottom), int(top) + 1):
                            valid_numbers.add(number)
                elif line_type == 2:
                    values = [int(x) for x in line.split(",")]
                    for value in values:
                        if value not in valid_numbers:
                            invalid_number_total += value

    return invalid_number_total

@register(16, 2020, 2, True)
def ticket_translation_2(split_text):
    all_valid_numbers = set()
    number_options = {}

    line_type = 0
    valid_tickets = []
    your_ticket = None
    for line in split_text:
        if len(line) > 0:
            if line == "your ticket:" or line == "nearby tickets:":
                line_type += 1
            else:
                if line_type == 0:
                    valid_numbers = set()
                    parsed_line = re.search(r"(.*): (\d+)-(\d+) or (\d+)-(\d+)", line)
                    for bottom, top in [(parsed_line.group(2), parsed_line.group(3)), (parsed_line.group(4), parsed_line.group(5))]:
                        for number in range(int(bottom), int(top) + 1):
                            valid_numbers.add(number)
                            all_valid_numbers.add(number)
                    number_options[parsed_line.group(1)] = valid_numbers
                elif line_type == 2:
                    values = [int(x) for x in line.split(",")]

                    valid_ticket = True
                    for value in values:
                        if value not in all_valid_numbers:
                            valid_ticket = False
                            break

                    if valid_ticket:
                        valid_tickets.append(values)
                else:
                    your_ticket = [int(x) for x in line.split(",")]
                    valid_tickets.append(your_ticket)

    ticket_options = [set(number_options.keys()) for i in range(len(your_ticket))]
    for ticket in valid_tickets:
        for i, value in enumerate(ticket):
            possible_options = list(ticket_options[i])
            for option_name in possible_options:
                if value not in number_options[option_name]:
                    ticket_options[i].remove(option_name)

    options_to_remove = []
    for ticket_option_set in ticket_options:
        if len(ticket_option_set) == 1:
            options_to_remove.append(list(ticket_option_set)[0])

    while len(options_to_remove) > 0:
        next_options_to_remove = []
        for ticket_option_set in ticket_options:
            if len(ticket_option_set) > 1:
                for option_to_remove in options_to_remove:
                    ticket_option_set.remove(option_to_remove)
            
                if len(ticket_option_set) == 1:
                    next_options_to_remove.append(list(ticket_option_set)[0])
                
        options_to_remove = next_options_to_remove

    total = 1
    for i, ticket_option_set in enumerate(ticket_options):
        if len(ticket_option_set) == 1:
            if list(ticket_option_set)[0][:9] == "departure":
                total *= your_ticket[i]

    return total



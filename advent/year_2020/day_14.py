from advent.runner import register

@register(14, 2020, 1, True)
def docking_data_1(split_text):
    memory_bank = {
    }
    
    for line in split_text:
        split_by_equals = line.split(" = ")

        if split_by_equals[0] == "mask":
            mask = {}
            for i, value in enumerate(reversed(split_by_equals[1])):
                if value != "X":
                    if value == "1":
                        value_bool = True
                    else:
                        value_bool = False
                    mask[2**i] = value_bool
        else:
            memory = int(split_by_equals[1])
            address = split_by_equals[0].split("[")[1][:-1]
            for mask_value, mask_bool in mask.items():
                if mask_bool:
                    memory = memory | mask_value
                else:
                    memory = memory & ~mask_value
            memory_bank[address] = memory 
    
    return sum(memory_bank.values())

def count_addresses(used_addresses, current_address, current_index):
    if current_address not in used_addresses:
        if current_index == len(current_address):
            used_addresses.add(current_address)
            return 1
        else:
            if current_address[current_index] == "X":
                used_addresses.add(current_address)
                total = 0
                for replacement_value in ["0", "1"]:
                    this_address = current_address[:current_index] + replacement_value + current_address[current_index + 1:]
                    total += count_addresses(used_addresses, this_address, current_index + 1)
                return total
            else:
                return count_addresses(used_addresses, current_address, current_index + 1)
    else:
        return 0

@register(14, 2020, 2, True)
def docking_data_2(split_text):
    addresses = []
    for line in split_text:
        split_by_equals = line.split(" = ")

        if split_by_equals[0] == "mask":
            mask = split_by_equals[1]
        else:
            addresses.append({
                "mask": mask,
                "address": int(split_by_equals[0].split("[")[1][:-1]),
                "memory": int(split_by_equals[1])
            })

    used_addresses = set()

    total = 0
    for address_details in reversed(addresses):
        address = format(address_details["address"], "036b")
        for i, value in enumerate(address_details["mask"]):
            if value == "1" or value == "X":
                address = address[:i] + value + address[i + 1:]
        count = count_addresses(used_addresses, address, 0)
        total += count * address_details["memory"]

    return total




    
    return sum(memory_bank.values())
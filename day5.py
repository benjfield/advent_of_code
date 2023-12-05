import re
from aocd import get_data

def seed_1(text):
    seeds = []
    seed_maps = []

    for line in text.split("\n"):
        if len(line) != 0:
            if re.match("^seeds:.+", line):
                seeds = re.findall(r"\d+", line)
            elif re.match(".*map:", line):
                seed_maps.append([])
            else:
                decoded_map = re.match("(\d+) (\d+) (\d+)", line)
                if decoded_map:
                    seed_maps[-1].append(
                        {
                            "destination": int(decoded_map.group(1)),
                            "source": int(decoded_map.group(2)),
                            "range": int(decoded_map.group(3)),
                        }
                    )
    results = []
    for seed in seeds:
        current_type = int(seed)
        for seed_map in seed_maps:
            for single_seed_map in seed_map:
                if current_type - single_seed_map["source"] >= 0 and current_type - single_seed_map["source"] < single_seed_map["range"]:
                    current_type = current_type - single_seed_map["source"] + single_seed_map["destination"]
                    break

        results.append(current_type)
    
    return min(results)

def seed_2(text):
    seeds = []
    seed_maps = []

    for line in text.split("\n"):
        if len(line) != 0:
            if re.match("^seeds:.+", line):
                for seed_pair in re.findall(r"(\d+) (\d+)", line):
                    seeds.append({
                        "start": int(seed_pair[0]),
                        "range": int(seed_pair[1])
                    })
            elif re.match(".*map:", line):
                seed_maps.append([])
            else:
                decoded_map = re.match("(\d+) (\d+) (\d+)", line)
                if decoded_map:
                    seed_maps[-1].append(
                        {
                            "destination": int(decoded_map.group(1)),
                            "source": int(decoded_map.group(2)),
                            "range": int(decoded_map.group(3)),
                        }
                    )

    def sortByDestination(map):
        return map["destination"]
    
    for i, seed_map in enumerate(seed_maps):
        seed_map.sort(key=sortByDestination)

    def sortByStart(seed):
        return seed["start"]
    
    seeds.sort(key=sortByStart)
    
    def find_seed(seed_maps, input):
        current_type = input
        for seed_map in reversed(seed_maps):
            for single_seed_map in seed_map:
                current_destination_diff = current_type - single_seed_map["destination"]
                if current_destination_diff >= 0 and current_destination_diff < single_seed_map["range"]:
                    current_type = current_destination_diff + single_seed_map["source"]
                    break
                elif current_destination_diff < 0:
                    break
        
        return current_type

    def add_valid_seeds(boundary_seeds, seeds, possible_seed):
        for seed in seeds:
            current_start_diff = possible_seed - seed["start"]
            if current_start_diff >= 0 and current_start_diff < seed["range"]:
                boundary_seeds.append(possible_seed)
            if current_start_diff < 0:
                break

    boundary_seeds = []

    for i in range(len(seed_maps) -1, -1, -1):
        add_valid_seeds(boundary_seeds, seeds, find_seed(seed_maps[:i+1], 0))
        for single_seed_map in seed_maps[i]:
            add_valid_seeds(boundary_seeds, seeds, 
                find_seed(seed_maps[:i+1], single_seed_map["destination"] - 1)
            )
            add_valid_seeds(boundary_seeds, seeds, 
                find_seed(seed_maps[:i+1], single_seed_map["destination"])
            )
            add_valid_seeds(boundary_seeds, seeds, 
                find_seed(seed_maps[:i+1], single_seed_map["destination"] + single_seed_map["range"] - 1)
            )
            add_valid_seeds(boundary_seeds, seeds, 
                find_seed(seed_maps[:i+1], single_seed_map["destination"] + single_seed_map["range"])
            )

    for seed in seeds:
        boundary_seeds.append(seed["start"])
        boundary_seeds.append(seed["start"])

    boundary_locations=[]

    def sortBySource(map):
        return map["source"]
    
    for i, seed_map in enumerate(seed_maps):
        seed_map.sort(key=sortBySource)

    for seed in boundary_seeds:
        current_type = seed
        for seed_map in seed_maps:
            for single_seed_map in seed_map:
                current_source_diff = current_type - single_seed_map["source"]
                if current_source_diff >= 0 and current_source_diff < single_seed_map["range"]:
                    current_type = current_source_diff + single_seed_map["destination"]
                    break
                elif current_source_diff < 0:
                    break
        boundary_locations.append(current_type)

    return min(boundary_locations)

seed_text = get_data(day=5, year=2023)
from advent.runner import register
def get_orbits(orbits, letter, orbit_cache):
    if letter in orbit_cache:
        return orbit_cache[letter]
    
    if letter in orbits:
        orbit = get_orbits(orbits, orbits[letter], orbit_cache) + 1
        orbit_cache[letter] = orbit
        return orbit
    else:
        orbit_cache[letter] = 0
        return 0

def create_orbits(text):
    split_text = text.split("\n")

    orbits = {}

    for line in split_text:
        split_line = line.split(")")

        orbits[split_line[1]] = split_line[0]

    return orbits

@register(6, 2019, 1)
def orbits_1(text):
    orbits = create_orbits(text)

    orbit_cache = {}

    total_orbits = 0
    for key in orbits.keys():
        total_orbits += get_orbits(orbits, key, orbit_cache)

    return total_orbits

def distance_to_cache(orbits, letter, orbit_cache):
    if letter in orbit_cache:
        return 0, orbit_cache[letter]
    
    if letter in orbits:
        distance_from_san_to_cache, distance_from_cache_to_center = distance_to_cache(orbits, orbits[letter], orbit_cache)
        distance_from_san_to_cache += 1
        return distance_from_san_to_cache, distance_from_cache_to_center
    else:
        return 0, 0

@register(6, 2019, 2)
def orbits_2(text):
    orbits = create_orbits(text)

    orbit_cache = {}

    distance_from_you_to_center = get_orbits(orbits, "YOU", orbit_cache)

    distance_from_san_to_cache, distance_from_cache_to_center = distance_to_cache(orbits, "SAN", orbit_cache)

    return distance_from_you_to_center - distance_from_cache_to_center + distance_from_san_to_cache - 2

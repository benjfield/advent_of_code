from advent.runner import register

class Cave:
    def __init__(self, name, neighbour_name):
        self.name = name
        self.neighbour_names = [neighbour_name]
        self.neighbours = []

        if self.name.islower():
            self.small = True
        else:
            self.small = False

        if self.name == "start":
            self.start = True
        else:
            self.start = False

        if self.name == "end":
            self.end = True
        else:
            self.end = False

    def add_neighbour_name(self, neighbour_name):
        self.neighbour_names.append(neighbour_name)

    def populate_neighbours(self, caves):
        self.neighbours = [ caves[neighbour_name] for neighbour_name in self.neighbour_names ]

    def count_paths(self, visited_small_caves, count):
        if self.end:
            return count + 1
        else:
            if self.small:
                if self.name in visited_small_caves:
                    return count
                else:
                    visited_small_caves = visited_small_caves.copy()
                    visited_small_caves.add(self.name)
            for neighbour in self.neighbours:
                count = neighbour.count_paths(visited_small_caves, count)
            return count

class CaveTwice(Cave):
    def count_paths(self, visited_small_caves, count):
        if self.end:
            return count + 1
        else:
            if self.small:
                if self.name in visited_small_caves:
                    if self.start or self.end:
                        return count
                    elif "twice" in visited_small_caves:
                        return count
                    else:
                        visited_small_caves = visited_small_caves.copy()
                        visited_small_caves.add("twice")
                else:
                    visited_small_caves = visited_small_caves.copy()
                    visited_small_caves.add(self.name)
            for neighbour in self.neighbours:
                count = neighbour.count_paths(visited_small_caves, count)
            return count

@register(12, 2021, 1)
def passage_1(text):
    split_text = text.split("\n")

    caves = {}

    for line in split_text:
        split_passage = line.split("-")

        for i, cave_name in enumerate(split_passage):
            neighbour_index = (i + 1)%2
            if cave_name in caves:
                caves[cave_name].add_neighbour_name(split_passage[neighbour_index])
            else:
                cave = Cave(
                    name=cave_name,
                    neighbour_name=split_passage[neighbour_index]
                )
                caves[cave_name] = cave
    
    for cave in caves.values():
        cave.populate_neighbours(caves)

    visited_small_caves = set()

    return caves["start"].count_paths(visited_small_caves, 0)

@register(12, 2021, 2)
def passage_2(text):
    split_text = text.split("\n")

    caves = {}

    for line in split_text:
        split_passage = line.split("-")

        for i, cave_name in enumerate(split_passage):
            neighbour_index = (i + 1)%2
            if cave_name in caves:
                caves[cave_name].add_neighbour_name(split_passage[neighbour_index])
            else:
                cave = CaveTwice(
                    name=cave_name,
                    neighbour_name=split_passage[neighbour_index]
                )
                caves[cave_name] = cave
    
    for cave in caves.values():
        cave.populate_neighbours(caves)

    visited_small_caves = set()

    return caves["start"].count_paths(visited_small_caves, 0)
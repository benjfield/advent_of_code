from advent.runner import register
import copy

@register(24, 2019, 1)
def bug_1(text):
    tiles = {}
    for y, line in enumerate(text.split("\n")):
        for x, char in enumerate(line):
            if char == "#":
                bug = True
            else:
                bug = False
            tile = Tile(x, y, bug)
            coords = (x, y)
            tiles[coords] = tile

    values_cache = set()

    while True:
        for tile in tiles.values():
            neighbours = tile.get_neighbours()
            for neighbour in neighbours:
                tiles[neighbour].add_adjacent()

        value = 0
        for tile in tiles.values():
            tile.set_bug()
            value += tile.biodiversity_value()

        if value in values_cache:
            return value
        else:
            values_cache.add(value)

class Tile:
    def __init__(
        self,
        x,
        y,
        bug,
    ):
        self.x = x
        self.y = y
        self.bug = bug
        self.neighbours = self.generate_neighbours()
        self.adjacent = 0

    def generate_neighbours(self):
        neighbours = []
        for possible_x, possible_y in [(self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]:
            if possible_x >= 0 and possible_x < 5 and possible_y >= 0 and possible_y < 5:
                neighbours.append((possible_x, possible_y))
        return neighbours

    def get_neighbours(self):
        if self.bug:
            return self.neighbours
        else:
            return []

    def add_adjacent(self):
        self.adjacent += 1

    def set_bug(self):
        if self.bug:
            if self.adjacent != 1:
                self.bug = False
        elif self.adjacent == 1 or self.adjacent == 2:
            self.bug = True
        self.adjacent = 0

    def biodiversity_value(self):
        if self.bug:
            return 2 ** (self.x + 5 * self.y)
        return 0

    def __str__(self):
        return f"{self.x}_{self.y}"
        
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


class RecursiveTile(Tile):
    def __init__(
        self,
        x,
        y,
        z,
        bug,
    ):
        self.z = z
        super().__init__(x, y, bug)

    def generate_neighbours(self):
        neighbours = []

        if self.x == 0:
            neighbours += [
                (1, 2, self.z + 1),
                (1, self.y, self.z)
            ]
        elif self.x == 4:
            neighbours += [
                (3, 2, self.z + 1),
                (3, self.y, self.z)
            ]
        elif self.x == 1:
            if self.y == 2:
                neighbours += [
                    (0, 0, self.z - 1),
                    (0, 1, self.z - 1),
                    (0, 2, self.z - 1),
                    (0, 3, self.z - 1),
                    (0, 4, self.z - 1),
                    (0, self.y, self.z),
                ]
            else:
                neighbours += [
                    (0, self.y, self.z),
                    (2, self.y, self.z)
                ]
        elif self.x == 3:
            if self.y == 2:
                neighbours += [
                    (4, 0, self.z - 1),
                    (4, 1, self.z - 1),
                    (4, 2, self.z - 1),
                    (4, 3, self.z - 1),
                    (4, 4, self.z - 1),
                    (4, self.y, self.z),
                ]
            else:
                neighbours += [
                    (2, self.y, self.z),
                    (4, self.y, self.z)
                ]
        else:
            neighbours += [
                (1, self.y, self.z),
                (3, self.y, self.z)
            ]

        if self.y == 0:
            neighbours += [
                (2, 1, self.z + 1),
                (self.x, 1, self.z)
            ]
        elif self.y == 4:
            neighbours += [
                (2, 3, self.z + 1),
                (self.x, 3, self.z)
            ]
        elif self.y == 1:
            if self.x == 2:
                neighbours += [
                    (0, 0, self.z - 1),
                    (1, 0, self.z - 1),
                    (2, 0, self.z - 1),
                    (3, 0, self.z - 1),
                    (4, 0, self.z - 1),
                    (self.x, 0, self.z),
                ]
            else:
                neighbours += [
                    (self.x, 0, self.z),
                    (self.x, 2, self.z)
                ]
        elif self.y == 3:
            if self.x == 2:
                neighbours += [
                    (0, 4, self.z - 1),
                    (1, 4, self.z - 1),
                    (2, 4, self.z - 1),
                    (3, 4, self.z - 1),
                    (4, 4, self.z - 1),
                    (self.x, 4, self.z),
                ]
            else:
                neighbours += [
                    (self.x, 2, self.z),
                    (self.x, 4, self.z)
                ]
        else:
            neighbours += [
                (self.x, 1, self.z),
                (self.x, 3, self.z)
            ]

        return neighbours
    
    def __str__(self):
        return f"{self.x}_{self.y}_{self.z}"
    
@register(24, 2019, 2)
def bug_2(text, turns = 200):
    tiles = {}
    for y, line in enumerate(text.split("\n")):
        for x, char in enumerate(line):
            if char != "?":
                if char == "#":
                    bug = True
                else:
                    bug = False
                tile = RecursiveTile(x, y, 0, bug)
                coords = (x, y, 0)
                tiles[coords] = tile

    for i in range(turns):
        neighbours_to_change = []
        for tile in tiles.values():
            neighbours_to_change += tile.get_neighbours()

        for neighbour in neighbours_to_change:
            if neighbour not in tiles:
                tiles[neighbour] = RecursiveTile(neighbour[0], neighbour[1], neighbour[2], False)
            tiles[neighbour].add_adjacent()

        for tile in tiles.values():
            tile.set_bug()

    bug_count = 0
    for tile in tiles.values():
        if tile.bug:
            bug_count += 1
    return bug_count
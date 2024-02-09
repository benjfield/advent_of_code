from advent.runner import register
from advent.utils.path_finding import Node, djikstra, NodeStore, NodeStoreWithPath, NodeWithPath
from functools import partial

keys_with_neighbours = {}

class KeysNode(Node):
    def __init__(self, key_tile, keys=None):
        self.key_tile = key_tile
        if keys is None:
            self.keys = set()
        else:
            self.keys = keys

    def get_neighbours(self, map, cost):
        next_keys = self.keys.copy()
        next_keys.add(self.key_tile)
        neighbours = []
        for neighbour in keys_with_neighbours[self.key_tile]:
            if neighbour["key"] not in next_keys:
                all_required_keys = True
                for door in neighbour["doors"]:
                    if door.lower() not in next_keys:
                        all_required_keys = False
                        break

                if all_required_keys:
                    neighbours.append({
                        "neighbour": type(self)(
                            neighbour["key"],
                            next_keys
                        ),
                        "cost": cost + neighbour["cost"]
                    })

        return neighbours
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        if self.key_tile == other.key_tile and self.keys == other.keys:
            return True
        return False

    def this_string(self):
        keys_list = list(self.keys)
        keys_list.sort()
        string = f"key {self.key_tile} keys {keys_list}"
        return string

    def __str__(self):
        return self.this_string()

def djikstra_terminate_keys(number_of_keys, current_square):
    if len(current_square.keys) == number_of_keys:
        return True
    return False

def djikstra_terminate_keys_function(number_of_keys):
    return partial(djikstra_terminate_keys, number_of_keys)

class NodeWithKeys(NodeWithPath): 
    def get_neighbours(self, map, cost):
        neighbours = []

        for x, y in [(self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]:
            if self.check_valid_neighbour(x, y, len(map[0]) - 1, len(map) - 1):
                if map[y][x] != "#":
                    possible_neighbour = type(self)(
                        x=x,
                        y=y,
                    )
                    self.append_neighbours(neighbours, possible_neighbour, cost)
        return neighbours


@register(18, 2019, 1)
def keys_1(text):
    keys_with_neighbours.clear()
    keys = []
    doors = {}
    split_text = text.split("\n")

    for y, row in enumerate(split_text):
        for x, tile in enumerate(row):
            if tile == "@":
                keys.append({
                        "x": x,
                        "y": y,
                        "key": tile
                    })
            elif tile.isalpha():
                if tile.islower():
                    keys.append({
                        "x": x,
                        "y": y,
                        "key": tile
                    })
                elif tile.isupper():
                    doors[f"{x}_{y}"] = tile

    i = 0
    for key in keys:
        key_neighbours = []

        start_point = NodeWithKeys(key["x"], key["y"])

        result = djikstra(split_text, start_point, True)

        for other_key in keys:
            if other_key != key:
                node = NodeWithKeys(other_key["x"], other_key["y"])
                if node in result.store:
                    path = result.store[node]

                    these_doors = []

                    for path_step in path:
                        if f"{path_step['x']}_{path_step['y']}" in doors:
                            these_doors.append(doors[f"{path_step['x']}_{path_step['y']}"])

                    key_neighbours.append({
                        "key": other_key["key"],
                        "cost": len(path),
                        "doors": these_doors
                    })

        keys_with_neighbours[key["key"]] = key_neighbours
        i += 1

    start_point = KeysNode("@")

    djikstra_function = djikstra_terminate_keys_function(len(keys) - 1)

    return djikstra(split_text, start_point, False, djikstra_function)

class MultipleKeysNode(Node):
    def __init__(self, key_tiles, keys=None):
        self.key_tiles = key_tiles
        if keys is None:
            self.keys = set()
        else:
            self.keys = keys

    def get_neighbours(self, map, cost):
        next_keys = self.keys.copy()
        for key_tile in self.key_tiles:
            next_keys.add(key_tile)
        neighbours = []
        for i, key_tile in enumerate(self.key_tiles):
            for neighbour in keys_with_neighbours[key_tile]:
                if neighbour["key"] not in next_keys:
                    all_required_keys = True
                    for door in neighbour["doors"]:
                        if door.lower() not in next_keys:
                            all_required_keys = False
                            break

                    if all_required_keys:
                        neighbour_keys = self.key_tiles.copy()
                        neighbour_keys[i] = neighbour["key"]

                        neighbours.append({
                            "neighbour": type(self)(
                                neighbour_keys,
                                next_keys
                            ),
                            "cost": cost + neighbour["cost"]
                        })

        return neighbours
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        if self.key_tiles == other.key_tiles and self.keys == other.keys:
            return True
        return False

    def this_string(self):
        keys_list = list(self.keys)
        keys_list.sort()
        string = f"key {self.key_tiles} keys {keys_list}"
        return string

    def __str__(self):
        return self.this_string()
    
@register(18, 2019, 2)
def keys_2(text, replace_center=True):
    keys_with_neighbours.clear()
    keys = []
    doors = {}
    split_text = text.split("\n")

    start_x = 0
    start_y = 0

    map = []
    start_count = 0
    for y, row in enumerate(split_text):
        map.append([])
        for x, tile in enumerate(row):
            if tile == "@":
                start_x = x
                start_y = y
            map[-1].append(tile)
            if tile.isalpha():
                if tile.islower():
                    keys.append({
                        "x": x,
                        "y": y,
                        "key": tile
                    })
                elif tile.isupper():
                    doors[f"{x}_{y}"] = tile

    for x in [start_x - 1, start_x, start_x + 1]:
        map[x][start_y] = "#"

    for y in [start_y - 1, start_y + 1]:
        map[start_x][y] = "#"

    for x, y, key in [
            (start_x - 1, start_y - 1, "0"),
            (start_x + 1, start_y - 1, "1"),
            (start_x - 1, start_y + 1, "2"),
            (start_x + 1, start_y + 1, "3")
        ]: 
        map[x][y] = key
        keys.append({
                "x": x,
                "y": y,
                "key": key
            })

    i = 0
    for key in keys:
        key_neighbours = []

        start_point = NodeWithKeys(key["x"], key["y"])

        result = djikstra(map, start_point, True)

        for other_key in keys:
            if other_key != key:
                node = NodeWithKeys(other_key["x"], other_key["y"])
                if node in result.store:
                    path = result.store[node]

                    these_doors = []

                    for path_step in path:
                        if f"{path_step['x']}_{path_step['y']}" in doors:
                            these_doors.append(doors[f"{path_step['x']}_{path_step['y']}"])

                    key_neighbours.append({
                        "key": other_key["key"],
                        "cost": len(path),
                        "doors": these_doors
                    })

        keys_with_neighbours[key["key"]] = key_neighbours
        i += 1

    start_point_keys = [str(i) for i in range(4)]

    start_point = MultipleKeysNode(start_point_keys)

    djikstra_function = djikstra_terminate_keys_function(len(keys) - 1)

    results = djikstra(map, start_point, False, djikstra_function)

    return results
import re
from advent.runner import register
from copy import deepcopy
                
def rotate_edges(
    top,
    right,
    bottom,
    left,
    max_index,
    rotation_type
):
    match rotation_type:
        case 0:
            return top, right, bottom, left
        case 1:
            return left, flip_number(top, max_index), right, flip_number(bottom, max_index)
        case 2:
            return flip_number(bottom, max_index), flip_number(left, max_index), flip_number(top, max_index), flip_number(right, max_index)
        case 3:
            return flip_number(right, max_index), bottom, flip_number(left, max_index), top

def flip_edges_vertical(
    top,
    right,
    bottom,
    left,
    max_index,
    flip
):
    if flip:
        return bottom, flip_number(right, max_index), top, flip_number(left, max_index)
    return top, right, bottom, left
                    
def flip_edges_horizontal(
    top,
    right,
    bottom,
    left,
    max_index,
    flip
):
    if flip:
        return flip_number(top, max_index), left, flip_number(bottom, max_index), right
    return top, right, bottom, left

class Tile:
    def __init__(
        self,
        tile_number,
        tile_pattern,
        edges
    ):
        self.tile_number = tile_number
        self.tile_pattern = tile_pattern
        self.edges = {}

        max_index = len(tile_pattern) - 1

        top = 0
        for i, tile in enumerate(reversed(self.tile_pattern[0])):
            if tile:
                top += 2 ** i
             
        bottom = 0 
        for i, tile in enumerate(reversed(self.tile_pattern[max_index])):
            if tile:
                bottom += 2 ** i

        left = 0
        for i in range(max_index + 1):
            if self.tile_pattern[i][0]:
                left += 2 ** i

        right = 0
        for i in range(max_index + 1):
            if self.tile_pattern[i][max_index]:
                right += 2 ** i

        added_edges = set()

        for rotation_type in range(4):
            for should_flip_vertical in [False, True]:
                for should_flip_horizontal in [False, True]:
                    new_top, new_right, new_bottom, new_left = rotate_edges(top, right, bottom, left, max_index, rotation_type)
                    new_top, new_right, new_bottom, new_left = flip_edges_vertical(new_top, new_right, new_bottom, new_left, max_index, should_flip_vertical)
                    new_top, new_right, new_bottom, new_left = flip_edges_horizontal(new_top, new_right, new_bottom, new_left, max_index, should_flip_horizontal)

                    edges_to_add = (new_top, new_right, new_bottom, new_left)
                    if edges_to_add not in added_edges:
                        added_edges.add(edges_to_add)
                        tile_position = (self.tile_number, rotation_type, should_flip_vertical, should_flip_horizontal)

                        self.edges[tile_position] = {
                            "top": new_top,
                            "right": new_right,
                            "bottom": new_bottom,
                            "left": new_left
                        }

                        for edge_type, edge_value in [
                            ("top", new_top),
                            ("right", new_right),
                            ("bottom", new_bottom),
                            ("left", new_left),
                        ]:
                            if edge_value in edges[edge_type]:
                                edges[edge_type][edge_value].add(tile_position)
                            else:
                                edges[edge_type][edge_value] = {tile_position}
                        


def flip_number(number, max_index):
    new_number = 0
    for i in range(max_index + 1):
        if number & 2** (max_index - i):
            new_number += 2**i
    return new_number

def try_tile(tiles, edges, tile_slots, used_tiles, x, y):
    if tile_slots[y][x]["top"] is None:
        possible_tiles = tile_slots[y][x]["left"]
    elif tile_slots[y][x]["left"] is None:
        possible_tiles = tile_slots[y][x]["top"]
    else:
        possible_tiles = tile_slots[y][x]["left"] | tile_slots[y][x]["top"]

    if len(possible_tiles) == 0:
        return None
    else:
        if x == len(tile_slots) - 1:
            if y == len(tile_slots) - 1:
                for possible_tile in possible_tiles:
                    if possible_tile[0] not in used_tiles:
                        tile_slots[y][x]["tile"] = possible_tile
                        return tile_slots
                return None
            else:
                next_y = y + 1
                next_x = 0
        else:                    
            next_y = y
            next_x = x + 1

        for possible_tile in possible_tiles:
            if possible_tile[0] not in used_tiles:
                tile_slots[y][x]["tile"] = possible_tile
                tile_edges = tiles[possible_tile[0]].edges[possible_tile]
                
                if x < len(tile_slots) - 1:
                    tile_slots[y][x + 1]["left"] = edges["left"][tile_edges["right"]]
                
                if y < len(tile_slots) - 1:
                    tile_slots[y + 1][x]["top"] = edges["top"][tile_edges["bottom"]]
                
                next_used_tiles = used_tiles.copy()
                next_used_tiles.add(possible_tile[0])

                returned_tile_slots = try_tile(tiles, edges, tile_slots, next_used_tiles, next_x, next_y)

                if returned_tile_slots is not None:
                    return returned_tile_slots
                
    return None

def process_tiles(split_text):
    split_text.append("")
    tiles = {}
    edges = {
        "top": {},
        "right": {},
        "bottom": {},
        "left": {},
    }
    for line in split_text:
        if len(line) == 0:
            tile = Tile(
                tile_number=tile_number,
                tile_pattern=tile_pattern,
                edges=edges
            )

            tiles[tile_number] = tile
        else:
            matched_line = re.search(r"Tile (\d+):", line)
            if matched_line is not None:
                tile_number = int(matched_line.group(1))
                tile_pattern = []
            else:
                tile_pattern.append([])
                for char in line:
                    tile_pattern[-1].append(char == "#")

    max_index = int(len(tiles) ** (1/2))

    tile_slots = []

    for y in range(max_index):
        tile_slots.append([])
        for x in range(max_index):
            tile_slots[-1].append({
                "tile": None,
                "top": None,
                "left": None
            })
    
    starting_possibilities = []

    for tile in tiles.values():
        starting_possibilities += list(tile.edges.keys())

    tile_slots[0][0]["left"] = set(starting_possibilities)

    return try_tile(tiles, edges, tile_slots, set(), 0, 0), tiles

@register(20, 2020, 1, True)
def jurassic_jigsaw_1(split_text):
    finished_tiles, tiles = process_tiles(split_text)
    corner_total = 1
    for x in [0, len(finished_tiles) - 1]:
        for y in [0, len(finished_tiles) - 1]:
            corner_total *= tiles[finished_tiles[y][x]["tile"][0]].tile_number

    return corner_total

def rotate(x, y, max_x, max_y, rotation_type):
    match rotation_type:
        case 0:
            return x, y, max_x, max_y
        case 1:
            return -y + max_y, x, max_y, max_x
        case 2:
            return -x + max_x, -y + max_y, max_x, max_y
        case 3:
            return y, -x + max_x, max_y, max_x

def flip_vertical(x, y, max_y, flip):
    if flip:
        return x, max_y - y
    else:
        return x, y
        
def flip_horizontal(x, y, max_x, flip):
    if flip:
        return max_x - x, y
    else:
        return x, y

def count_sea_monsters(picture):
    sea_monster_count = deepcopy(picture)

    for y in range(len(sea_monster_count)):
        for x in range(len(sea_monster_count)):
            sea_monster_count[y][x] = False

    sea_monster_positions = [
        (0, 1),
        (1, 2),
        (4, 2),
        (5, 1),
        (6, 1),
        (7, 2),
        (10, 2),
        (11, 1),
        (12, 1),
        (13, 2),
        (16, 2),
        (17, 1),
        (18, 1),
        (18, 0),
        (19, 1)
    ]

    max_x = 19
    max_y = 2
    
    found_sea_monsters = False              
    for rotation_type in range(4):
        for flip_ver_type in [False, True]:
            for flip_hor_type in [False, True]:
                these_sea_monster_positions = []
                for x, y in sea_monster_positions:
                    x, y, rotated_max_x, rotated_max_y = rotate(x, y, max_x, max_y, rotation_type)
                    x, y = flip_vertical(x, y, rotated_max_y, flip_ver_type)
                    x, y = flip_horizontal(x, y, rotated_max_x, flip_hor_type)
                    these_sea_monster_positions.append((x, y))
                    
                for y in range(len(picture)):
                    for x in range(len(picture)):
                        found_sea_monster = True

                        for x_change, y_change in these_sea_monster_positions:
                            if x + x_change < 0 or x + x_change >= len(picture) or y + y_change < 0 or y + y_change >= len(picture) or not picture[y + y_change][x + x_change]:
                                found_sea_monster = False
                                break
            
                        if found_sea_monster:
                            found_sea_monsters = True
                            for x_change, y_change in these_sea_monster_positions:
                                sea_monster_count[y + y_change][x + x_change] = True
                
                if found_sea_monsters:
                    tile_count = 0
                    for y, row in enumerate(sea_monster_count):
                        for x, tile in enumerate(row):
                            if not tile:
                                if picture[y][x]:
                                    tile_count += 1
                    return tile_count    
    return None                 

@register(20, 2020, 2, True)
def jurassic_jigsaw_2(split_text):
    finished_tiles, tiles = process_tiles(split_text)

    tile_row_count = len(tiles[finished_tiles[0][0]["tile"][0]].tile_pattern[1:-1])

    finished_picture = []
    
    positive_pixels = set()

    for picture_y, slot_row in enumerate(finished_tiles):
        for picture_x, slot in enumerate(slot_row):
            tile = tiles[slot["tile"][0]]
            for tile_y, tile_row in enumerate(tile.tile_pattern[1:-1]):
                for tile_x, pixel in enumerate(tile_row[1:-1]):
                    if pixel:
                        x, y, rotated_max_x, rotated_max_y = rotate(tile_x, tile_y, tile_row_count - 1, tile_row_count - 1, slot["tile"][1])
                        x, y = flip_vertical(x, y, rotated_max_y, slot["tile"][2])
                        x, y = flip_horizontal(x, y, rotated_max_x, slot["tile"][3])

                        positive_pixels.add((picture_x * tile_row_count + x, picture_y * tile_row_count + y))

    for picture_y, slot_row in enumerate(finished_tiles):
        for picture_x, slot in enumerate(slot_row):
            tile = tiles[slot["tile"][0]]
            for tile_y, tile_row in enumerate(tile.tile_pattern[1:-1]):
                if picture_x == 0:
                    finished_picture.append([])
                for tile_x, pixel in enumerate(tile_row[1:-1]):
                    if (picture_x * tile_row_count + tile_x, picture_y * tile_row_count + tile_y) in positive_pixels:
                        finished_picture[picture_y * tile_row_count + tile_y].append(True)
                    else:
                        finished_picture[picture_y * tile_row_count + tile_y].append(False)

    return count_sea_monsters(finished_picture)
                    

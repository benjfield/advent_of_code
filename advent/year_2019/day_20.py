from advent.runner import register
from advent.utils.path_finding import Node, NodeStore
from advent.utils.direction import Direction

class TeleportNode(Node):
    def __init__(self, inner_x, inner_y, outer_x, outer_y):
       self.inner_x = inner_x
       self.inner_y = inner_y
       self.outer_x = outer_x
       self.outer_y = outer_y

    def get_neighbours(self, final_x, final_y, map, teleporters):
        neighbours = []

        for x, y in [
            (self.inner_x - 1, self.inner_y), 
            (self.inner_x + 1, self.inner_y), 
            (self.inner_x, self.inner_y - 1), 
            (self.inner_x, self.inner_y + 1),
            (self.outer_x - 1, self.outer_y), 
            (self.outer_x + 1, self.outer_y), 
            (self.outer_x, self.outer_y - 1), 
            (self.outer_x, self.outer_y + 1)
            ]:
            if self.check_valid_neighbour(x, y, final_x, final_y):
                if map[y][x] == ".":
                    possible_neighbour = NodeWithTeleporters(
                        x=x,
                        y=y,
                    )
                    neighbours.append(possible_neighbour)
        return neighbours
            
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        if self.inner_x == other.inner_x and self.inner_y == other.inner_y and self.outer_x == other.outer_x and self.outer_y == other.outer_y:
            return True
        return False
    
    def __str__(self):
        return f"x {self.inner_x} y {self.inner_y} x_2 {self.outer_x} y_2 {self.outer_y}"
    
    @classmethod
    def is_teleporter(cls):
        return True
    
class NodeWithTeleporters(Node):    
    def get_neighbours(self, final_x, final_y, map, teleporters):
        neighbours = []

        for x, y in [(self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]:
            if self.check_valid_neighbour(x, y, final_x, final_y):
                if map[y][x] == ".":
                    possible_neighbour = NodeWithTeleporters(
                        x=x,
                        y=y,
                    )
                    neighbours.append(possible_neighbour)
                elif map[y][x].isalpha():
                    possible_neighbour = NodeWithTeleporters(
                        x=x,
                        y=y,
                    )
                    if str(possible_neighbour) in teleporters:
                        neighbour_details = teleporters[str(possible_neighbour)]
                        possible_neighbour = TeleportNode(
                            neighbour_details["inner_x"],
                            neighbour_details["inner_y"],
                            neighbour_details["outer_x"],
                            neighbour_details["outer_y"],
                        )
                        neighbours.append(possible_neighbour)

        return neighbours

    @classmethod
    def is_teleporter(cls):
        return False
    
def djikstra(map, start_x, start_y, node_type=Node, end_x=None, end_y=None, teleporters=None):
    start_point = node_type(start_x, start_y)

    open_list = NodeStore()

    closed_list = NodeStore()

    final_x = len(map[0]) - 1
    final_y = len(map) - 1
    
    open_list.store_node(start_point, 0)

    while len(open_list.store) > 0:
        current_square, current_square_cost = open_list.get_lowest_cost_node()
        if end_x is not None and end_y is not None:
            if not current_square.is_teleporter():
                if current_square.x == end_x and current_square.y == end_y:
                    return current_square_cost

        closed_list.store_node(current_square, current_square_cost)

        neighbours = current_square.get_neighbours(final_x, final_y, map, teleporters)


        for neighbour in neighbours:
            if neighbour in closed_list.store:
                pass
            else:
                if current_square.is_teleporter():
                    open_list.store_node(neighbour, current_square_cost)
                else:
                    open_list.store_node(neighbour, current_square_cost + 1)

    return closed_list

def get_precalced_details(split_text):
    
    half_teleporters = {}
    teleporters = {}

    start_x = 0
    start_y = 0

    end_x = 0
    end_y = 0

    #prepopulate teleporters and start
    for y, row in enumerate(split_text):
        for x, tile in enumerate(row):
            if tile.isalpha():
                teleporter=False
                teleporter_name = ""
                potential_x = 0
                potential_y = 0
                for check_x, check_y in [
                    (x - 1, y), 
                    (x + 1, y), 
                    (x, y - 1), 
                    (x, y + 1)
                    ]:
                    if check_x >= 0 and check_x < len(row) and check_y >= 0 and check_y < len(split_text):
                        if split_text[check_y][check_x] == ".":
                            teleporter = True
                            potential_x = check_x
                            potential_y = check_y
                        elif split_text[check_y][check_x].isalpha():
                            first_letter = False
                            for direction in [Direction.RIGHT, Direction.DOWN]:
                                direction_x, direction_y = direction.move_forward(x, y)
                                if direction_x == check_x and direction_y == check_y:
                                    first_letter = True

                            if first_letter:
                                teleporter_name = tile + split_text[check_y][check_x]
                            else:
                                teleporter_name = split_text[check_y][check_x] + tile

                if teleporter:
                    outer = False
                    if x == 1 or y == 1 or x == len(row) - 2 or y == len(split_text) - 2:
                        outer = True

                    if teleporter_name in half_teleporters:
                        if outer:
                            node_details = {
                                "inner_x": half_teleporters[teleporter_name]["x"],
                                "inner_y": half_teleporters[teleporter_name]["y"],
                                "outer_x": x,
                                "outer_y": y
                            }
                        else:
                            node_details = {
                                "inner_x": x,
                                "inner_y": y,
                                "outer_x": half_teleporters[teleporter_name]["x"],
                                "outer_y": half_teleporters[teleporter_name]["y"]
                            }

                        teleporters[f"x {x} y {y}"] = node_details
                        teleporters[f"x {half_teleporters[teleporter_name]['x']} y {half_teleporters[teleporter_name]['y']}"] = node_details
                    else:
                        half_teleporters[teleporter_name] = {
                            "x": x,
                            "y": y
                        }
                    
                    if teleporter_name == "AA":
                        start_x = potential_x
                        start_y = potential_y
                    elif teleporter_name == "ZZ":
                        end_x = potential_x
                        end_y = potential_y

    return teleporters, start_x, start_y, end_x, end_y

@register(20, 2019, 1)
def teleport_1(text):
    split_text = text.split("\n")

    teleporters, start_x, start_y, end_x, end_y = get_precalced_details(split_text)

    return djikstra(split_text, start_x, start_y, NodeWithTeleporters, end_x, end_y, teleporters)

class RecursiveTeleportNode(TeleportNode):
    def __init__(self, inner_x, inner_y, outer_x, outer_y, inner_level=None, outer_level=None):
        super().__init__(inner_x, inner_y, outer_x, outer_y)
        if inner_level is None and outer_level is None:
            raise Exception("Missing levels!")
        if inner_level is not None:
            self.inner_level = inner_level
            self.outer_level = inner_level + 1
        elif outer_level is not None:
            self.inner_level = outer_level - 1
            self.outer_level = outer_level

    def get_neighbours(self, final_x, final_y, map, teleporters):
        neighbours = []

        for x, y, level in [
            (self.inner_x - 1, self.inner_y, self.inner_level), 
            (self.inner_x + 1, self.inner_y, self.inner_level), 
            (self.inner_x, self.inner_y - 1, self.inner_level), 
            (self.inner_x, self.inner_y + 1, self.inner_level),
            (self.outer_x - 1, self.outer_y, self.outer_level), 
            (self.outer_x + 1, self.outer_y, self.outer_level), 
            (self.outer_x, self.outer_y - 1, self.outer_level), 
            (self.outer_x, self.outer_y + 1, self.outer_level)
            ]:
            if self.check_valid_neighbour(x, y, final_x, final_y) and level >= 0:
                if map[y][x] == ".":
                    possible_neighbour = RecursiveNodeWithTeleporters(
                        x=x,
                        y=y,
                        level=level
                    )
                    neighbours.append(possible_neighbour)
        return neighbours
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        if self.inner_x == other.inner_x and self.inner_y == other.inner_y and self.outer_x == other.outer_x and self.outer_y == other.outer_y and self.inner_level == other.inner_level  and self.outer_level == other.outer_level:
            return True
        return False
    
    def __str__(self):
        return f"inner_x {self.inner_x} inner_y {self.inner_y} outer_x {self.outer_x} outer_y {self.outer_y} inner_level {self.inner_level} outer_level {self.outer_level}"
    
class RecursiveNodeWithTeleporters(NodeWithTeleporters):    
    def __init__(self, x, y, level):
       super()
       self.x = x
       self.y = y
       self.level = level

    def get_neighbours(self, final_x, final_y, map, teleporters):
        neighbours = []

        for x, y in [(self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]:
            if self.check_valid_neighbour(x, y, final_x, final_y):
                if map[y][x] == ".":
                    possible_neighbour = RecursiveNodeWithTeleporters(
                        x=x,
                        y=y,
                        level=self.level
                    )
                    neighbours.append(possible_neighbour)
                elif map[y][x].isalpha():
                    neighbour_string = f"x {x} y {y}"
                    if neighbour_string in teleporters:
                        neighbour_details = teleporters[neighbour_string]
                        if x == neighbour_details["inner_x"] and y == neighbour_details["inner_y"]:
                            possible_neighbour = RecursiveTeleportNode(
                                neighbour_details["inner_x"],
                                neighbour_details["inner_y"],
                                neighbour_details["outer_x"],
                                neighbour_details["outer_y"],
                                inner_level=self.level
                            )
                        else:
                            possible_neighbour = RecursiveTeleportNode(
                                neighbour_details["inner_x"],
                                neighbour_details["inner_y"],
                                neighbour_details["outer_x"],
                                neighbour_details["outer_y"],
                                outer_level=self.level
                            )

                        neighbours.append(possible_neighbour)

        return neighbours
        
    def __hash__(self):
        return hash(str(self))
    
    def __str__(self):
        return f"x {self.x} y {self.y} level {self.level}"
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.level == other.level:
            return True
        return False

    
def djikstra_with_recursive_levels(map, start_x, start_y, end_x=None, end_y=None, teleporters=None):
    start_point = RecursiveNodeWithTeleporters(start_x, start_y, 0)

    open_list = NodeStore()

    closed_list = NodeStore()

    final_x = len(map[0]) - 1
    final_y = len(map) - 1
    
    open_list.store_node(start_point, 0)

    while len(open_list.store) > 0:
        current_square, current_square_cost = open_list.get_lowest_cost_node()
        if end_x is not None and end_y is not None:
            if not current_square.is_teleporter():
                if current_square.x == end_x and current_square.y == end_y and current_square.level == 0:
                    return current_square_cost

        closed_list.store_node(current_square, current_square_cost)

        neighbours = current_square.get_neighbours(final_x, final_y, map, teleporters)

        for neighbour in neighbours:
            if neighbour in closed_list.store:
                pass
            else:
                if current_square.is_teleporter():
                    open_list.store_node(neighbour, current_square_cost)
                else:
                    open_list.store_node(neighbour, current_square_cost + 1)


    return closed_list

@register(20, 2019, 2)
def teleport_2(text):
    split_text = text.split("\n")

    teleporters, start_x, start_y, end_x, end_y = get_precalced_details(split_text)

    return djikstra_with_recursive_levels(split_text, start_x, start_y, end_x, end_y, teleporters)
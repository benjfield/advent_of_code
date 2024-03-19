from enum import Enum
from advent.utils.path_finding import Node, djikstra, NodeStore, NodeStoreWithPath, NodeWithPath
from functools import partial
from advent.runner import register

class SpaceType(Enum):
    HALL = 0
    ROOM = 1
    ENTRANCE = 2

class Space:
    def __init__(
            self,
            space_type,
            allowed,
            coord
        ):
        self.space_type = space_type
        self.coord = coord
        self.allowed = allowed

        self.initial_neighbours = []
        self.neighbours = []

    def populate_neighbours(
        self,
        spaces
    ): 
        for coord in [
            (self.coord[0] - 1, self.coord[1]),
            (self.coord[0] + 1, self.coord[1]),
            (self.coord[0], self.coord[1] - 1),
            (self.coord[0], self.coord[1] + 1)
        ]:
            if coord in spaces:
                self.initial_neighbours.append(spaces[coord])
                if self.space_type == SpaceType.HALL and coord[1] == self.coord[1] + 1:
                    self.space_type = SpaceType.ENTRANCE

    def build_paths(
        self,
        start_coord,
        start_type,
        path,
        cost,
        destinations,
        visited
    ):
        if self.coord != start_coord:
            cost += 1

            if self.space_type != SpaceType.ENTRANCE:
                path = path.copy()
                path.append(self.coord)
            
            if (start_type == SpaceType.HALL and self.space_type == SpaceType.ROOM) or (start_type == SpaceType.ROOM and self.space_type != SpaceType.ENTRANCE):
                destinations.append({
                    "destination": self.coord,
                    "path": path,
                    "allowed": self.allowed,
                    "cost": cost
                })

        visited = visited.copy()
        visited.add(self.coord)

        for neighbour in self.initial_neighbours:
            if neighbour.coord not in visited:
                destinations = neighbour.build_paths(
                    start_coord,
                    start_type,
                    path,
                    cost,
                    destinations,
                    visited
                )
        
        return destinations
    
    def get_neighbours(
        self
    ):
        self.build_paths(
            self.coord,
            self.space_type,
            [],
            0,
            self.neighbours,
            set()
        )

class State(): 
    def __init__(
        self,
        state_tuple
        ):
        self.state_tuple = state_tuple

    def __hash__(self):
        return hash(self.state_tuple)
    
    def __eq__(self, other):
        if self.state_tuple == other.state_tuple:
            return True
        return False
    
    def get_neighbours(
            self,
            map,
            cost):
        neighbours = []
        for coord, index in map["coords_to_tuple"].items():
            if self.state_tuple[index] != "":
                valid_start = True 
                if self.state_tuple[index] == map["required_state"][index]:  
                    dependencies_filled = True 
                    for dependency_coord in map["dependencies"][coord]:
                        dependency_index = map["coords_to_tuple"][dependency_coord]
                        if self.state_tuple[dependency_index] != map["required_state"][dependency_index]:
                            dependencies_filled = False
                            break
                    if dependencies_filled:
                        valid_start = False

                if valid_start:
                    for destination in map["spaces"][coord].neighbours:
                        end_index =  map["coords_to_tuple"][destination["destination"]]
                        if self.state_tuple[index] in destination["allowed"] and self.state_tuple[end_index] == "":
                            valid_end = True 
                            #Will already be allowed
                            if map["required_state"][end_index] != "":
                                dependencies_filled = True 
                                for dependency_coord in map["dependencies"][destination["destination"]]:
                                    dependency_index = map["coords_to_tuple"][dependency_coord]
                                    if self.state_tuple[dependency_index] != map["required_state"][dependency_index]:
                                        dependencies_filled = False
                                        break
                                if not dependencies_filled:
                                    valid_end = False
                            if valid_end:
                                blocked = False
                                for in_between in destination["path"]:
                                    in_between_index = map["coords_to_tuple"][in_between]
                                    if self.state_tuple[in_between_index] != "":
                                        blocked = True
                                        break
                                if not blocked:
                                    new_state = list(self.state_tuple)
                                    move_cost_multiplier = map["multipliers"][new_state[index]]
                                    new_state[end_index] = new_state[index]
                                    new_state[index] = ""
                                    neighbours.append({
                                        "neighbour": State(tuple(new_state)),
                                        "cost": cost + destination["cost"] * move_cost_multiplier
                                    })
        return neighbours
    
    def __str__(self):
        return str(self.state_tuple)

def djikstra_terminate_amphipod(required_state_tuple, current_state):
    if current_state.state_tuple == required_state_tuple: 
        return True
    return False

def djikstra_terminate_amphipod_function(required_state_tuple):
    return partial(djikstra_terminate_amphipod, required_state_tuple)

def generate_map(split_text):

    required_state_list = []
    state_list = []
    spaces_dict = {}
    coords_to_tuple = {}
    dependencies = {}

    for y, line in enumerate(split_text):
        for x, char in enumerate(line):
            if char != "#" and char != " ":
                if char == ".":
                    state_list.append("")
                else:
                    state_list.append(char)
                coords = (x, y)
                coords_to_tuple[coords] = len(state_list) - 1

                if y == 1:
                    this_space = Space(
                        SpaceType.HALL,
                        {"A", "B", "C", "D"},
                        coords
                    )
                    required_state_list.append("")
                else:
                    if x == 3:
                        required_letter = "A"
                    elif x == 5:
                        required_letter = "B"
                    elif x == 7:
                        required_letter = "C"
                    elif x == 9:
                        required_letter = "D"

                    this_space = Space(
                        SpaceType.ROOM,
                        {required_letter},
                        coords
                    )
                    required_state_list.append(required_letter)

                    if y < len(split_text) - 1:
                        dependencies[coords] = []
                        for dependent_y in range(y + 1, len(split_text) - 1):
                            dependencies[coords].append((x, dependent_y))
                spaces_dict[coords] = this_space
    
    for space in spaces_dict.values():
        space.populate_neighbours(spaces_dict)

    for space in spaces_dict.values():
        space.get_neighbours()

    move_state_multipliers = {
        "A": 1,
        "B": 10,
        "C": 100,
        "D": 1000
    }

    start_point = State(tuple(state_list))

    required_state_tuple = tuple(required_state_list)

    return {
        "required_state": required_state_tuple,
        "dependencies": dependencies,
        "coords_to_tuple": coords_to_tuple,
        "spaces": spaces_dict,
        "multipliers": move_state_multipliers
    }, start_point, djikstra_terminate_amphipod_function(required_state_tuple)

@register(23, 2021, 1)
def amphipod_1(text):
    split_text = text.split("\n")
    
    map, start_point, djikstra_terminate_function = generate_map(split_text)

    return djikstra(map, start_point, False, djikstra_terminate_function)

@register(23, 2021, 2)
def amphipod_2(text):
    split_text_old = text.split("\n")

    split_text = split_text_old[:3]
    split_text.append("  #D#C#B#A#  ")
    split_text.append("  #D#B#A#C#  ")
    split_text += split_text_old[3:]

    map, start_point, djikstra_terminate_function = generate_map(split_text)

    return djikstra(map, start_point, False, djikstra_terminate_function)
                



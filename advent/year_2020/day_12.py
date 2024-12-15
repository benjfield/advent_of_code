from advent.runner import register
from advent.utils.direction import Direction

class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = Direction.RIGHT

    def take_action(self, letter, number):
        match letter:
            case "N":
                self.y -= number
            case "S":
                self.y += number
            case "E":
                self.x += number
            case "W":
                self.x -= number
            case "L":
                if number % 90 != 0:
                    raise NotImplementedError
                for i in range(int(number/90)):
                    self.direction = self.direction.rotate(False)
            case "R":
                if number % 90 != 0:
                    raise NotImplementedError
                for i in range(int(number/90)):
                    self.direction = self.direction.rotate(True)
            case "F":
                self.x, self.y = self.direction.move_forward_x_and_y(self.x, self.y, number)
     
@register(12, 2020, 1, True)
def rain_risk_1(split_text):
    ship = Ship()
    
    for line in split_text:
        letter = line[0]
        number = int(line[1:])

        ship.take_action(letter, number)

    return abs(ship.x) + abs(ship.y)
     
class Waypoint:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = -1
           
    def take_action(self, letter, number):
        match letter:
            case "N":
                self.waypoint_y -= number
            case "S":
                self.waypoint_y += number
            case "E":
                self.waypoint_x += number
            case "W":
                self.waypoint_x -= number
            case "L":
                if number % 90 != 0:
                    raise NotImplementedError
                for i in range(int(number/90)):
                    x = self.waypoint_x
                    y = self.waypoint_y
                    self.waypoint_x = y
                    self.waypoint_y = -1 * x
            case "R":
                if number % 90 != 0:
                    raise NotImplementedError
                for i in range(int(number/90)):
                    x = self.waypoint_x
                    y = self.waypoint_y
                    self.waypoint_x = -1 * y
                    self.waypoint_y = x
            case "F":
                self.x += self.waypoint_x * number
                self.y += self.waypoint_y * number

    def __str__(self):
        return f"ship: {self.x}, {self.y}, waypoint: {self.waypoint_x}, {self.waypoint_y}"

@register(12, 2020, 2, True)
def rain_risk_2(split_text):
    ship = Waypoint()
    
    for line in split_text:
        letter = line[0]
        number = int(line[1:])

        ship.take_action(letter, number)

    return abs(ship.x) + abs(ship.y)

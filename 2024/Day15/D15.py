from collections import defaultdict
from collections import deque


class sim:
    def __init__(self):
        self.warehouse = defaultdict(lambda: ".")

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def add_robot(self, x, y):
        self.warehouse[(x, y)] = "@"
        self.robotPos = (x, y)

    def add_wall(self, x, y):
        self.warehouse[(x, y)] = "#"
        self.warehouse[(x + 1, y)] = "#"

    def add_box(self, x, y):
        self.warehouse[(x, y)] = "["
        self.warehouse[(x + 1, y)] = "]"

    def move(self, direction):
        moveQueue = deque()
        x, y = self.robotPos
        moveQueue.append((x, y))
        # add everything to queue
        pos = 0
        while pos < len(moveQueue):
            x, y = moveQueue[pos]
            symbol = self.warehouse[(x, y)]
            if symbol == "#":  # hit a wall so don't move anything
                return False
            elif self.warehouse[(x, y)] == ".":
                moveQueue.remove((x, y))
                continue
            if direction == "^":
                newX, newY = x, y - 1
            elif direction == "v":
                newX, newY = x, y + 1
            elif direction == ">":
                newX, newY = x + 1, y
            elif direction == "<":
                newX, newY = x - 1, y
            if (newX, newY) not in moveQueue:
                moveQueue.append((newX, newY))

            if direction == "v" or direction == "^":
                if self.warehouse[(newX, newY)] == "[":
                    if (newX + 1, newY) not in moveQueue:
                        moveQueue.append((newX + 1, newY))
                elif self.warehouse[(newX, newY)] == "]":
                    if (newX - 1, newY) not in moveQueue:
                        moveQueue.append((newX - 1, newY))
            pos += 1

        # move everything
        while moveQueue:
            x, y = moveQueue.pop()
            symbol = self.warehouse[(x, y)]
            if direction == "^":
                newX, newY = x, y - 1
            elif direction == "v":
                newX, newY = x, y + 1
            elif direction == ">":
                newX, newY = x + 1, y
            elif direction == "<":
                newX, newY = x - 1, y
            if symbol == "@":
                self.robotPos = (newX, newY)
            self.warehouse[(newX, newY)] = symbol
            self.warehouse[(x, y)] = "."
            pass

    def warehouse_to_string(self):
        warehouse = ""
        for y in range(self.height):
            for x in range(self.width):
                warehouse += self.warehouse[(x, y)]
            warehouse += "\n"
        return warehouse

    def get_score(self):
        total = 0
        for key in [a for a in self.warehouse.keys() if self.warehouse[a] == "["]:
            total += 100 * key[1] + key[0]
        return total


with open("2024/Day15/input.txt", "r") as input:
    warehouse, movements = input.read().split("\n\n")
    y = 0
    simulation = sim()
    for line in warehouse.splitlines():
        x = 0
        for char in line:
            if char == "#":
                simulation.add_wall(x * 2, y)
            elif char == "@":
                simulation.add_robot(x * 2, y)
            elif char == "O":
                simulation.add_box(x * 2, y)
            x += 1
        simulation.set_width(x * 2)
        y += 1
    simulation.set_height(y)
    for move in movements.replace("\n", ""):
        simulation.move(move)
    print(simulation.warehouse_to_string())
    print(simulation.get_score())

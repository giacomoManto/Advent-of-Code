import re

size = 101, 103


class Robot:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.size = size

    def move(self, time):
        newx = (self.pos[0] + self.vel[0] * time) % self.size[0]
        newy = (self.pos[1] + self.vel[1] * time) % self.size[1]
        self.pos = newx, newy

    def quad(self):
        if self.pos[0] < (size[0] - 1) / 2:
            if self.pos[1] < (size[1] - 1) / 2:
                return 1
            elif self.pos[1] > (size[1] - 1) / 2:
                return 3
        elif self.pos[0] > (size[0] - 1) / 2:
            if self.pos[1] < (size[1] - 1) / 2:
                return 2
            elif self.pos[1] > (size[1] - 1) / 2:
                return 4
        return 0


def show_robots_on_grid(robots):
    grid = {}

    for robot in robots:
        grid[robot.pos] = grid.get(robot.pos, 0) + 1
    output = ""
    for y in range(size[1]):
        for x in range(size[0]):
            if x == (size[0] - 1) / 2 or y == (size[1] - 1) / 2:
                output += " "
            else:
                output += str(grid.get((x, y), "."))
        output += "\n"
    return output


with open("2024/Day14/input.txt", "r") as input_file:
    robot_search = re.compile(r"p=(-?\d*),(-?\d*) v=(-?\d*),(-?\d*)")
    robots = []
    for line in input_file.readlines():
        robot_input = robot_search.match(line)
        robots.append(
            Robot(
                (int(robot_input.group(1)), int(robot_input.group(2))),
                (int(robot_input.group(3)), int(robot_input.group(4))),
            )
        )


for a in range(10000):
    quad = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    for robot in robots:
        robot.move(1)
        quad[robot.quad()] += 1
    middle_count = 0
    for robot in robots:
        if (
            abs(robot.pos[0] - (size[0] - 1) / 2) <= 10
            and abs(robot.pos[1] - (size[1] - 1) / 2) <= 10
        ):
            middle_count += 1

    if middle_count > 0:
        ratio = middle_count / len(robots)
        if ratio > 0.2:
            print(
                f"At step {a}, robots are clustered near the middle with ratio: {ratio:.2f}"
            )
            with open(f"2024/Day14/step{a + 1}.txt", "w") as output_file:
                output_file.write(show_robots_on_grid(robots))

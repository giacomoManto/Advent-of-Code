import re
import math
from collections import deque
import sys


class ClawMachine:
    acost = 3
    bcost = 1

    def __init__(self, button_a, button_b, target):
        self.button_a = button_a
        self.button_b = button_b
        self.target = target

    def can_make_target(self):
        return (
            self.target[0] % math.gcd(self.button_a[0], self.button_b[0]) == 0
            and self.target[1] % math.gcd(self.button_a[1], self.button_b[1]) == 0
        )

    def linear_solve(self):
        coefficient_a = (
            self.target[0] * self.button_b[1] - self.target[1] * self.button_b[0]
        ) / (self.button_a[0] * self.button_b[1] - self.button_a[1] * self.button_b[0])

        if coefficient_a != int(coefficient_a):
            return 0

        coefficient_b = (
            self.target[0] - coefficient_a * self.button_a[0]
        ) / self.button_b[0]

        if coefficient_b != int(coefficient_b):
            return 0

        return int(coefficient_a * self.acost + coefficient_b * self.bcost)

    def min_moves_to_target(self):
        if not self.can_make_target():
            return 0
        target_x, target_y = self.target
        queue = deque([(0, 0, 0, 0)])  # (curx, cury, a_presses, b_presses)
        visited = set()

        lowestCost = sys.maxsize

        while queue:
            curx, cury, a_presses, b_presses = queue.popleft()

            if (
                (
                    curx,
                    cury,
                    a_presses * self.acost + b_presses * self.bcost,
                )
                in visited
                or a_presses * self.acost + b_presses * self.bcost >= lowestCost
            ):
                continue

            if (curx, cury) == (target_x, target_y):
                lowestCost = min(
                    lowestCost, a_presses * self.acost + b_presses * self.bcost
                )
                continue

            visited.add((curx, cury, a_presses * self.acost + b_presses * self.bcost))

            queue.append(
                (
                    curx + self.button_a[0],
                    cury + self.button_a[1],
                    a_presses + 1,
                    b_presses,
                )
            )
            queue.append(
                (
                    curx + self.button_b[0],
                    cury + self.button_b[1],
                    a_presses,
                    b_presses + 1,
                )
            )
        if lowestCost == sys.maxsize:
            return 0
        return lowestCost


def parse_data(file_path, offset=0):
    with open(file_path, "r") as file:
        lines = file.readlines()

    data = []
    button_pattern = re.compile(r".*?X([\+-]\d*), Y([\+-]\d*)")
    target_pattern = re.compile(r"X=(\d+), Y=(\d+)")

    for i in range(0, len(lines), 4):
        button_a_line = lines[i].strip()
        button_b_line = lines[i + 1].strip()
        target_line = lines[i + 2].strip()

        button_a_match = button_pattern.search(button_a_line)
        button_b_match = button_pattern.search(button_b_line)
        target_match = target_pattern.search(target_line)

        if button_a_match and button_b_match and target_match:
            button_a = (int(button_a_match.group(1)), int(button_a_match.group(2)))
            button_b = (int(button_b_match.group(1)), int(button_b_match.group(2)))
            target = (
                int(target_match.group(1)) + offset,
                int(target_match.group(2)) + offset,
            )

            data.append(ClawMachine(button_a, button_b, target))

    return data


file_path = "2024/Day13/input.txt"
data = parse_data(file_path)

print(f"Part one: {sum([claw_machine.linear_solve() for claw_machine in data])}")

data2 = parse_data(file_path, 10000000000000)
print(f"Part two: {sum([claw_machine.linear_solve() for claw_machine in data2])}")

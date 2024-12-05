import re
from collections import defaultdict

inputfile = "2015/Day6/input.txt"

search = re.compile(
    r"(toggle|turn off|turn on) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})"
)

commands = []
lights = defaultdict(lambda: bool(False))
lights2 = defaultdict(lambda: int(0))
with open(inputfile, "r") as input:
    for line in input.read().splitlines():
        result = search.match(line)
        command = result.group(1)
        sx, sy = int(result.group(2)), int(result.group(3))
        ex, ey = int(result.group(4)), int(result.group(5))

        if command == "turn on":
            for x in range(sx, ex + 1):
                for y in range(sy, ey + 1):
                    lights[(x, y)] = True
                    lights2[(x, y)] += 1
        elif command == "turn off":
            for x in range(sx, ex + 1):
                for y in range(sy, ey + 1):
                    lights[(x, y)] = False
                    lights2[(x, y)] = max(0, lights2[(x, y)] - 1)
        elif command == "toggle":
            for x in range(sx, ex + 1):
                for y in range(sy, ey + 1):
                    lights[(x, y)] = not lights[(x, y)]
                    lights2[(x, y)] += 2
totalon = 0
total2 = 0
for key in lights.keys():
    if lights[key]:
        totalon += 1
    total2 += lights2[key]

print(f"Part one: {totalon}")
print(f"Part two: {total2}")

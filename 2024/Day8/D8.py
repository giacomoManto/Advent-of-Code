from collections import defaultdict

inputfile = "2024/Day8/input.txt"


positions = defaultdict(list)
height = 0
width = 0
with open(inputfile, "r") as input:
    data = input.read()
    y = 0
    for line in data.splitlines():
        x = 0
        width = len(line)
        for char in line:
            if char != ".":
                positions[char].append((x, y))
            x += 1
        y += 1
    height = y
antinodes = set()


def withinBounds(point) -> bool:
    if point[0] < 0 or point[1] < 0:
        return False
    if point[0] >= width or point[1] >= height:
        return False
    return True


for key in positions.keys():
    for first in range(len(positions[key])):
        for second in range(first + 1, len(positions[key])):
            antinodes.add(positions[key][first])
            antinodes.add(positions[key][second])
            diff = (
                positions[key][second][0] - positions[key][first][0],
                positions[key][second][1] - positions[key][first][1],
            )
            count = 1
            while True:
                a1 = (
                    positions[key][first][0] - diff[0] * count,
                    positions[key][first][1] - diff[1] * count,
                )
                if withinBounds(a1):
                    antinodes.add(a1)
                else:
                    break
                count += 1
            count = 1
            while True:
                a2 = (
                    positions[key][second][0] + diff[0] * count,
                    positions[key][second][1] + diff[1] * count,
                )

                if withinBounds(a2):
                    antinodes.add(a2)
                else:
                    break
                count += 1

print(len(antinodes))
print(antinodes)

from collections import defaultdict

inputFile = "2024/Day12/input.txt"


with open(inputFile, "r") as input:
    data = input.read().split("\n")
    data = [list(x) for x in data]

seen = defaultdict(lambda: False)


def traverse(x, y, char) -> tuple[int, int]:
    if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]):
        return 0, 1
    if data[x][y] != char:
        return 0, 1
    if seen[(x, y)]:
        return 0, 0

    seen[(x, y)] = True
    area = 1
    perimeter = 0

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        a, p = traverse(x + dx, y + dy, char)
        area += a
        perimeter += p

    return area, perimeter


price = 0

for x in range(len(data)):
    for y in range(len(data[x])):
        if seen[(x, y)]:
            continue
        a, p = traverse(x, y, data[x][y])
        price += a * p
print(f"Part 1: {price}")

seen = defaultdict(lambda: False)


def checkSurrounding(x, y, char) -> bool:
    if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]):
        return False
    return data[x][y] == char


def findAreaAndSides(x, y, char) -> tuple[int, int]:
    if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]):
        return 0, 0
    if data[x][y] != char:
        return 0, 0
    if seen[(x, y)]:
        return 0, 0

    seen[(x, y)] = True
    area = 1
    sides = 0

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        a, s = findAreaAndSides(x + dx, y + dy, char)
        area += a
        sides += s

    if not checkSurrounding(x + 1, y, char) and not checkSurrounding(x, y + 1, char):
        sides += 1
    if not checkSurrounding(x + 1, y, char) and not checkSurrounding(x, y - 1, char):
        sides += 1
    if not checkSurrounding(x - 1, y, char) and not checkSurrounding(x, y + 1, char):
        sides += 1
    if not checkSurrounding(x - 1, y, char) and not checkSurrounding(x, y - 1, char):
        sides += 1
    if (
        checkSurrounding(x + 1, y, char)
        and checkSurrounding(x, y + 1, char)
        and not checkSurrounding(x + 1, y + 1, char)
    ):
        sides += 1
    if (
        checkSurrounding(x + 1, y, char)
        and checkSurrounding(x, y - 1, char)
        and not checkSurrounding(x + 1, y - 1, char)
    ):
        sides += 1
    if (
        checkSurrounding(x - 1, y, char)
        and checkSurrounding(x, y + 1, char)
        and not checkSurrounding(x - 1, y + 1, char)
    ):
        sides += 1
    if (
        checkSurrounding(x - 1, y, char)
        and checkSurrounding(x, y - 1, char)
        and not checkSurrounding(x - 1, y - 1, char)
    ):
        sides += 1

    return area, sides


price = 0

for x in range(len(data)):
    for y in range(len(data[x])):
        if seen[(x, y)]:
            continue
        a, p = findAreaAndSides(x, y, data[x][y])
        price += a * p
        # Debugging
        # print(f"char`{data[x][y]}`: {a} * {p} = {a*p}")
print(f"Part 1: {price}")

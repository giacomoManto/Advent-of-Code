inputfile = "2024/Day10/input.txt"

with open(inputfile, "r") as input:
    data = input.read().splitlines()


def harness(x, y):
    return x < 0 or y < 0 or y >= len(data) or x >= len(data[y])


peaks = set()
trailheads = {}


def hike(x, y, prev, start, visited):
    if (x, y) in visited or harness(x, y) or int(data[y][x]) != prev + 1:
        return
    num = int(data[y][x])
    visited.add((x, y))
    if num == 9:
        peaks.add((x, y))
        trailheads[start] += 1
    else:
        hike(x - 1, y, num, start, visited)
        hike(x + 1, y, num, start, visited)
        hike(x, y - 1, num, start, visited)
        hike(x, y + 1, num, start, visited)


def hikeUnique(x, y, prev, visited):
    if (x, y) in visited or harness(x, y) or int(data[y][x]) != prev + 1:
        return 0
    if int(data[y][x]) == 9:
        return 1
    else:
        return (
            hikeUnique(x - 1, y, int(data[y][x]), visited.copy())
            + hikeUnique(x + 1, y, int(data[y][x]), visited.copy())
            + hikeUnique(x, y - 1, int(data[y][x]), visited.copy())
            + hikeUnique(x, y + 1, int(data[y][x]), visited.copy())
        )


p2 = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if int(data[y][x]) == 0:
            trailheads[(x, y)] = 0
            hike(x, y, -1, (x, y), set())
            p2 += hikeUnique(x, y, -1, set())

print(f"Part one: {sum(trailheads.values())}")
print(f"Part two: {p2}")

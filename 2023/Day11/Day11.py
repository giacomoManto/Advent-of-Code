import time

data: list[list] = []  # stored as [row][column]
for line in open("input.txt", "r").readlines():
    row = []
    for char in line.removesuffix("\n"):
        row.append(char)
    data.append(row)

# Expanding columns
expandingColumns = []
for column in range(len(data[0])):
    expanding = True
    for row in range(len(data)):
        if data[row][column] != ".":
            expanding = False
            break

    if expanding:
        expandingColumns.append(column)

# expand rows
expandingRows = []
for row in range(len(data)):
    if data[row].count(".") == len(data[row]):
        expandingRows.append(row)

galaxies = []

for row in range(len(data)):
    for column in range(len(data[row])):
        if data[row][column] == "#":
            galaxies.append((row, column))


def shortestPaths(multiplier):
    sum = 0
    meow = 0
    for g1 in range(len(galaxies) - 1):
        for g2 in range(g1 + 1, len(galaxies)):
            meow += 1
            rowRange = range(0)
            colRange = range(0)

            if galaxies[g1][0] > galaxies[g2][0]:
                rowRange = range(galaxies[g2][0], galaxies[g1][0])
            else:
                rowRange = range(galaxies[g1][0], galaxies[g2][0])
            if galaxies[g1][1] > galaxies[g2][1]:
                colRange = range(galaxies[g2][1], galaxies[g1][1])
            else:
                colRange = range(galaxies[g1][1], galaxies[g2][1])

            for row in rowRange:
                if row in expandingRows:
                    sum += multiplier
                else:
                    sum += 1
            for col in colRange:
                if col in expandingColumns:
                    sum += multiplier
                else:
                    sum += 1
    print(meow)
    return sum


# part1
start = time.time()
result = shortestPaths(2)
end = time.time()
print("Part 1: %d | Time: %f" % (result, (end - start)))

# part2
start = time.time()
result = shortestPaths(1000000)
end = time.time()
print("Part 2: %d | Time: %f" % (result, (end - start)))

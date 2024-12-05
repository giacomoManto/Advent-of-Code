inputfile = "2015/Day3/input.txt"

with open(inputfile, "r") as input:
    instructions = input.read().removesuffix("\n")

visitedYearOne = set()
x, y = 0, 0
visitedYearOne.add((x, y))

visitedYearTwo = set()
x0, y0 = 0, 0
x1, y1 = 0, 0
visitedYearTwo.add((0, 0))
santaMove = True
for instruct in instructions:
    if instruct == ">":
        x += 1
        if santaMove:
            x0 += 1
        else:
            x1 += 1
    elif instruct == "<":
        x -= 1
        if santaMove:
            x0 -= 1
        else:
            x1 -= 1
    elif instruct == "^":
        y += 1
        if santaMove:
            y0 += 1
        else:
            y1 += 1
    elif instruct == "v":
        y -= 1
        if santaMove:
            y0 -= 1
        else:
            y1 -= 1

    santaMove = not santaMove
    visitedYearOne.add((x, y))
    visitedYearTwo.add((x0, y0))
    visitedYearTwo.add((x1, y1))

print(f"Part one: {len(visitedYearOne)}")
print(f"Part two: {len(visitedYearTwo)}")

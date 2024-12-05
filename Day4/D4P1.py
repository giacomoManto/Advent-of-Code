inputfile = "Day4/input.txt"

crossword = []

exes = []

with open(inputfile, "r") as input:
    y = 0
    for line in input.readlines():
        crossword.append(line.removesuffix("\n"))
        x = 0
        for char in line:
            if char == "X":
                exes.append((x, y))
            x += 1
        y += 1

count = 0
for x, y in exes:
    # safety Checks
    right = (x + 3) < len(crossword[y])
    left = (x - 3) >= 0
    up = (y - 3) >= 0
    down = (y + 3) < len(crossword)

    if up and crossword[y - 1][x] + crossword[y - 2][x] + crossword[y - 3][x] == "MAS":
        count += 1
    if (
        right
        and crossword[y][x + 1] + crossword[y][x + 2] + crossword[y][x + 3] == "MAS"
    ):
        count += 1
    if (
        right
        and down
        and crossword[y + 1][x + 1] + crossword[y + 2][x + 2] + crossword[y + 3][x + 3]
        == "MAS"
    ):
        count += 1
    if (
        right
        and up
        and crossword[y - 1][x + 1] + crossword[y - 2][x + 2] + crossword[y - 3][x + 3]
        == "MAS"
    ):
        count += 1
    if (
        down
        and crossword[y + 1][x] + crossword[y + 2][x] + crossword[y + 3][x] == "MAS"
    ):
        count += 1
    if (
        left
        and crossword[y][x - 1] + crossword[y][x - 2] + crossword[y][x - 3] == "MAS"
    ):
        count += 1
    if (
        left
        and down
        and crossword[y + 1][x - 1] + crossword[y + 2][x - 2] + crossword[y + 3][x - 3]
        == "MAS"
    ):
        count += 1
    if (
        left
        and up
        and crossword[y - 1][x - 1] + crossword[y - 2][x - 2] + crossword[y - 3][x - 3]
        == "MAS"
    ):
        count += 1

print(count)

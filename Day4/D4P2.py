inputfile = "Day4/input.txt"

crossword = []

aes = []

with open(inputfile, "r") as input:
    y = 0
    for line in input.readlines():
        crossword.append(line.removesuffix("\n"))
        x = 0
        for char in line:
            if char == "A":
                aes.append((x, y))
            x += 1
        y += 1

init = set()
count = 0
for x, y in aes:
    # safety Checks
    right = (x + 1) < len(crossword[y])
    left = (x - 1) >= 0
    up = (y - 1) >= 0
    down = (y + 1) < len(crossword)

    if not (right and left and up and down):
        continue

    if (
        crossword[y - 1][x - 1] + crossword[y][x] + crossword[y + 1][x + 1] != "MAS"
        and crossword[y + 1][x + 1] + crossword[y][x] + crossword[y - 1][x - 1] != "MAS"
    ):
        continue

    if (
        crossword[y - 1][x + 1] + crossword[y][x] + crossword[y + 1][x - 1] != "MAS"
        and crossword[y + 1][x - 1] + crossword[y][x] + crossword[y - 1][x + 1] != "MAS"
    ):
        continue

    count += 1

print(count)

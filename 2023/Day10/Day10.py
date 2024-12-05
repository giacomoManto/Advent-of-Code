input = open("input.txt", "r").readlines()
pipes = []
start = None
for line in input:
    lineOpipes = []
    for char in line:
        lineOpipes.append(char)
        if char == "S":
            start = (input.index(line), line.index(char))
    pipes.append(lineOpipes)


def getTile(pos):
    try:
        return pipes[pos[0]][pos[1]]
    except IndexError:
        print("FAILED")
        return None


seen = []


def getNextTile(curPos, nextPos):
    if (curPos, nextPos) in seen:
        print("LOOPING")
        return "S"
    else:
        seen.append((curPos, nextPos))

    nextTile = getTile(nextPos)
    nextNextPos = None
    if nextPos[0] > curPos[0]:
        if nextTile == "|":
            nextNextPos = (nextPos[0] + 1, nextPos[1])
        elif nextTile == "L":
            nextNextPos = (nextPos[0], nextPos[1] + 1)
        elif nextTile == "J":
            nextNextPos = (nextPos[0], nextPos[1] - 1)
    elif nextPos[0] < curPos[0]:
        if nextTile == "|":
            nextNextPos = (nextPos[0] - 1, nextPos[1])
        elif nextTile == "F":
            nextNextPos = (nextPos[0], nextPos[1] + 1)
        elif nextTile == "7":
            nextNextPos = (nextPos[0], nextPos[1] - 1)
    elif nextPos[1] > curPos[1]:
        if nextTile == "-":
            nextNextPos = (nextPos[0], nextPos[1] + 1)
        elif nextTile == "J":
            nextNextPos = (nextPos[0] - 1, nextPos[1])
        elif nextTile == "7":
            nextNextPos = (nextPos[0] + 1, nextPos[1])
    elif nextPos[1] < curPos[1]:
        if nextTile == "-":
            nextNextPos = (nextPos[0], nextPos[1] - 1)
        elif nextTile == "L":
            nextNextPos = (nextPos[0] - 1, nextPos[1])
        elif nextTile == "F":
            nextNextPos = (nextPos[0] + 1, nextPos[1])
    return nextNextPos


north = getTile((start[0] - 1, start[1]))
south = getTile((start[0] + 1, start[1]))
east = getTile((start[0], start[1] + 1))
west = getTile((start[0], start[1] - 1))

cur = start
next = None
if north in ["|", "7", "F"]:
    print("NORTH")
    next = (start[0] - 1, start[1])
elif south in ["|", "L", "J"]:
    print("SOUTH")
    next = (start[0] + 1, start[1])
elif east in ["-", "J", "7"]:
    print("EAST")
    next = (start[0], start[1] + 1)
elif west in ["-", "F", "L"]:
    print("WEST")
    next = (start[0], start[1] - 1)

path = []
path.append(start)
while getTile(next) != "S":
    path.append(next)
    temp = getNextTile(cur, next)
    cur = next
    next = temp

print(len(path) / 2)


def raycast(pos):
    count = 0
    x = pos[0] + 1
    y = pos[1] + 1
    while x < len(pipes) and y < len(pipes[x]):
        if (x, y) in path:
            if getTile((x, y)) == "L" or getTile((x, y)) == "7":
                count += 1
            count += 1
        y += 1
        x += 1
    return count


inLoop = []
outLoop = []

x = 0
while x < len(pipes):
    # print("X: %d" % x)
    y = 0
    while y < len(pipes[x]):
        # if (x, y) not in inLoop and (x, y) not in outLoop:
        if (x, y) not in path:
            if raycast((x, y)) % 2 == 0:
                outLoop.append((x, y))
            else:
                inLoop.append((x, y))
        y += 1
    x += 1

print(len(inLoop) + len(outLoop) + len(path))
print(len(inLoop))
print(len(pipes) * len(pipes[0]))

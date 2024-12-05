input = open("input.txt", "r")
data = []

for line in input.readlines():
    levels = []
    levels.append([int(x) for x in line.removesuffix("\n").split(" ")])
    curLevel = levels[0]
    while curLevel.count(0) != len(curLevel):
        nextLevel = []
        index = 0
        while index < (len(curLevel) - 1):
            nextLevel.append(curLevel[index + 1] - curLevel[index])
            index += 1
        levels.append(nextLevel)
        curLevel = nextLevel
    data.append(levels)

sum = 0
for line in data:
    line.reverse()
    change = 0
    for level in line[1:]:
        change = level[0] - change
    sum += change

print(sum)

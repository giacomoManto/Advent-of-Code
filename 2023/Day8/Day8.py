import sys


def findLCM(stepsList1):
    stepsList = stepsList1.copy()

    if len(stepsList) == 2:
        while stepsList.count(stepsList[0]) != len(stepsList):
            min = sys.maxsize
            for step in stepsList:
                if step < min:
                    min = step

            stepsList[stepsList.index(min)] += stepsList1[stepsList.index(min)]

        return stepsList[0]
    else:
        newStep = stepsList[2:]
        newStep.append(findLCM(stepsList[0:2]))
        return findLCM(newStep)


input = open("input.txt", "r")
input = input.readlines()
directions = input[0].split()[0]
map = {}
curNodes = []
for node in input[2:]:
    split = node.split(" = ")
    map[split[0]] = split[1].removeprefix("(").removesuffix(")\n").split(", ")
    if split[0][2] == "A":
        curNodes.append(split[0])

stepsList = []
for node in curNodes:
    curNode = node
    steps = 0
    while curNode[2] != "Z":
        for direction in directions:
            steps += 1
            if direction == "L":
                curNode = map[curNode][0]
            elif direction == "R":
                curNode = map[curNode][1]
            if curNode[2] == "Z":
                break
        print("Steps %d" % steps)
    stepsList.append(steps)

print(stepsList)
print(findLCM(stepsList))

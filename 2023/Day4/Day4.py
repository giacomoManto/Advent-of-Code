import time


def day4p1():
    input = open("input.txt", "r")
    sum = 0
    for line in input.readlines():
        matches = 0
        winning = line.split(":")[1].split("|")[0].split(" ")
        yours = line.split(":")[1].split("|")[1].removesuffix("\n").split(" ")
        for auto in yours:
            try:
                int(auto)
                if auto in winning:
                    matches += 1
            except TypeError:
                continue
        if matches > 0:
            sum += 2 ** (matches - 1)
    input.close()
    return sum


def day4p2():
    input = open("input.txt", "r")
    lines = []
    sum = 0
    for line in input.readlines():
        winning = line.split(":")[1].split("|")[0].split(" ")
        yours = line.split(":")[1].split("|")[1].removesuffix("\n").split(" ")
        lines.append((winning, yours))
    input.close()

    for lineNum in range(0, len(lines)):
        sum += calculateCopies(lines, lineNum)

    return sum


lookupTable = {}
lookup2Table = {}


def calculateCopies(lines, lineNum):
    if lineNum in lookup2Table:
        return lookup2Table[lineNum]
    sum = 1
    matches = 0
    if lineNum in lookupTable:
        matches = lookupTable[lineNum]
    else:
        for auto in lines[lineNum][1]:
            try:
                int(auto)
                if auto in lines[lineNum][0]:
                    matches += 1
            except TypeError:
                continue
        lookupTable[lineNum] = matches

    for newNum in range(lineNum + 1, lineNum + matches + 1):
        sum += calculateCopies(lines, newNum)

    lookup2Table[lineNum] = sum
    return sum


if __name__ == "__main__":
    startTime = time.time()
    p1 = day4p1()
    p1Time = time.time()
    p2 = day4p2()
    p2Time = time.time()
    print("P1: %s, Time: %f" % (p1, (p1Time - startTime)))
    print("P1: %s, Time: %f" % (p2, (p2Time - p1Time)))

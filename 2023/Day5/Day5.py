import time
import sys


def day5p1():
    start = time.time()
    input = open("input.txt", "r")
    lines = input.readlines()
    input.close()
    seeds = lines[0].split(":")[1].removesuffix("\n").split(" ")

    mapList = []

    curMap = []
    for line in lines[3:]:
        if "map" in line:
            mapList.append(curMap.copy())
            curMap.clear()
        elif len(line.removesuffix("\n").split(" ")) == 3:
            nums = line.removesuffix("\n").split(" ")
            curMap.append(
                (
                    range(int(nums[1]), int(nums[1]) + int(nums[2])),
                    range(int(nums[0]), int(nums[0]) + int(nums[2])),
                )
            )

    mapList.append(curMap)
    minimum = sys.maxsize
    for seed in seeds:
        minimum = min(minimum, moveDown(seed, mapList))

    print("P1: %d, Time: %f" % (minimum, time.time() - start))


def day5p2():
    time.time()

    input = open("input2.txt", "r")
    lines = input.readlines()
    input.close()
    seeds = lines[0].split(":")[1].removesuffix("\n").split(" ")
    seedRange = []
    for pos in range(1, len(seeds), 2):
        seedRange.append((int(seeds[pos]), int(seeds[pos + 1])))

    mapList = []

    curMap = []
    for line in lines[3:]:
        if "map" in line:
            mapList.append(curMap.copy())
            curMap.clear()
        elif len(line.removesuffix("\n").split(" ")) == 3:
            nums = line.removesuffix("\n").split(" ")
            curMap.append((int(nums[1]), int(nums[0]), int(nums[2])))

    mapList.append(curMap)
    # print(mapList)
    curRow = 0
    print(seedRange)
    toBeProcessed = []
    toBeProcessed.extend(seedRange.copy())
    print(toBeProcessed)
    while curRow < len(mapList):
        print(curRow)
        processed = []
        while len(toBeProcessed) > 0:
            # print("Row: %d, processed: %d, processedLeft: %d" % (curRow, len(processed), len(toBeProcessed)))
            curProccessing = toBeProcessed.pop()
            split = False
            for mapping in mapList[curRow]:
                if curProccessing[0] >= mapping[0] and curProccessing[0] < (
                    mapping[0] + mapping[2]
                ):
                    processed.append((mapping[1], min(curProccessing[1], mapping[2])))
                    toBeProcessed.append(
                        (
                            curProccessing[0] + min(curProccessing[1], mapping[2]),
                            curProccessing[0] + curProccessing[1],
                        )
                    )
                    split = True
                    break
                elif mapping[0] >= curProccessing[0] and mapping[0] < (
                    curProccessing[0] + curProccessing[1]
                ):
                    if (curProccessing[0] + curProccessing[1]) > (
                        mapping[0] + mapping[2]
                    ):
                        processed.append((mapping[1], mapping[2]))
                        toBeProcessed.append(
                            (curProccessing[0], mapping[0] - curProccessing[0])
                        )
                        toBeProcessed.append(
                            (
                                mapping[0] + mapping[2],
                                (curProccessing[0] + curProccessing[1])
                                - (mapping[0] + mapping[2]),
                            )
                        )
                        split = True
                        break
                    else:
                        processed.append(
                            (
                                mapping[1],
                                curProccessing[0] + curProccessing[1] - mapping[0],
                            )
                        )
                        toBeProcessed.append(
                            (curProccessing[0], mapping[0] - curProccessing[0])
                        )
                        split = True
                        break
            if not split:
                processed.append(curProccessing)
        toBeProcessed = cleanUp(list(set(processed.copy())))
        curRow += 1
        print(toBeProcessed)


def cleanUp(ranges):
    r1 = 0
    nr = ranges.copy()
    while r1 < len(nr) - 1:
        nr1 = nr[r1]
        r2 = r1 + 1
        while r2 < len(nr):
            nr2 = nr[r2]
            if nr2[0] >= nr1[0] and nr2[0] < (nr1[0] + nr1[1]):
                if (nr2[0] + nr2[1]) <= (nr1[0] + nr1[1]):
                    nr[r2] = (0, 0)
                else:
                    nr[r1] = (nr1[0], nr1[1] + nr2[1])
                    nr[r2] = (0, 0)
            elif nr1[0] >= nr2[0] and nr1[0] < (nr2[0] + nr2[1]):
                if (nr1[0] + nr1[1]) <= (nr2[0] + nr2[1]):
                    nr[r1] = nr2
                    nr[r2] = (0, 0)
                else:
                    nr[r1] = (nr2[0], nr1[1] + nr2[1])
                    nr[r2] = (0, 0)
            r2 += 1
        r1 += 1
    r1 = 0
    while (0, 0) in nr:
        nr.remove((0, 0))
    return nr


def moveDown(seed, mapList):
    try:
        curSeed = int(seed)
    except ValueError:
        return sys.maxsize

    for step in mapList:
        for pot in step:
            if curSeed in pot[0]:
                curSeed = pot[1][pot[0].index(curSeed)]
                break
    return curSeed


if __name__ == "__main__":
    day5p1()
    day5p2()

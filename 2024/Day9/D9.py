inputfile = "2024/Day9/input.txt"


with open(inputfile, "r") as input:
    data = input.read()
    data.removesuffix("\n")
    pos = 1
    ID = 0
    expandedData = []
    for char in data:
        if pos % 2 == 0:
            expandedData.extend(["."] * int(char))
        else:
            expandedData.extend([str(ID)] * int(char))
            ID += 1
        pos += 1


lPointer = 0
rPointer = len(expandedData) - 1


checkSumP1 = 0
while lPointer <= rPointer:
    if expandedData[lPointer] == ".":
        while expandedData[rPointer] == ".":
            rPointer -= 1

        checkSumP1 += lPointer * int(expandedData[rPointer])

        # print(f"R {lPointer} * {expandedData[rPointer]}")
        rPointer -= 1
    else:
        checkSumP1 += lPointer * int(expandedData[lPointer])
        # print(f"L {lPointer} * {expandedData[lPointer]}")
    lPointer += 1


print(f"Part one: {checkSumP1}")

lPointer = 0
rPointer = len(expandedData) - 1

emptySpace = {}
# Find and categorize empty space
while lPointer <= rPointer:
    sIndex = None
    while lPointer <= rPointer and expandedData[lPointer] == ".":
        if sIndex is None:
            sIndex = lPointer
        lPointer += 1
    if sIndex is not None:
        emptySpace[sIndex] = lPointer - sIndex
    lPointer += 1

keys = list(emptySpace.keys())
keys.sort()

checkSumP2 = 0
dataSize = 0
prev = expandedData[rPointer]
while 0 <= rPointer:
    if expandedData[rPointer] == prev:
        dataSize += 1
    else:
        dataSize = 1

    if (
        rPointer > 0 and expandedData[rPointer - 1] != expandedData[rPointer]
    ) or rPointer == 0:  # If we are at the edge of this data
        if expandedData[rPointer] != ".":
            found = False
            dataSpot = range(0)
            for key in keys:
                if emptySpace[key] >= dataSize:
                    emptySpace[key + dataSize] = emptySpace[key] - dataSize
                    emptySpace[key] = 0
                    keys.remove(key)
                    keys.append(key + dataSize)
                    keys.sort()
                    dataSpot = range(key, key + dataSize)
                    found = True
                    break

            if not found:
                dataSpot = range(rPointer, rPointer + dataSize)
            for p in dataSpot:
                checkSumP2 += p * int(expandedData[rPointer])
    prev = expandedData[rPointer]
    rPointer -= 1


print(f"Part two: {checkSumP2}")

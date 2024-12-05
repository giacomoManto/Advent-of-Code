inputfile = "2024/Day1/sample.txt"

leftMap = {}
rightMap = {}

with open(inputfile, "r") as input:
    for line in input.readlines():
        leftNum = int(line.split("   ")[0])
        if leftNum in leftMap:
            leftMap[leftNum] += 1
        else:
            leftMap[leftNum] = 1

        rightNum = int(line.split("   ")[1].removesuffix("\n"))
        if rightNum in rightMap:
            rightMap[rightNum] += 1
        else:
            rightMap[rightNum] = 1


total = 0
for left in leftMap.keys():
    total += leftMap[left] * rightMap.get(left, 0) * left

print(total)

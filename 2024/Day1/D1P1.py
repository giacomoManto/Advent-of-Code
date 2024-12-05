import bisect

inputfile = "2024/Day1/sample.txt"

leftList = []
rightList = []

with open(inputfile, "r") as input:
    for line in input.readlines():
        leftNum = int(line.split("   ")[0])
        lindex = bisect.bisect_left(leftList, leftNum)
        leftList.insert(lindex, leftNum)

        rightNum = int(line.split("   ")[1].removesuffix("\n"))
        rindex = bisect.bisect_left(rightList, rightNum)
        rightList.insert(rindex, rightNum)


total = 0

for left, right in zip(leftList, rightList):
    total += abs(left - right)

print(total)

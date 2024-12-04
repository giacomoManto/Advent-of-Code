import bisect

inputfile = "Day1\input.txt"

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

for l, r in zip(leftList, rightList):
    total += abs(l - r)

print(total)

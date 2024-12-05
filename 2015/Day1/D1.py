inputfile = "2015/Day1/input.txt"

with open(inputfile, "r") as input:
    data = input.read().removesuffix("\n")


runningTally = 0
pos = 1
for char in data:
    if char == "(":
        runningTally += 1
    elif char == ")":
        runningTally -= 1
    if runningTally < 0:
        print(pos)
        break
    pos += 1

print(f"Part one: {data.count("(") - data.count(")")}")
print(f"Part two: {pos}")

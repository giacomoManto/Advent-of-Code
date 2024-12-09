inputfile = "2024/Day7/input.txt"


def collapse(input) -> list:
    if len(input) <= 1:
        return input
    add = [input[0] + input[1]] + input[2:]
    mult = [input[0] * input[1]] + input[2:]
    concat = [int(str(input[0]) + str(input[1]))] + input[2:]
    return collapse(add) + collapse(mult) + collapse(concat)


count = 0
with open(inputfile, "r") as input:
    data = input.read()
    for line in data.splitlines():
        testVal = int(line.split(":")[0])
        otherVals = [int(val) for val in line.split(":")[1].strip().split(" ")]
        if testVal in collapse(otherVals):
            count += testVal
print(count)

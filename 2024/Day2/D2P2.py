inputfile = "2024/Day2/sample.txt"


def safetyCheck(line: list) -> int:
    increasing = None
    for index in range(len(line)):
        if index == 0:
            increasing = line[index + 1] > line[index]
            continue
        if increasing:
            if line[index - 1] >= line[index]:
                return index
        else:
            if line[index - 1] <= line[index]:
                return index
        if abs(line[index - 1] - line[index]) > 3:
            return index
    return -1


safe = 0

with open(inputfile, "r") as input:
    for line in input.readlines():
        line = line.removesuffix("\n").split(" ")
        line = [int(a) for a in line]
        fail = safetyCheck(line)
        if fail != -1:
            l0 = line.copy()
            l0.pop(0)
            l1 = line.copy()
            l1.pop(fail)
            l2 = line.copy()
            l2.pop(fail - 1)
            if safetyCheck(l1) == -1 or safetyCheck(l2) == -1 or safetyCheck(l0) == -1:
                safe += 1
        else:
            safe += 1

print(safe)

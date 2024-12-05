inputfile = "2024/Day2/sample.txt"

safe = 0

with open(inputfile, "r") as input:
    for line in input.readlines():
        line = line.removesuffix("\n").split(" ")
        line = [int(a) for a in line]
        increasing = None
        safeLine = True
        for level in range(len(line)):
            if level == 0:
                increasing = line[level + 1] > line[level]
                continue
            if increasing:
                if line[level - 1] >= line[level]:
                    safeLine = False
                    break
            else:
                if line[level - 1] <= line[level]:
                    safeLine = False
                    break
            if abs(line[level - 1] - line[level]) > 3:
                safeLine = False
                break
        if safeLine:
            safe += 1

print(safe)

import re

inputfile = "2024/Day3/sample.txt"

expression = re.compile(r"mul\((\d{1,3},\d{1,3})\)")
sum = 0
with open(inputfile, "r") as input:
    for match in expression.finditer(input.read()):
        left, right = [int(a) for a in match.groups()[0].split(",")]
        sum += left * right
        pass
print(sum)

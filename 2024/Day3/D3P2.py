import re

inputfile = "2024/Day3/sample.txt"

expression = re.compile(r"mul\((\d{1,3},\d{1,3})\)|(do\(\))|(don't\(\))")
sum = 0
do = True
with open(inputfile, "r") as input:
    for match in expression.finditer(input.read()):
        if match.groups()[2] == "don't()":
            do = False
        elif match.groups()[1] == "do()":
            do = True
        elif do:
            left, right = [int(a) for a in match.groups()[0].split(",")]
            sum += left * right

print(sum)

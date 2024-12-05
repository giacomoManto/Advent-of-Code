inputfile = "Day5/input.txt"


def processOneLine(line, rules) -> int:
    seen = []
    for num in line:
        if num in rules:
            for after in rules[num]:
                if after in seen:
                    return 0
        seen.append(num)
    return line[int((len(line) - 1) / 2)]


with open(inputfile, "r") as input:
    por, updates = input.read().split("\n\n")

    # Process page ordering rules
    rpor = {}
    for a in por.splitlines():
        before = int(a.split("|")[0])
        after = int(a.split("|")[1])
        if before not in rpor:
            rpor[before] = set()
        rpor[before].add(after)
    por = rpor

    # Process updates
    rupdates = []
    for line in updates.splitlines():
        intline = []
        for num in line.split(","):
            intline.append(int(num))
        rupdates.append(intline)
    updates = rupdates
sum = 0

for line in updates:
    sum += processOneLine(line, por)
print(sum)

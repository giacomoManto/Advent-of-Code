inputfile = "Day5/input.txt"


class Rule:
    def __init__(self, number: int):
        self.number = number
        self.lesser = set()
        self.greater = set()

    def addLesserNum(self, lesser: int):
        self.lesser.add(lesser)

    def addGreaterNum(self, greater: int):
        self.greater.add(greater)

    def __lt__(self, other):
        return other.number in self.greater

    def __le__(self, other):
        return other.number in self.greater and other.number not in self.lesser

    def __gt__(self, other):
        return other.number in self.lesser

    def __ge__(self, other):
        return other.number in self.lesser and other.number not in self.greater

    def __eq__(self, other):
        return other.number not in self.lesser and other.number not in self.greater

    def __ne__(self, other):
        return other.number in self.greater or other.number in self.lesser


class RuleBook:
    def __init__(self):
        self.rules = {}

    def addRule(self, lesser: int, greater: int):
        if lesser not in self.rules:
            self.rules[lesser] = Rule(lesser)
        if greater not in self.rules:
            self.rules[greater] = Rule(greater)

        self.rules[lesser].addGreaterNum(greater)
        self.rules[greater].addLesserNum(lesser)

    def getRule(self, number):
        if number not in self.rules:
            self.rules[number] = Rule(number)
        return self.rules[number]


def processOneLine(line, rules: RuleBook) -> int:
    realLine = [rules.getRule(a) for a in line]
    if sorted(realLine) != realLine:
        return sorted(realLine)[int((len(realLine) - 1) / 2)].number
    else:
        return 0


with open(inputfile, "r") as input:
    por, updates = input.read().split("\n\n")
    rules = RuleBook()
    # Process page ordering rules
    rpor = {}
    for a in por.splitlines():
        before = int(a.split("|")[0])
        after = int(a.split("|")[1])
        rules.addRule(before, after)

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
    sum += processOneLine(line, rules)
print(sum)

vowels = set("aeiou")
# One letter twice in a row
banned = set(["ab", "cd", "pq", "xy"])

inputfile = "2015/Day5/input.txt"

with open(inputfile, "r") as input:
    data = input.read().splitlines()

niceStrings = 0

for line in data:
    good = False
    vc = 0
    for char in range(len(line)):
        if line[char] in vowels:
            vc += 1
        if char == 0:
            continue
        if line[char - 1] + line[char] in banned:
            good = False
            break
        if line[char - 1] == line[char]:
            good = True
    if good and vc >= 3:
        niceStrings += 1

print(f"Part one: {niceStrings}")

# Pair appears twice with no overlap e.g "xyxy" valid but "aaa" not
# One letter that repeats with one letter between
goodLines = 0
for line in data:
    potentialPairs = {}
    twoPair = False
    repeatedLetter = False
    for char in range(1, len(line)):
        pair = line[char - 1] + line[char]
        if pair not in potentialPairs:
            potentialPairs[pair] = set([char, char - 1])
        else:
            if (
                char not in potentialPairs[pair]
                and char - 1 not in potentialPairs[pair]
            ):
                twoPair = True
                if repeatedLetter:
                    break

        if char >= 2:
            if line[char - 2] == line[char]:
                repeatedLetter = True
                if twoPair:
                    break
    if repeatedLetter and twoPair:
        goodLines += 1
print(f"Part two: {goodLines}")

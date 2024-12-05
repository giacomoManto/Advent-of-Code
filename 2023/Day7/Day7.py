from functools import cmp_to_key
import time


FIVE = 0
FOUR = 1
FULL = 2
THREE = 3
TWO = 4
ONE = 5
HIGH = 6

cardValue = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}


def getCardValue(card):
    if card in cardValue:
        return cardValue.get(card)
    else:
        return int(card)


def handType(hand):
    unique = [*hand[0]].copy()
    seen = []
    nums = []
    for card in unique:
        if card in seen:
            continue
        else:
            nums.append(unique.count(card))
            seen.append(card)
    nums.sort(reverse=True)

    # part 2 shenanigans
    if cardValue["J"] == 1:
        if "J" in unique:
            jcount = unique.count("J")
            if jcount != 5:
                nums.remove(jcount)
                nums[0] += jcount

    if 5 in nums:
        return FIVE
    elif 4 in nums:
        return FOUR
    elif 3 in nums:
        if 2 in nums:
            return FULL
        else:
            return THREE
    else:
        pairs = nums.count(2)
        if pairs == 2:
            return TWO
        elif pairs == 1:
            return ONE
        else:
            return HIGH


def compare(hand1, hand2):
    if handType(hand1) < handType(hand2):
        return -1
    elif handType(hand2) < handType(hand1):
        return 1
    else:
        h1index = 0
        h2index = 0
        while h1index < len(hand1[0]):
            if hand1[0][h1index] == hand2[0][h2index]:
                h1index += 1
                h2index += 1
                continue
            else:
                return getCardValue(hand2[0][h2index]) - getCardValue(hand1[0][h1index])
        return 0


f = open("input.txt", "r")
data = []
for line in f.read().splitlines():
    data.append(line.split())

# part 1
start = time.time()
data1 = sorted(data, key=cmp_to_key(compare))

index = len(data1)
sum = 0
for entry in data1:
    sum += int(entry[1]) * index
    index -= 1
print("Part 1 answer: %d" % sum)
print("Found in %f seconds" % (time.time() - start))

# part 2
cardValue["J"] = 1
start = time.time()
data2 = sorted(data, key=cmp_to_key(compare))

index = len(data2)
sum = 0
for entry in data2:
    sum += int(entry[1]) * index
    index -= 1
print("Part 2 answer: %d" % sum)
print("Found in %f seconds" % (time.time() - start))

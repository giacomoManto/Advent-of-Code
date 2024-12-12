import functools

inputFile = "2024/Day11/input.txt"


with open(inputFile, "r") as input:
    data = [int(a) for a in input.read().removesuffix("\n").split(" ")]


@functools.cache
def blinkStone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stoneString = str(stone)
        firstPart, secondPart = (
            stoneString[: len(stoneString) // 2],
            stoneString[len(stoneString) // 2 :],
        )
        return int(firstPart), int(secondPart)
    else:
        return [stone * 2024]


@functools.cache
def blink(stone, steps):
    if steps == 0:
        return 1

    blinked = blinkStone(stone)
    return sum([blink(a, steps - 1) for a in blinked])


p1 = sum([blink(a, 25) for a in data])
p2 = sum([blink(a, 75) for a in data])

print(f"Part one: {p1}")
print(f"Part two: {p2}")

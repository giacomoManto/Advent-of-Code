input = [(47, 400), (98, 1213), (66, 1011), (98, 1540)]


def day6p1():
    total = 1
    for race in input:
        raceTotal = 0
        for timePressed in range(1, race[0] + 1):
            if canWin(timePressed, race[0], race[1]):
                raceTotal += 1
        if raceTotal > 0:
            total = total * raceTotal
    print(total)


def canWin(timePressed, totalTime, distance):
    return (totalTime - timePressed) * timePressed >= distance


input2 = (47986698, 400121310111540)


def day6p2():
    raceTotal = 0
    for timePressed in range(1, input2[0] + 1):
        if canWin(timePressed, input2[0], input2[1]):
            raceTotal += 1
    print(raceTotal)


# 1/ms^2

if __name__ == "__main__":
    day6p2()

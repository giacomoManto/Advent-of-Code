MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def day2p1():
    input = open("input.txt", "r")
    sum = 0
    for round in input.readlines():
        gameNum = int(round.split(":")[0].split(" ")[1])
        colors = round.split(":")[1].split(" ")
        valid = True
        for i in range(0, len(colors)):
            if "red" in colors[i]:
                valid = valid and int(colors[i - 1]) <= MAX_RED
            elif "green" in colors[i]:
                valid = valid and int(colors[i - 1]) <= MAX_GREEN
            elif "blue" in colors[i]:
                valid = valid and int(colors[i - 1]) <= MAX_BLUE
        if valid:
            sum += gameNum
    input.close()
    return sum


def day2p2():
    input = open("input.txt", "r")
    sum = 0
    for round in input.readlines():
        int(round.split(":")[0].split(" ")[1])
        colors = round.split(":")[1].split(" ")
        maxRed = 0
        maxGreen = 0
        maxBlue = 0

        for i in range(0, len(colors)):
            if "red" in colors[i]:
                maxRed = max(int(colors[i - 1]), maxRed)
            elif "green" in colors[i]:
                maxGreen = max(int(colors[i - 1]), maxGreen)
            elif "blue" in colors[i]:
                maxBlue = max(int(colors[i - 1]), maxBlue)

        sum += maxRed * maxBlue * maxGreen
    input.close()
    return sum


if __name__ == "__main__":
    print(day2p2())

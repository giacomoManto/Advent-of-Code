# 48 - 57 inclusive


def day3p1():
    input = open("input.txt", "r")
    symbols = []
    for line in input.readlines():
        symbols.append([*line])
    input.close()
    fsum = 0

    def prune(localLine, localChar):
        line = symbols[localLine]
        prunedNum = []
        localSum = 0
        for char in range(0, len(line)):
            if ord(line[char]) >= 48 and ord(line[char]) <= 57:
                prunedNum.append(char)
            elif char < localChar:
                prunedNum.clear()
            else:
                final = []
                for pos in prunedNum:
                    final.append(line[pos])
                    symbols[localLine][pos] = "."
                localSum += int("".join(final))
                break

        return localSum

    for line in range(0, len(symbols)):
        for char in range(0, len(symbols[line])):
            if symbols[line][char] == ".":
                continue
            elif (
                ord(symbols[line][char]) < 48 or ord(symbols[line][char]) > 57
            ) and ord(symbols[line][char]) != 10:
                lineRange = range(max(0, line - 1), min(line + 2, len(symbols)))
                charRange = range(max(0, char - 1), min(char + 2, len(symbols[line])))
                for localLine in lineRange:
                    for localChar in charRange:
                        if (
                            ord(symbols[localLine][localChar]) >= 48
                            and ord(symbols[localLine][localChar]) <= 57
                        ):
                            fsum += prune(localLine, localChar)
    return fsum


def day3p2():
    input = open("input.txt", "r")
    symbols = []
    for line in input.readlines():
        symbols.append([*line])
    input.close()
    fsum = 0

    def prune(localLine, localChar):
        line = symbols[localLine]
        prunedNum = []
        for char in range(0, len(line)):
            if ord(line[char]) >= 48 and ord(line[char]) <= 57:
                prunedNum.append(char)
            elif char < localChar:
                prunedNum.clear()
            else:
                final = []
                for pos in prunedNum:
                    final.append(line[pos])
                    symbols[localLine][pos] = "."
                return int("".join(final))

    for line in range(0, len(symbols)):
        for char in range(0, len(symbols[line])):
            if symbols[line][char] == ".":
                continue
            elif ord(symbols[line][char]) == 42:
                lineRange = range(max(0, line - 1), min(line + 2, len(symbols)))
                charRange = range(max(0, char - 1), min(char + 2, len(symbols[line])))
                nearbyParts = []
                for localLine in lineRange:
                    for localChar in charRange:
                        if (
                            ord(symbols[localLine][localChar]) >= 48
                            and ord(symbols[localLine][localChar]) <= 57
                        ):
                            nearbyParts.append(prune(localLine, localChar))
                if len(nearbyParts) == 2:
                    fsum += nearbyParts[0] * nearbyParts[1]
    return fsum


if __name__ == "__main__":
    print(day3p1())
    print(day3p2())

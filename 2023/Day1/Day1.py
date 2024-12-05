spellings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
lookup = dict(zip(spellings, values))


def day1():
    input = open("input.txt", "r")
    sum = 0
    for line in input.readlines():
        list = strToList(line)
        sum += int("%s%s" % (list[0], list[-1]))
    print(sum)
    input.close()


def strToList(line):
    values = []
    start = 0
    stop = 3
    while start < len(line):
        try:
            int(line[start])
            values.append(line[start])
            start += 1
            stop = start + 3
            continue
        except ValueError:
            if line[start:stop] in spellings:
                values.append(lookup[line[start:stop]])
                start = stop
                stop = start + 3
                continue
            elif stop < len(line):
                stop += 1
                continue
            else:
                start += 1
                stop = start + 3
                continue
    return values


if __name__ == "__main__":
    day1()

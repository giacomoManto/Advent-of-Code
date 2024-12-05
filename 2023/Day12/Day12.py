import time

springs: list[list[str]] = []  # stored as [row][column]
records: list[list[int]] = []
for line in open("input.txt", "r").readlines():
    lineParts = line.removesuffix("\n").split(" ")

    recordLine: list[int] = []
    for value in lineParts[1].split(","):
        recordLine.append(int(value))
    records.append(recordLine)

    row: list[str] = []
    for char in lineParts[0]:
        row.append(char)
    springs.append(row)

memory = {}


def solveRowCombinations(springRow: list[str], recordRow: list[int]) -> int:
    if ("".join(springRow) + ",".join(str(x) for x in recordRow)) in memory:
        return memory[("".join(springRow) + ",".join(str(x) for x in recordRow))]

    if len(springRow) == 0:
        if len(recordRow) == 0:
            memory[("".join(springRow) + ",".join(str(x) for x in recordRow))] = 1
            return 1
        else:
            memory[("".join(springRow) + ",".join(str(x) for x in recordRow))] = 0
            return 0

    if len(recordRow) == 0:
        if "#" in springRow:
            return 0
        else:
            return 1

    if springRow[0] == ".":
        answer = solveRowCombinations(springRow[1:], recordRow)
        memory[("".join(springRow) + ",".join(str(x) for x in recordRow))] = answer
        return answer
    elif springRow[0] == "?":
        next = ["#"]
        next.extend(springRow[1:])

        answer = solveRowCombinations(springRow[1:], recordRow) + solveRowCombinations(
            next, recordRow
        )
        memory[("".join(springRow) + ",".join(str(x) for x in recordRow))] = answer
        return answer
    elif springRow[0] == "#":
        if len(springRow) < recordRow[0]:
            return 0

        for index in range(recordRow[0]):
            if springRow[index] == ".":
                return 0

        try:
            if springRow[recordRow[0]] == "#":
                return 0
            else:
                answer = solveRowCombinations(
                    springRow[recordRow[0] + 1 :], recordRow[1:]
                )
                memory[("".join(springRow) + ",".join(str(x) for x in recordRow))] = (
                    answer
                )
                return answer
        except IndexError:
            answer = solveRowCombinations([], recordRow[1:])
            memory[("".join(springRow) + ",".join(str(x) for x in recordRow))] = answer
            return answer


start = time.time()
sum = 0
for spring, record in zip(springs, records):
    sum += solveRowCombinations(spring, record)
print(time.time() - start)
print(sum)
springs2 = []
records2 = []
for index in range(len(springs)):
    newSpring = springs[index].copy()
    newRecord = records[index].copy()

    for i in range(4):
        newSpring.extend(["?"])
        newSpring.extend(springs[index])

        newRecord.extend(records[index])

    springs2.append(newSpring)
    records2.append(newRecord)

start = time.time()
sum = 0
for spring, record in zip(springs2, records2):
    sum += solveRowCombinations(spring, record)
print(time.time() - start)
print(sum)

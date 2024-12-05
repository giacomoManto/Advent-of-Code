import hashlib

puzzleinput = "bgvyzdsv"


def encode(suffix="") -> str:
    result = hashlib.md5(bytes(f"{puzzleinput}{suffix}", "utf8"))
    return result.hexdigest()


partOne = 0
partTwo = 0
num = 0
while True:
    encoded = encode(str(num))
    if partOne == 0 and encoded[:5] == "00000":
        partOne = num
    if encoded[:6] == "000000":
        partTwo = num
        break
    print(f"{num} | {encoded}")
    num += 1

print(f"Part one: {partOne} | {encode(str(partOne))}")
print(f"Part two: {partTwo} | {encode(str(partTwo))}")

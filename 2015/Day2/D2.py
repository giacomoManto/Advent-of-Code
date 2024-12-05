inputfile = "2015/Day2/input.txt"

with open(inputfile, "r") as input:
    data = input.read().splitlines()
    boxes = [(split.split("x")) for split in data]
    boxes = [(int(length), int(width), int(height)) for length, width, height in boxes]

wrappingPaper = 0
ribbon = 0
for box in boxes:
    length, width, height = box
    wrappingPaper += 2 * (length * width + width * height + height * length) + min(
        length * width, width * height, height * length
    )
    volume = length * width * height
    smallestPerim = min(
        2 * length + 2 * width, 2 * width + 2 * height, 2 * height + 2 * length
    )
    ribbon += volume
    ribbon += smallestPerim
print(f"Part one: {wrappingPaper}")
print(f"Part two: {ribbon}")

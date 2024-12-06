import os


for year in [str(a) for a in range(2015, 2023)]:
    if not os.path.exists(year):
        os.mkdir(year)

    for i in range(1, 26):
        if not os.path.exists(f"{year}/Day{i}"):
            os.mkdir(f"{year}/Day{i}")
        if not os.path.exists(f"{year}/Day{i}/D{i}.py"):
            with open(f"{year}/Day{i}/D{i}.py", "w") as pyFile:
                pyFile.write(
                    f'with open("{year}/Day{i}/input.txt", "r") as input:\n    pass'
                )
        if not os.path.exists(f"{year}/Day{i}/input.txt"):
            with open(f"{year}/Day{i}/input.txt", "w") as input:
                input.write("")

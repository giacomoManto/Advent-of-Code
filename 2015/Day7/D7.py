import re
import numpy as np
from functools import lru_cache

reWIRE = re.compile(r"^(\w+) -> (\w+)", re.MULTILINE)
reAND = re.compile(r"^(\w+) AND (\w+) -> (\w+)", re.MULTILINE)
reLSHIFT = re.compile(r"^(\w+) LSHIFT (\w+) -> (\w+)", re.MULTILINE)
reRSHIFT = re.compile(r"^(\w+) RSHIFT (\w+) -> (\w+)", re.MULTILINE)
reNOT = re.compile(r"^NOT (\w+) -> (\w+)", re.MULTILINE)
reOR = re.compile(r"^(\w+) OR (\w+) -> (\w+)", re.MULTILINE)

with open("2015/Day7/input.txt", "r") as input:
    data = input.read()

wires = {}
bands = {}
bors = {}
lshifts = {}
rshifts = {}
bnots = {}

for wire in reWIRE.findall(data):
    wires[wire[1]] = wire[0]

for band in reAND.findall(data):
    bands[band[2]] = (band[0], band[1])

for bor in reOR.findall(data):
    bors[bor[2]] = (bor[0], bor[1])

for lshift in reLSHIFT.findall(data):
    lshifts[lshift[2]] = (lshift[0], lshift[1])

for rshift in reRSHIFT.findall(data):
    rshifts[rshift[2]] = (rshift[0], rshift[1])

for bnot in reNOT.findall(data):
    bnots[bnot[1]] = bnot[0]


@lru_cache(maxsize=None)
def solve(out: str):
    try:
        return np.uint16(int(out))
    except ValueError:
        pass
    if out in wires:
        return solve(wires[out])
    elif out in bands:
        return solve(bands[out][0]) & solve(bands[out][1])
    elif out in bors:
        return solve(bors[out][0]) | solve(bors[out][1])
    elif out in lshifts:
        return solve(lshifts[out][0]) << solve(lshifts[out][1])
    elif out in rshifts:
        return solve(rshifts[out][0]) >> solve(rshifts[out][1])
    elif out in bnots:
        return ~solve(bnots[out])


print(solve("a"))

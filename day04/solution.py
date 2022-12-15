import os
import re

with open(os.getcwd() + "/day04/input.txt") as f:
    input = f.read().splitlines()

pairs = [re.split(",|-", str) for str in input]

pair_overlap = {}
pair_overlap[1] = [
    True
    if (int(lst[0]) <= int(lst[2]) and int(lst[1]) >= int(lst[3]))
    or (int(lst[0]) >= int(lst[2]) and int(lst[1]) <= int(lst[3]))
    else False
    for lst in pairs
]
pair_overlap[2] = [
    True
    if (int(lst[1]) >= int(lst[2]) and int(lst[1]) <= int(lst[3]))
    or (int(lst[3]) >= int(lst[0]) and int(lst[3]) <= int(lst[1]))
    else False
    for lst in pairs
]

for k, lst in pair_overlap.items():
    print(
        "The number of overlapping pairs for part",
        k,
        ":\n",
        sum(lst),
    )

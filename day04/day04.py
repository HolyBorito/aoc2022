import os
import re

with open(os.getcwd() + "/day04/input.txt") as f:
    input = f.read().splitlines()

pairs = [re.split(",|-", str) for str in input]

range_overlap = {}
range_overlap[1] = [
    True
    if (int(lst[0]) <= int(lst[2]) and int(lst[1]) >= int(lst[3]))
    or (int(lst[0]) >= int(lst[2]) and int(lst[1]) <= int(lst[3]))
    else False
    for lst in pairs
]
range_overlap[2] = [
    True
    if (int(lst[1]) >= int(lst[2]) and int(lst[1]) <= int(lst[3]))
    or (int(lst[3]) >= int(lst[0]) and int(lst[3]) <= int(lst[1]))
    else False
    for lst in pairs
]

for k, lst in range_overlap.items():
    print(
        "The number of pairs in which their ranges overlap for part",
        k,
        ":\n",
        sum(lst),
    )

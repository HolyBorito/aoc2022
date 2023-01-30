import os
from itertools import groupby

with open(os.getcwd() + "/day01/input.txt") as f:
    input = f.read().splitlines()

elf_calories = [list(g) for k, g in groupby(input, key=bool) if k]
elf_calories = [[int(i) for i in lst] for lst in elf_calories]
elf_calories_tot = [sum(lst) for lst in elf_calories]
print(
    "Amount of calories of the elf carrying the most calories:\n",
    max(elf_calories_tot),
)

elf_calories_tot_top3 = sorted(elf_calories_tot, reverse=True)[:3]
print(
    "Amount of calories of the top three elves carrying the most calories:\n",
    sum(elf_calories_tot_top3),
)

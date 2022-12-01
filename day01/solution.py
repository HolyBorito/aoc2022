import os
from itertools import groupby

with open(os.getcwd() + "/day01/input.txt") as f:
    input = f.read().splitlines()

# Divide list into sub-lists, convert strings to integers,
# sum over the values of each sub-list and find the maximum value
elf_calories = [list(g) for k, g in groupby(input, key=bool) if k]
elf_calories = [[int(i) for i in lst] for lst in elf_calories]
elf_calories_tot = [sum(lst) for lst in elf_calories]
print(
    "Amount of calories of the elf carrying the most calories:",
    max(elf_calories_tot),
)

# Extract the top three Elves with the most calories and their sum
elf_calories_tot_top3 = sorted(elf_calories_tot, reverse=True)[:3]
print(
    "Amount of calories of the top three elves carrying the most calories:",
    sum(elf_calories_tot_top3),
)

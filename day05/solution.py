import copy
import re

with open("/home/1000/gitrepos/aoc2022/day05/input.txt") as f:
    input = f.read().splitlines()

n_stacks = 9
crates = {}
crates[1] = {k + 1: [] for k in range(0, n_stacks)}

for i in range(0, n_stacks - 1):
    for str in re.finditer("\[", input[i]):
        crates[1][(str.start() / 4) + 1].append(input[i][str.start() + 1])
crates[2] = copy.deepcopy(crates[1])
# print(crates)

for s in range(n_stacks + 1, len(input)):
    step = re.findall(r"\d+", input[s])
    crates[1][int(step[2])][:0] = list(
        reversed(crates[1][int(step[1])][: int(step[0])])
    )
    crates[2][int(step[2])][:0] = list(crates[2][int(step[1])][: int(step[0])])
    del crates[1][int(step[1])][: int(step[0])]
    del crates[2][int(step[1])][: int(step[0])]
# print(crates)

for k, c in crates.items():
    message = ""
    for s in c:
        message += crates[k][s][0]
    print(
        "The message consisting of the crates ending up on top of each stack for part",
        k,
        ":\n",
        message,
    )

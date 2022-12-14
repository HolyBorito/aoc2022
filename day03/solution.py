import os
import string

with open(os.getcwd() + "/day03/input.txt") as f:
    rucksack_items = f.read().splitlines()

first_compartment, second_compartment = zip(
    *[(str[: len(str) // 2], str[len(str) // 2 :]) for str in rucksack_items]
)

common_items = {}
common_items[1] = [
    "".join(set(first_compartment[i]).intersection(second_compartment[i]))
    for i in range(len(rucksack_items))
]

common_items[2] = [
    "".join(
        set(rucksack_items[3 * i]).intersection(
            rucksack_items[3 * i + 1], rucksack_items[3 * i + 2]
        )
    )
    for i in range(int(len(rucksack_items) / 3))
]
priorities = [
    [
        string.ascii_lowercase.index(str.lower()) + 1
        if str.islower()
        else string.ascii_lowercase.index(str.lower()) + 27
        for str in lst
    ]
    for lst in common_items.values()
]

[
    print(
        "The sum of priorities of common item types for part",
        k,
        ":\n",
        sum(prio),
    )
    for k, prio in dict(zip([1, 2], priorities)).items()
]

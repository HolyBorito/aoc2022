import re

from find_nested_keys_values import (
    find_directory_size,
    find_parent_keys,
    update_key_value,
)

# with open("/home/1000/gitrepos/aoc2022/day07/input_test.txt") as f:
#     output = f.read().splitlines()
with open("/home/1000/gitrepos/aoc2022/day07/input.txt") as f:
    output = f.read().splitlines()

output = [re.split(" ", out) for out in output]
# print(output)

###############################################################################
### OBTAIN THE FULL DICTIONARY REPRESENTATION OF THE FILESYSTEM DIRECTORIES ###
### TOGETHER WITH THE CORRESPONDING DIRECTORY SIZES (GET_SIZE=TRUE).        ###
###############################################################################
filesystem = {}
GET_SIZE = True

for i in range(2, len(output)):
    if output[i - 1][-1] == "ls":
        # print(filesystem, i - 1, output[i - 2])
        parent_keys = find_parent_keys(filesystem, output[i - 2][-1], "dir")
        if len(parent_keys) == 1:
            if GET_SIZE:
                filesystem[output[i - 2][-1]] = [0, {}]
            else:
                filesystem[output[i - 2][-1]] = {}
        else:
            if GET_SIZE:
                filesystem = update_key_value(
                    filesystem,
                    parent_keys,
                    output[i - 2][-1],
                    [0, {}],
                    GET_SIZE,
                )
            else:
                filesystem = update_key_value(
                    filesystem,
                    parent_keys,
                    output[i - 2][-1],
                    {},
                    GET_SIZE,
                )
        for lst in output[i:]:
            if lst[0] != "$":
                filesystem = update_key_value(
                    filesystem,
                    parent_keys,
                    output[i - 2][-1],
                    {lst[-1]: lst[0]},
                    GET_SIZE,
                )
            else:
                break
# print(filesystem)

if GET_SIZE:
    USED_SPACE = filesystem["/"][0]
    UNUSED_SPACE = 30000000
    TOTAL_SPACE = 70000000
    sum_dir_sizes = find_directory_size(filesystem, MAX_SIZE=100000)
    target_dir_size = find_directory_size(
        filesystem, MIN_SIZE=USED_SPACE + UNUSED_SPACE - TOTAL_SPACE
    )
    print(f"The sum of allowed total directory sizes is:\n {sum_dir_sizes}")
    print(f"The smallest allowed total directory size is:\n {target_dir_size}")

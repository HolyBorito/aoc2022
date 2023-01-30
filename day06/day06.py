with open("/home/1000/gitrepos/aoc2022/day06/input.txt") as f:
    buffer = f.read()

markers = {"packet": 4, "message": 14}

for k, char in markers.items():
    sliding_window = [
        buffer[i : i + char] for i in range(0, len(buffer) - char + 1)
    ]
    # print(sliding_window)

    first_marker = (
        next(
            (
                i
                for i in range(0, len(sliding_window))
                if len(set(sliding_window[i])) is len(sliding_window[i])
            ),
            None,
        )
        + char
    )

    print(
        f"The first start-of-{k} marker occurs after character:\n {first_marker}"
    )

import os

import pandas as pd

# A, X: rock
# B, Y: paper
# C, Z: scissor
score = {}
score["rock"] = 1
score["paper"] = 2
score["scissor"] = 3
score["lost"] = 0
score["draw"] = 3
score["win"] = 6
score_matrix_1 = pd.DataFrame(
    columns=["X", "Y", "Z"],
    index=["A", "B", "C"],
)
score_matrix_1.loc["A"] = [
    score["rock"] + score["draw"],
    score["paper"] + score["win"],
    score["scissor"] + score["lost"],
]
score_matrix_1.loc["B"] = [
    score["rock"] + score["lost"],
    score["paper"] + score["draw"],
    score["scissor"] + score["win"],
]
score_matrix_1.loc["C"] = [
    score["rock"] + score["win"],
    score["paper"] + score["lost"],
    score["scissor"] + score["draw"],
]
# print(score_matrix_1)
score_matrix_2 = pd.DataFrame(
    columns=["X", "Y", "Z"],
    index=["A", "B", "C"],
)
score_matrix_2.loc["A"] = [
    score["scissor"] + score["lost"],
    score["rock"] + score["draw"],
    score["paper"] + score["win"],
]
score_matrix_2.loc["B"] = [
    score["rock"] + score["lost"],
    score["paper"] + score["draw"],
    score["scissor"] + score["win"],
]
score_matrix_2.loc["C"] = [
    score["paper"] + score["lost"],
    score["scissor"] + score["draw"],
    score["rock"] + score["win"],
]
# print(score_matrix_2)

with open(os.getcwd() + "/day02/input.txt") as f:
    rounds = pd.read_csv(f, sep=" ", header=None)

rounds.columns = ["opponent", "you"]
for k, df in {1: score_matrix_1, 2: score_matrix_2}.items():
    for opp_move in ["A", "B", "C"]:
        for your_move in ["X", "Y", "Z"]:
            rounds.loc[
                (rounds["opponent"] == opp_move)
                & (rounds["you"] == your_move),
                "score",
            ] = df.loc[opp_move, your_move]
    print(
        "Your total score according to the strategy guide for part",
        k,
        ":\n",
        sum(rounds["score"]),
    )

import numpy as np

def find_view_distance(list_, height) -> int:
    for i, L_height in enumerate(list_):
        if L_height >= height:
            return (i + 1)
    return len(list_)

with open("input.txt", "r") as file:
    heights = [[int(j) for j in i] for i in file.read().split("\n")]
    heights.pop(len(heights)-1)

    np_heights = np.transpose(np.vstack([np.array(i) for i in heights]))
    t_heights = [[j for j in list(i)] for i in np_heights]

    scores = []

    for i, row in enumerate(heights):
        for j, height in enumerate(row):
            view = [
                    [n for index, n in enumerate(row) if index > j],
                    [n for index, n in enumerate(row) if index < j][::-1],
                    [n for index, n in enumerate(t_heights[j]) if index > i],
                    [n for index, n in enumerate(t_heights[j]) if index < i][::-1]
            ]

            score = 1
            for d in view:
                score *= find_view_distance(d, height)

            scores.append(score)

    print(max(scores))


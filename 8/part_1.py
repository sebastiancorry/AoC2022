import numpy as np

with open("input.txt", "r") as file:
    heights = [[int(j) for j in i] for i in file.read().split("\n")]
    heights.pop(len(heights)-1)

    np_heights = np.transpose(np.vstack([np.array(i) for i in heights]))
    t_heights = [[j for j in list(i)] for i in np_heights]

    visible = (2 * len(heights)) + (2 * len(t_heights)) - 4

    for i, row in enumerate(heights[1:len(heights) - 1], start=1):
        for h, height in enumerate(row[1:len(row) - 1], start=1):
            if height > max(row[:h]) or height > max(row[h+1:]) or height > max(t_heights[h][:i]) or height > max(t_heights[h][i+1:]):
                visible += 1

    print(visible)


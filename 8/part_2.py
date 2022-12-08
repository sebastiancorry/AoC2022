import numpy as np

with open("test.txt", "r") as file:
    heights = [[int(j) for j in i] for i in file.read().split("\n")]
    heights.pop(len(heights)-1)

    np_heights = np.transpose(np.vstack([np.array(i) for i in heights]))
    t_heights = [[j for j in list(i)] for i in np_heights]

    scores = []

    while len(scores) < len(heights) * len(heights):
        for i in heights:
            score = 1
            for j, height in enumerate(i):
                for k, h in enumerate(i[:j][::-1]):
                    if h >= height:
                        score *= k + 1
                        break

                for k, h in enumerate(i[j+1:]):
                    if h >= height:
                        score *= k + 1
                        break

        for i in t_heights:
            for j, height in enumerate(i):
                for k, h in enumerate(i[:j][::-1]):
                    if h >= height:
                        score *= k + 1
                        break

                for k, h in enumerate(i[j+1:]):
                    if h >= height:
                        score *= k + 1
                        break

        scores.append(score)

    print(max(scores))


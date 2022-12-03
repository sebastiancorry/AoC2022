# Documentation can be found in ./part_2.py

otal_score = 0
round_scores = []

home_key = ["Z", "Y", "X"]
opp_key = ["C", "B", "A"]

key = [
       ["X", "A", 2], # Rock
       ["Y", "B", 0], # Paper
       ["Z", "C", 1]  # Scissors
        ]

def search_2D(L, n):
    for i, x in enumerate(L):
        if n in x:
            return i

file = open('./input.txt', 'r')

def rock_paper_scissors(home_move, opp_move, key):
    home_index = search_2D(key, home_move)
    home_key_val = key[home_index]

    if home_key_val[1] == opp_move:
        return 3 + (home_index + 1)

    if home_key_val[2] == search_2D(key, opp_move):
        return 6 + (home_index + 1)
    else:
        return 0 + (home_index + 1)

for line in file:
    characters = [x for x in line]
    home_move = characters[2];
    opp_move = characters[0];

    score = rock_paper_scissors(home_move, opp_move, key)
    round_scores.append(score)
    total_score += score

file.close()

print(total_score)


# Open file.
file = open('./input.txt', 'r')

total_score = 0
round_scores = [] # Not used but implemented in part 1 in case of part 2.

# [Home Input, Opponent Input, Index of input it beats]
key = [
       ["X", "A", 2], # Rock
       ["Y", "B", 0], # Paper
       ["Z", "C", 1]  # Scissors
        ]

# Search a 2D array and return the first element of the index vector.
def search_2D(L, n):
    for i, x in enumerate(L):
        if n in x:
            return i

# Conver the input of Lose/Draw/Win to the inputs used in part 1.
def convert_input_to_move(home_input, opp_move, key):
    opp_index = search_2D(key, opp_move)
    match home_input:
        case "X": # Lose
            return key[key[opp_index][2]][0] # Return the move that loses to opp_move.
        case "Y": # Draw
            return key[opp_index][0] # Return the same move as opp_move.
        case "Z": # Win
            return key[search_2D(key, opp_index)][0] # Return the move that beats opp_move.

# Compute game.
def rock_paper_scissors(home_input, opp_move, key):
    # Part 2.
    home_move = convert_input_to_move(home_input, opp_move, key)

    # Get the key index for the home input.
    home_index = search_2D(key, home_move)

    # Get the key entry.
    home_key_val = key[home_index]

    if home_key_val[1] == opp_move: # Draw
        return 3 + (home_index + 1)

    if home_key_val[2] == search_2D(key, opp_move): # Win
        return 6 + (home_index + 1)
    else: # Lose
        return 0 + (home_index + 1)

# Iterate through file.
for line in file:
    # Parse inputs.
    characters = [x for x in line] # Split line by character.
    home_move = characters[2];
    opp_move = characters[0];

    # Temporary score variable.
    score = rock_paper_scissors(home_move, opp_move, key)

    # Update global score variables.
    round_scores.append(score)
    total_score += score

# Print result.
print(total_score)


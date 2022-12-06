import numpy as np
import re

with open("input.txt", "r") as file:
    crates = []
    instructions = []
    for line in file:
        if "move" in line:
            split_line = line.split(" ")
            instructions.append([int(split_line[1]), int(split_line[3]), int(split_line[5])])
        elif "[" in line:
            c_counter = 0 # Tracks the number of white spaces in a row.
            row = [] # The current row/line of the file as parsed.

            # Iterate through characters in line.
            for c in line:
                if c == " ": # White space.
                    c_counter += 1
                    if c_counter >= 4:
                        row.append("NULL")
                        c_counter = 0

                elif c != "\n" and c!= "[" and c!= "]": # Add crate.
                    row.append(c)
                    c_counter = 0

            # Push row to crates.
            crates.append(row)

    # Transpose crates to form columns.
    np_crates = np.transpose(np.vstack([np.array(i) for i in crates]))
    crates = [[j for j in list(i) if j != "NULL"] for i in np_crates]

    for i in crates:
        print(i)
    print("\n\n")

    # crates = [["D","Z","T","H"],["S","C","G","T","W","R","Q"],["H","C","R","N","Q","F","B","P"],["Z","H","F","N","C","L"],["S","Q","F","L","G"],["S","C","R","B","Z","W","P","V"],["J","F","Z"],["Q","H","R","Z","V","L","D"],["D","L","Z","F","N","G","H","B"]]

    # Run simulation.
    for i in instructions:
        m_crates = crates[i[1]-1][:i[0]]
        print(m_crates)
        print(m_crates)
        crates[i[2]-1] = [*m_crates, *crates[i[2]-1]]
        print("BEFORE")
        print(crates[i[1]-1])
        for j in range(i[0]):
            crates[i[1]-1].pop(0)
        print(crates[i[1]-1])
        print("!")
        for j in crates:
            print(j)
        print("?\n\n")

    for i in crates:
        print(i[0])


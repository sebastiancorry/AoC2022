import time
import os

def modify_coord(coord, mod):
    return tuple(map(lambda a,b: a+b, coord, mod))

def visualize(map_, emphasis=(0,0)):
    L_bound = min([i[0] for i in map_])
    r_bound = max([i[0] for i in map_])
    u_bound = min([i[1] for i in map_])
    b_bound = max([i[1] for i in map_])
    for i in range(u_bound, b_bound+1):
        for j in range(L_bound, r_bound+1):
            c = '#' if map_.setdefault((j,i), False) else '.'
            if (j,i) == emphasis:
                print("\033[1m" + "O", end=" ")
            else:
                print("\033[0m" + c, end=" ")
        print()

with open("input.txt", "r") as file:
    # Parse the file.
    map_ = {}
    for line in file:
        f_coords = line.strip().split("->")
        for i in range(len(f_coords) - 1):
            x1, y1 = tuple(int(comp) for comp in f_coords[i].split(","))
            x2, y2 = tuple(int(comp) for comp in f_coords[i+1].split(","))

            if x1 - x2 != 0:
                x1, x2 = sorted([x1, x2])
                for x in range(x1, x2+1):
                    map_[(x, y1)] = True
            else: # y1 - y2 != 0
                y1, y2 = sorted([y1, y2])
                for y in range(y1, y2+1):
                    map_[(x1, y)] = True

    # NOTE: max and min are inverted in the following lines as y increases as it gets lower.

    # Find the maximum height for x = 500.
    x500 = [i for i in map_ if i[0] == 500]
    x500_max = min(x500, key=lambda x: x[1])[1]

    # Find the minimum height for y in map_.
    y = [i[1] for i in map_]
    y_min = max(y) + 2

    # Add floor.
    for i in range(0, 1000):
        map_[i, y_min] = True

    # Simulate sand.
    n = 0
    while not map_.setdefault((500,0), False):
        s_coord = (500, x500_max - 1)

        at_rest = False
        while not at_rest:
            # Translate down.
            if not map_.setdefault(modify_coord(s_coord, (0,1)), False):
                s_coord = modify_coord(s_coord, (0,1))

            # Left and down.
            elif not map_.setdefault(modify_coord(s_coord, (-1,1)), False):
                s_coord = modify_coord(s_coord, (-1,1))

            # Right and down.
            elif not map_.setdefault(modify_coord(s_coord, (1,1)), False):
                s_coord = modify_coord(s_coord, (1,1))

            # At rest.
            else:
                at_rest = True

        if s_coord == (500, x500_max - 1):
            x500_max -= 1
        map_[s_coord] = True
        if at_rest:
            n += 1

    print(n)

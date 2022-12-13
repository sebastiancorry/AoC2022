import numpy as np

def is_edge(component, bound):
    return (component == 0 or component == bound - 1)

def is_corner(coord, r_bound, b_bound):
    return (coord == (0, 0)\
            or coord == (r_bound - 1, 0)\
            or coord == (0, b_bound - 1)\
            or coord == (r_bound - 1, b_bound - 1))

# Only use after checking that a coordinate is on an edge!
def which_edge(component, bound):
    return (component == bound - 1)

def find_distance(A, B, map_):
    v_A = map_[A[0]][A[1]]
    if v_A == -13:
        v_A = 1

    if v_A == -27:
        v_A = 26

    v_B = map_[B[0]][B[1]]
    if v_B == -13:
        v_B = 1

    if v_B == -27:
        v_B = 26

    if v_B >= v_A:
        return abs(v_A - v_B)
    else:
        return 1

def check_connection(x, y, C, map_):
    return [C] if find_distance((x, y), C, map_) <= 1 else []

with open("input.txt", "r") as file:
    map_ = []
    for line in file:
        line = line.strip()
        map_.append([ord(c) - 96 for c in line])

    np_map_ = np.transpose(np.vstack([np.array(i) for i in map_]))
    map_ = [[j for j in list(i)] for i in np_map_]

    # Boundary variables.
    x_bound = len(map_)
    y_bound = len(map_[0])

    # Find starting place.
    start = (0, 0)
    if map_[0][0] != -13:
        for x in range(x_bound):
            for y in range(y_bound):
                if map_[x][y] == -13:
                    start = (x, y)
                    break
            if map_[start[0]][start[1]] == -13:
                break

    # Find ending place.
    end = (0, 0)
    if map_[0][0] != -27:
        for x in range(x_bound):
            for y in range(y_bound):
                if map_[x][y] == -27:
                    end = (x, y)
                    break
            if map_[end[0]][end[1]] == -27:
                break

    # Generate graph.
    ve_pairs = {}
    for x in range(x_bound):
        for y in range(y_bound):
            connections = []

            if is_corner((x, y), x_bound, y_bound):
                x_edge = which_edge(x, x_bound)
                y_edge = which_edge(y, y_bound)
                x_modifier = -1 if x_edge else 1
                y_modifier = -1 if y_edge else 1

                connections += check_connection(x, y, (x+x_modifier, y), map_)\
                            + check_connection(x, y, (x, y+y_modifier), map_)
            elif is_edge(x, x_bound):
                edge = which_edge(x, x_bound)
                modifier = -1 if edge else 1

                connections += check_connection(x, y, (x+modifier, y), map_)\
                            + check_connection(x, y, (x, y+1), map_)\
                            + check_connection(x, y, (x, y-1), map_)
            elif is_edge(y, y_bound):
                edge = which_edge(y, y_bound)
                modifier = -1 if edge else 1

                connections += check_connection(x, y, (x, y+modifier), map_)\
                            + check_connection(x, y, (x+1, y), map_)\
                            + check_connection(x, y, (x-1, y), map_)
            else:
                connections += check_connection(x, y, (x+1, y), map_)\
                            + check_connection(x, y, (x-1, y), map_)\
                            + check_connection(x, y, (x, y+1), map_)\
                            + check_connection(x, y, (x, y-1), map_)

            ve_pairs[(x, y)] = connections

    def min_(dict_):
        minimum = min(dict_.items(), key=lambda x: x[1])[0]
        mins = [v for v in dict_ if dict_[v] == minimum]
        mins.append(minimum)
        print(minimum)
        highest = map_[mins[0][0]][mins[0][1]]
        highest_coord = mins[0]
        for m in mins:
            if map_[m[0]][m[1]] > highest:
                highest = map_[m[0]][m[1]]
                highest_coord = m
        return highest_coord

    visited = {start : 0}
    queue = [start]
    while queue and not end in visited:
        v = queue.pop(0)

        for i in ve_pairs[v]:
            if i not in visited:
                visited[i] = visited[v] + 1
                queue.append(i)

    print(visited[end])


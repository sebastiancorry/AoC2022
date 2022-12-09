import operator

def transform(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

with open("input.txt", "r") as file:
    # Transformations for HEAD.
    directions = {
            "L": lambda c: (c[0] - 1, c[1]),
            "R": lambda c: (c[0] + 1, c[1]),
            "U": lambda c: (c[0], c[1] + 1),
            "D": lambda c: (c[0], c[1] - 1)
            }

    # Knots.
    n_coords = [(0, 0)] * 10
    # Points that the TAIL has covered.
    points = [n_coords[0]]

    for line in file:
        # Parse line.
        dir_, dist = line.replace("\n", "").split(" ")
        dist = int(dist)

        while dist > 0:
            # Move HEAD one unit.
            n_coords[0] = directions[dir_](n_coords[0])

            for i in range(1, len(n_coords)):
                # Compute vector between previous knot and current one.
                pc_vec = tuple(map(operator.sub, n_coords[i-1], n_coords[i]))

                # If current knot is far from previous knot.
                if abs(pc_vec[0]) > 1 or abs(pc_vec[1]) > 1:
                    transformation = tuple(map(transform, pc_vec))
                    n_coords[i] = tuple(map(operator.add, n_coords[i], transformation))

            points.append(n_coords[9])

            # Update distance.
            dist -= 1

    print(len(set(points)))


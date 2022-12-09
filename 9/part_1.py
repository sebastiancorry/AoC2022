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

    # HEAD / TAIL.
    h_coords, t_coords = (0, 0), (0, 0)
    # Points that the TAIL has covered.
    points = [t_coords]

    for line in file:
        # Parse line.
        dir_, dist = line.replace("\n", "").split(" ")
        dist = int(dist)

        while dist > 0:
            # Move HEAD one unit.
            h_coords = directions[dir_](h_coords)

            # Compute vector between the HEAD and TAIL.
            ht_vec = tuple(map(operator.sub, h_coords, t_coords))

            # If the TAIL is far away from the HEAD.
            if abs(ht_vec[0]) > 1 or abs(ht_vec[1]) > 1:
                transformation = tuple(map(transform, ht_vec))
                t_coords = tuple(map(operator.add, t_coords, transformation))

            points.append(t_coords)

            # Update distance.
            dist -= 1

    print(len(set(points)))


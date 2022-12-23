# Manhattan distance.
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def project_row(S, y, d):
    dy = abs(y - S[1])
    return abs(d + 1 - dy)

with open("test.txt", "r") as file:
    # Signal / Distance pairs.
    s_dist = {}

    beacons = []

    y_bound = 20

    for line in file:
        # Parse coordinates.
        f_sensor = line.strip().split(":")[0].split("at")[1].replace(",", "=").split("=")[1::2]
        f_beacon = line.strip().split("at")[2].replace(",", "=").split("=")[1::2]

        sensor = tuple(int(i) for i in f_sensor)
        beacon = tuple(int(i) for i in f_beacon)

        # Signal : Distance to beacon.
        s_dist[sensor] = distance(sensor, beacon)

    break_bool = False
    not_beacon = []
    for y in range(0, y_bound):
        nb = []
        for s in s_dist:
            p = project_row(s, y, s_dist[s])
            nb.append((s[0]-p, s[0]+p))

        not_beacon.append(nb)
        print(y / y_bound)

    for i in not_beacon:
        print(i)

    answer = 0
    for y in range(0, y_bound):
        for r in not_beacon[y]:
            row = [r for r in not_beacon[y]]
            min_ = min(row, key=lambda x: x[0])[0]
            max_ = max(row, key=lambda x: x[1])[1]
            for x in range(min_, max_+1):
                if x not in range(r[0]-1, r[1]+1):
                    print(x)
                    # answer = (x*4_000_000) + y
                    break
            if answer != 0:
                break
        if answer != 0:
            break

    print(answer)


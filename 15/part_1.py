# Manhattan distance.
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def project_row(S, y, d):
    dy = abs(y - S[1])
    return d + 1 - dy

with open("input.txt", "r") as file:
    # Signal / Distance pairs.
    s_dist = {}

    beacons = []

    for line in file:
        # Parse coordinates.
        f_sensor = line.strip().split(":")[0].split("at")[1].replace(",", "=").split("=")[1::2]
        f_beacon = line.strip().split("at")[2].replace(",", "=").split("=")[1::2]

        sensor = tuple(int(i) for i in f_sensor)
        beacon = tuple(int(i) for i in f_beacon)

        beacons.append(beacon)

        # Signal : Distance to beacon.
        s_dist[sensor] = distance(sensor, beacon)

    beacons = set(beacons)

    y = 2000000
    not_beacon = set()

    for s in s_dist:
        p = project_row(s, y, s_dist[s])
        print(f"{s} : {s_dist[s]} : {p}")
        for i in range(s[0]-p+1, s[0]+p):
            if not (i,y) in beacons:
                not_beacon.add(i)

    print(len(not_beacon))


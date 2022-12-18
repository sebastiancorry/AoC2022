def pressure(v_rates, v_conns, initial, time, memo={}):
    if time == 1:
        return v_rates[initial]

    routes = []

    n_v_rates = dict(v_rates)
    n_v_rates[initial] = 0
    routes.append(\
            (v_rates[initial] * (time-1)) + pressure(n_v_rates, v_conns, initial, time-1, memo))

    str_rates = "".join([str(i) for i in v_rates.values()])
    for neighbor in v_conns[initial]:
        if (str_rates, neighbor, time-1) in memo:
            routes.append(memo[(str_rates, neighbor, time-1)])
        else:
            p = pressure(v_rates, v_conns, neighbor, time-1, memo)
            memo[(str_rates, neighbor, time-1)] = p
            routes.append(p)

    return max(routes)

with open("test.txt", "r") as file:
    v_rates = {}
    v_conns = {}

    for line in file:
        valve_id = line.split(" ")[1]
        rate = int(line.split("=")[1].split(";")[0])

        f_connections = line.split(";")[1].split(" ")[5::]
        connections = "".join(f_connections).strip().split(",")

        v_rates[valve_id] = rate
        v_conns[valve_id] = connections

    print(pressure(v_rates, v_conns, "AA", 26, {}))


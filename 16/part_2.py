def pressure(v_rates, v_conns, agent, elephant, time, a_vis=set(), e_vis=set(), memo={}):
    if time == 1 or (set(v_conns[agent]).issubset(a_vis) and set(v_conns[elephant]).issubset(e_vis)):
        if agent != elephant:
            return v_rates[agent] + v_rates[elephant]
        else:
            return v_rates[agent]

    routes = []

    # Agent opens, Elephant opens.
    if agent != elephant and v_rates[agent] != 0 and v_rates[elephant] != 0:
        n_v_rates = dict(v_rates)
        n_v_rates[agent] = 0
        n_v_rates[elephant] = 0
        str_rates = "".join([str(i) for i in n_v_rates.values()])

        ca_vis = set()
        ce_vis = set()
        str_a_vis = "".join(list(ca_vis))
        str_e_vis = "".join(list(ce_vis))

        if (str_rates, agent, elephant, time-1, str_a_vis, str_e_vis) in memo:
            p = memo[(str_rates, agent, elephant, time-1, str_a_vis, str_e_vis)]
        else:
            p = pressure(n_v_rates, v_conns, agent, elephant, time-1, ca_vis, ce_vis, memo)
            memo[(str_rates, agent, elephant, time-1, str_a_vis, str_e_vis)] = p
        routes.append(\
                (v_rates[agent] * (time-1))\
                + (v_rates[elephant] * (time-1))\
                + p\
                )

    # Agent opens, Elephant proceeds.
    if v_rates[agent] != 0:
        n_v_rates = dict(v_rates)
        n_v_rates[agent] = 0
        str_rates = "".join([str(i) for i in n_v_rates.values()])
        for neighbor in v_conns[elephant]:
            if neighbor not in e_vis:
                ce_vis = set(e_vis)
                ce_vis.add(neighbor)
                str_a_vis = "".join(list())
                str_e_vis = "".join(list(str_rates))

                if (str_rates, agent, neighbor, time-1, str_a_vis, str_e_vis) in memo:
                    routes.append(memo[(str_rates, agent, neighbor, time-1, str_a_vis, str_e_vis)]\
                                    + (v_rates[agent] * (time-1)))
                else:
                    p = pressure(n_v_rates, v_conns, agent, neighbor, time-1, set(), ce_vis, memo)
                    memo[(str_rates, agent, neighbor, time-1, str_a_vis, str_e_vis)] = p
                    routes.append(p + (v_rates[agent] * (time-1)))

    # Agent proceeds, Elephant opens.
    if v_rates[elephant] != 0:
        n_v_rates = dict(v_rates)
        n_v_rates[elephant] = 0
        str_rates = "".join([str(i) for i in n_v_rates.values()])
        for neighbor in v_conns[agent]:
            if neighbor not in a_vis:
                ca_vis = set(a_vis)
                ca_vis.add(neighbor)
                str_a_vis = "".join(list(ca_vis))
                str_e_vis = "".join(list())

                if (str_rates, neighbor, elephant, time-1, str_a_vis, str_e_vis) in memo:
                    routes.append(memo[(str_rates, neighbor, elephant, time-1, str_a_vis, str_e_vis)]\
                                    + (v_rates[elephant] * (time-1)))
                else:
                    p = pressure(n_v_rates, v_conns, neighbor, elephant, time-1, ca_vis, set(), memo)
                    memo[(str_rates, neighbor, elephant, time-1, str_a_vis, str_e_vis)] = p
                    routes.append(p + (v_rates[elephant] * (time-1)))


    # Agent proceeds, Elephant proceeds.
    str_rates = "".join([str(i) for i in v_rates.values()])
    for a_neighbor in v_conns[agent]:
        if a_neighbor not in a_vis:
            for e_neighbor in v_conns[elephant]:
                if e_neighbor not in e_vis:
                    ca_vis = set(a_vis)
                    ce_vis = set(e_vis)

                    ca_vis.add(a_neighbor)
                    ce_vis.add(e_neighbor)

                    str_a_vis = "".join(list(ca_vis))
                    str_e_vis = "".join(list(ce_vis))

                    if (str_rates, a_neighbor, e_neighbor, time-1, str_a_vis, str_e_vis) in memo:
                        routes.append(memo[(str_rates, a_neighbor, e_neighbor, time-1, str_a_vis, str_e_vis)])
                    else:
                        p = pressure(v_rates, v_conns, a_neighbor, e_neighbor, time-1, ca_vis, ce_vis, memo)
                        memo[(str_rates, a_neighbor, e_neighbor, time-1, str_a_vis, str_e_vis)] = p
                        routes.append(p)

    if len(routes) > 0:
        return max(routes)
    else:
        return 0

with open("input.txt", "r") as file:
    v_rates = {}
    v_conns = {}

    for line in file:
        valve_id = line.split(" ")[1]
        rate = int(line.split("=")[1].split(";")[0])

        f_connections = line.split(";")[1].split(" ")[5::]
        connections = "".join(f_connections).strip().split(",")

        v_rates[valve_id] = rate
        v_conns[valve_id] = connections

    print(pressure(v_rates, v_conns, "AA", "AA", 26, set(), set(), {}))


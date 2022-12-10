with open("input.txt", "r") as file:
    signal_checks = [20, 60, 100, 140, 180, 220]

    lines = file.readlines()

    r_X = 1
    cycle = 1
    sum_ = 0

    for i in range(len(lines)):
        if cycle in signal_checks:
            sum_ += (r_X * cycle)

        if lines[i].strip().replace("\n", "") != "noop":
            cycle += 1
            if cycle in signal_checks:
                sum_ += (r_X * cycle)

            x = int(lines[i].replace("\n", "").split(" ")[1])
            r_X += x
        cycle += 1

    print(sum_)

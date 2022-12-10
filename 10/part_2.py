import textwrap as tw

with open("input.txt", "r") as file:
    crt = []
    r_X = 1
    next_i = 1
    instruction = (1, 0)
    for c in range(1, 241):
        if c == instruction[0]:
            r_X += instruction[1]

            line = file.readline().replace("\n", "")
            if "addx" in line:
                n = 2
                V = int(line.split(" ")[1])
                instruction = (c + n, V)
            else:
                instruction = (c + 1, 0)

        sprite = [r_X-1, r_X, r_X+1]
        if (c % 40) - 1 in sprite:
            crt.append("█")
        else:
            crt.append(".")

    print(tw.fill("".join(crt), 40))


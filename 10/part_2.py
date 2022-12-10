# with open("test.txt", "r") as file:
#     signal_checks = [20, 60, 100, 140, 180, 220]
#     crt = [[]]*6
# 
#     r_X = 1
#     cycle = 1
#     sum_ = 0
# 
#     incr = 0
#     next_inst = 0
# 
#     for cycle in range(240):
#         c_row = cycle // 40
#         c_row -= 1 if c_row > 0 else 0
# 
#         r_X += incr
#         incr = 0
# 
#         if next_inst == 0:
#             inst = file.readline()
#             if inst.strip().replace("\n", "") != "noop":
#                 next_inst = 2
#                 incr = int(inst.replace("\n", "").split(" ")[1])
# 
#         next_inst -= 1
# 
#         if cycle - ((c_row-1) * 40) == r_X:
#             crt[c_row].append("#")
#         else:
#             crt[c_row].append(".")
# 
#     for i in crt:
#         print("".join(i))


with open("test.txt", "r") as file:
    crt = ["."]*240
    r_X = 1
    x = 0
    n_inst_on = 1

    for i in range(240):
        cycle = i + 1

        if n_inst_on == cycle:
            r_X += x
            inst = file.readline()
            if not "noop" in inst:
                x = int(inst.replace("\n", "").split(" ")[1])
                n_inst_on = cycle + 2
            else:
                x = 0
                n_inst_on = cycle + 1


            if i == r_X or i - 1 == r_X or i + 1 == r_X:
                crt[i] = "#"

    for i in range(6):
        print("".join(crt[i*40:(i+1)*40]))

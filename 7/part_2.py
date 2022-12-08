with open("input.txt", "r") as file:
    path = ""
    paths = []
    file_key = {}

    for line in file:
        line = line.replace("\n", "")
        args = line.split(" ")
        if line.startswith("$ cd"):
            if ".." in line:
                path = "_".join(path.split("_")[:len(path.split("_")) - 1])
            else:
                path = path + "_" + args[2]
                paths.append(path)
        elif not line.startswith("$"):
            t_path = path + "_" + args[1]

            if not line.startswith("dir"):
                file_key[t_path + "F"] = int(args[0])
                paths.append(t_path + "F")
            else:
                paths.append(t_path)

    paths = list(set(paths))
    paths.sort(key=lambda x: (len(x), x), reverse=True)

    result = 0
    result_vals = {}
    sums = {}

    for p in paths:
        sum = 0

        if p in file_key:
            sum = file_key[p]
        else:
            for i in sums:
                if p in i and len(i.split("_")) - len(p.split("_")) == 1:
                    sum += sums[i]
            if sum <= 100000:
                result += sum
                result_vals[p] = sum
        sums[p] = sum

    unused = 70000000 - sums["_/"]
    needed = 30000000 - unused
    l_sums = [sums[i] for i in sums]
    l_sums.sort(reverse=True)
    for i in range(len(l_sums)):
        if l_sums[i] < needed:
            print("\n\n\n")
            print("Result: " + str(l_sums[i-1]))
            break


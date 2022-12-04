file = open("input.txt", "r")

sum = 0

for line in file:
    ranges = [set([i for i in range(int(x.split("-")[0]), int(x.split("-")[1])+1)]) for x in line.strip().split(",")]
    print(ranges)
    sum += 1 if len(ranges[0] & ranges[1]) != 0 else 0

print(sum)

file.close()

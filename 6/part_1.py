def find_marker(dstream):
    for i in range(len(dstream) - 4):
        if len(set(dstream[i:i+4])) == 4:
            return (i + 4)

with open("input.txt", "r") as f:
    print(find_marker(f.readline()))


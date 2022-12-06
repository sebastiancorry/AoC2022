def find_marker(dstream):
    for i in range(len(dstream) - 14):
        if len(set(dstream[i:i+14])) == 14:
            return (i + 14)

with open("input.txt", "r") as f:
    print(find_marker(f.readline()))


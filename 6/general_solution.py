def find_marker(dstream, num_c):
    for i in range(len(dstream) + num_c):
        if len(set(dstream[i:i+num_c])) == num_c:
            return (i + num_c)

import sys

with open(str(sys.argv[1]), "r") as f:
    print(find_marker(f.readline(), int(sys.argv[2])))


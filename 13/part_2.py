class Pair:
    def __init__(self, packet1, packet2):
        self.packet1 = packet1

        self.packet2 = packet2
        self.correct = False

def is_correct(left, right):
    for i in range(len(left)):
        if i >= len(right):
            break

        if isinstance(left[i], int)\
        and isinstance(right[i], int)\
        and left[i] != right[i]:
            return left[i] < right[i]

        elif isinstance(left[i], int)\
        and isinstance(right[i], list):
            return is_correct([left[i]], right[i])

        elif isinstance(left[i], list)\
        and isinstance(right[i], int):
            return is_correct(left[i], [right[i]])

        elif left[i] != right[i]: # Both are lists.
            return is_correct(left[i], right[i])

    return len(left) <= len(right)

def bubble_sort(packets):
    n_packets = len(packets)

    for i in range(n_packets):
        for j in range(0, n_packets-i-1):
            if is_correct(packets[j+1], packets[j]):
                packets[j], packets[j+1] = packets[j+1], packets[j]

    return packets

with open("input.txt", "r") as file:
    # Parse file.
    lines = file.read().split("\n")
    packets = []
    for line in lines:
        if line.strip():
            packets.append(eval(line.strip()))

    # Divider packets.
    packets.append([[2]])
    packets.append([[6]])

    # Sort packets.
    packets = bubble_sort(packets)

    # Find dividers.
    d2_index = -1 # [[2]]
    d6_index = -1 # [[6]]
    for p, packet in enumerate(packets):
        if packet == [[2]]:
            d2_index = p + 1

        elif packet == [[6]]:
            d6_index = p + 1

    print(d2_index * d6_index)


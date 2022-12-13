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

    return len(left) < len(right)

with open("input.txt", "r") as file:
    # Parse file.
    f_pairs = file.read().split("\n\n")
    pairs = []
    for f_pair in f_pairs:
        packets = f_pair.split("\n")
        pairs.append(Pair(eval(packets[0].strip()), eval(packets[1].strip())))

    # Sum of correct pairs.
    sum_ = 0
    for i in range(len(pairs)):
        if is_correct(pairs[i].packet1, pairs[i].packet2):
            print(f"{i + 1}: correct")
            sum_ += i + 1
    print(sum_)


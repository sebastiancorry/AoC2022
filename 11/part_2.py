class Monkey:
    activity = 0

    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test

monkeys = [
        Monkey([54, 98, 50, 94, 69, 62, 53, 85],\
                lambda x: x * 13,\
                lambda x: 2 if (x % 3 == 0) else 1),
        Monkey([71, 55, 82],\
                lambda x: x + 2,\
                lambda x: 7 if (x % 13 == 0) else 2),
        Monkey([77, 73, 86, 72, 87],\
                lambda x: x + 8,\
                lambda x: 4 if (x % 19 == 0) else 7),
        Monkey([97, 91],\
                lambda x: x + 1,\
                lambda x: 6 if (x % 17 == 0) else 5),
        Monkey([78, 97, 51, 85, 66, 63, 62],\
                lambda x: x * 17,\
                lambda x: 6 if (x % 5 == 0) else 3),
        Monkey([88],\
                lambda x: x + 3,\
                lambda x: 1 if (x % 7 == 0) else 0),
        Monkey([87, 57, 63, 86, 87, 53],\
                lambda x: x * x,\
                lambda x: 5 if (x % 11 == 0) else 0),
        Monkey([73, 59, 82, 65],\
                lambda x: x + 6,\
                lambda x: 4 if (x % 2 == 0) else 3)
        ]

def round(monkeys):
    for m in range(len(monkeys)):
        monkey = monkeys[m]
        while len(monkeys[m].items) > 0:
            i = monkey.operation(monkeys[m].items.pop(0))
            i = i % (3 * 13 * 19 * 17 * 5 * 7 * 11 * 2)

            monkeys[monkey.test(i)].items.append(i)
            monkeys[m].activity += 1

    return monkeys

for r in range(10000):
    monkeys = round(monkeys)

a = [m.activity for m in monkeys]
a.sort(reverse=True)
print(a[0] * a[1])


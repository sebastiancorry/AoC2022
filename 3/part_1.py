file = open("./input.txt", "r")

sum = 0

for line in file:
    compart_1, compart_2 = line[:len(line)//2], line[len(line)//2:] # Split the line in half as two lists.

    common_item = list(set(compart_1) & set(compart_2))[0] # Find the common item by the intersection of lists converted to sets.

    sum += (ord(common_item.lower()) - 96) if not common_item.isupper() else (ord(common_item.lower()) - 96 + 26) # Use ord() to find alphabetical position of the item, add 26 if it is capitalized.

print(sum)
file.close()

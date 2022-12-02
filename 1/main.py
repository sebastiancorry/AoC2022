# Open the file containing elf calories.
file = open('./input.txt', 'r')

# Elf inventory variable (treated as mutable).
inventories = []

# Used to keep track of which elf inventory is being summed.
count = -1;

# Iterate through file.
for line in file:
    if len(line.strip()) == 0: # If the line is empty, start a new elf inventory.
        inventories.append(0)
        count += 1; # Increment the count var to account for new elf inventory.
    else:
        inventories[count] += + int(line) # Sum contents of elf inventory.

# Sort the inventory list in reverse to get the highest calorie inventories
inventories.sort(reverse = True)

# Pt. 1
print(inventories[0]) # Print the absolute highest calorie inventory.

# Pt. 2
print(inventories[0] + inventories[1] + inventories[2]) # Prints sum of top 3.


sum = 0

with open("./input.txt", "r") as file:
    for i in range(100): # 100 is determined by the file length / 3.
        lines = []
        for i in range(3): # Grab 3 lines.
            line = file.readline()
            if line == "":
                break
            lines.append(list(line.strip())) # String -> list of chars.

        common_item = list(set(lines[0]) & set(lines[1]) & set(lines[2]))[0] # Find the common item using set intersection.
        sum += (ord(common_item.lower()) - 96) if not common_item.isupper() else (ord(common_item.lower()) - 96 + 26) #Use ord() to find alphabetical position and add 26 if the letter is uppercase.

print(sum)

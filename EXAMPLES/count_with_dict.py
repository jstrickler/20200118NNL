#!/usr/bin/python3

counts = {}
with open("../DATA/breakfast.txt") as breakfast_in:
    for line in breakfast_in:
        print(counts)
        breakfast_item = line.rstrip()
        if breakfast_item in counts: # if key is in dict
            counts[breakfast_item] = counts[breakfast_item] + 1  # increment value
            # counts[breakfast_item] += 1
        else:
            counts[breakfast_item] = 1

for item, count in counts.items():
    print(item,count)

print()
print(counts.items())

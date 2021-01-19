i = 0
while i < 3:
    print(i)
    i += 1
print("Done")

while True:
    item = input("What item (or q)? ")
    if item == 'q':
        break  # exit loop
    if item == '':
        print("Please enter an item")
        continue
    raw_count = input("How many? ")
    if raw_count == '':
        print("Please enter the count as a number")
        continue  # go to top
    count = float(raw_count)
    print("Adding {} {}".format(count, item))
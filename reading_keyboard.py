

item = input("Please enter item: ")
raw_count = input("How many would you like: ")
try:
    count = int(raw_count)
except ValueError as err:
    print("Please enter a number")
else:
    print("OK, that's {} {}(s)".format(count, item))


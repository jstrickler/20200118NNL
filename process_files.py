import sys

print(sys.argv)
print()

for file_name in sys.argv[1:]:  # start with sys.argv[1]
    print("reading", file_name)
    with open(file_name) as file_in:
        for raw_line in file_in:
            line = raw_line.rstrip()  # stripping \n optional
            # do something with line ...

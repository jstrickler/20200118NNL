import sys
from sys import argv

print(len(sys.argv), type(sys.argv))

print(sys.argv)

print(argv)

if len(sys.argv) >= 3:
    print(sys.argv[0])  # script name
    print(sys.argv[1])  # 1st argument
    print(sys.argv[2])  # 2nd argument
else:
    print("Please specify two arguments")


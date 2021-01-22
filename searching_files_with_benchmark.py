import re
import timeit  # benchmark module

setup = """
import re
pattern = r"\b\w{10,}\b"
"""

code1 = """
with open('DATA/alice.txt') as alice_in:
    # 1. read line-by-line
    # 2. read entire file
    contents = alice_in.read()
    #                             string to search
    for m in re.finditer(pattern, contents):
        print(m.group())
"""

code2 = """
with open('DATA/alice.txt') as alice_in:
    # 1. read line-by-line
    # 2. read entire file
    for line in alice_in:
        for m in re.finditer(pattern, line):
            print(m.group())
"""

for code in code1, code2:
    t = timeit.Timer(code, setup)
    print(t.timeit(100))
    print()

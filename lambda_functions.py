
def spam():
    return 100

x = spam()
print(x)

eggs = lambda: 200  # not a good practice...
x = eggs()
print(x)

print(type(spam), type(eggs))
print(type(lambda: None))

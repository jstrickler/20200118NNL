import typing as T

def get_message():
    return "Hello, NNL world"

m = get_message()
print(m)

def shout_message():
    msg = get_message()
    print(msg.upper())

r = shout_message()
print(r)

# def c2f():
#     # convert c to f here
#     return c

def spam(x, y):
    print("x: {}\n".format(x))
    print("y: {}\n".format(y))


spam(1, 2) # args 1, 2 are copied to params x, y
spam('ham', 'toast')


Number = T.Union[int, float]

def eggs(a: Number, b: Number) -> Number:
    return a * b

print(eggs(5, 10))
print(eggs('a', 5))
print(eggs(98.6, 100.92))

#result: int

result = eggs(8, 9.1)




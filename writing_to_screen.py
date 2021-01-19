
name = "John Smith"

value = 27.3 / 3.91

print(name)    # print(str(name) + end)
print(value)   # print(str(value) + end)

print(name, value)   # print(str(name) + sep + str(value) + end)
print()

a = 1
b = 2
c = 3
print(a, b, c, sep='/')
print(a, b, c, sep='')
print(a, b, c, sep=', ')

print(a)
print(b)
print(c)
print()

print(a, end=' ')
# if ....
print(b, end=' ')
print(c)

print(name, value)
print("{} {}".format(name, value))
print("{} {:.1f}".format(name, value))
# {:.3f}  {:5d} {:05d} {:10s}  {:>10s}

print("{}\u00B0 below zero".format(5))

v1 = 25
v2 = 300
v3 = 4
print("{:4d} {:4d} {:4d}".format(v1, v2, v3))
print("{:04d} {:04d} {:04d}".format(v1, v2, v3))

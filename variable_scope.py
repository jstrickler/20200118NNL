x = 100  # global

if x > 50:
    name = 'Fred'

def spam():
    x = "Wolverine" # local
    y = "wombat"   # local
    print(x, y)
    return y

m = spam()
print(name)
print(m)
print(x)


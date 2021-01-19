fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

nums = [800,80,1000,32,255,400,5,5000]

print(len(fruits), len(nums))
print(min(fruits), max(fruits), min(nums), max(nums), sum(nums))
print(sorted(fruits))
print(sorted(nums))

colors = ['red', 'blue', 'green', 'purple', 'orange', 'mauve', 'brown', 'white', 'black', 'yellow']

for color in reversed(colors):
    print(color, end=' ')
print('\n')

r = reversed(colors)
print(r)
for color in r:
    print(color)
print()

print("2nd loop:")
for color in r:
    print(color)
print()

for num, color in zip(nums, colors):
    print(num, color)
print()

print(list(zip(nums, colors)), '\n')

for color in colors:
    print(color)
print()

for i, color in enumerate(colors):
    print(i, color)
print()

print(list(enumerate(colors)))

e = enumerate(colors)
print(e)

for i, color in e:
    print(i, color)
print()

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
a = 'foo'
b = 'bar'
c = a + b
print(c)

print('-' * 60)
print([True] * 10)
print([1, 2, 3] * 5)

x = [0] * 25
print(x)

i = 0
while i < 5:
    print(i)
    i += 1
print()

for i in range(5):
    print(i)
print()

# range(STOP) range(START, STOP)  range(START, STOP, STEP)
for i in range(1, 11):
    print(i, end=' ')
print('\n')

for i in range(5, 101, 5):
    print(i, end=' ')
print('\n')


import sys
from pprint import pprint

list1 = list()  # empty list
list2 = ['a', 'b', 'c']  # initialized list
list3 = []  # empty list

list4 = list(list2)
#  list(ITERABLE)
# listx = list2   # NOT A COPY,  but an ALIAS

#  () -- call/define function/class,  force precedence
#  {} -- literal dict, literal set
#  [] -- literal list, index list/tuple/dict
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [1, 'a', 5.9, None, ['wombat', 'gorilla']]

cities = ['Pittsburgh', 'Albany', 'Schenectady', 'Boston']
print(cities)
print(cities[0], cities[3])
print(cities[-1])
cities.append('Sewickley')
cities.append('Rochester')
cities.append('Saratoga Springs')
print(cities)
cities.insert(0, "McKeesport")
cities.insert(3, 'Confluence')
print(cities)
cities[3] = "Homestead"
print(cities)
#  LIST.append(object) LIST.insert(position, object) LIST.extend(iterable)

more_cities = ['Greenburg', 'Troy', 'Amsterdam']

cities.extend(more_cities)

print(cities, '\n')

nested = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [10, 20, 30]
]
print(nested[0])
print(nested[2])
print(nested[2][2])
print(nested[1][0])
print(nested)
pprint(nested)

print(cities)
del cities[5]  # del obj
print(cities)

c = cities.pop()  # remove last element and return it
print(c)
print(cities)
c = cities.pop(4)  # remove fifth element and return it
print(c)
print(cities)

cities.remove('Homestead')
print(cities)


# del LIST[x]  LIST.pop() LIST.pop(x) LIST.remove(value)

colors = ['purple', 'orange']   # create list object and assign name 'colors' to the object
c2 = colors  # assign 'c2' to same list object
c3 = list(colors)  # create copy of colors and assign 'c3' to new object

print(cities)

print(cities[0:3])
print(cities[:3])
print(cities[2:5])
print(cities[2:7])
print(cities[2:])
print(cities[5:])
print(cities[-3:])

actor = "Chris Hemsworth"
print(actor[:5], actor[6:], actor[3:5])
print()

for city in cities:
    # city = next element of cities
    print(city)
print()

# for VAR ... in ITERABLE:
#     code ...

# ITERABLES: str list tuple dict set bytes generator

for color in 'red', 'blue', 'purple':
    print(color.upper())
print()

for arg in sys.argv[1:]:
    print("processing", arg)

data = [
    [(0, 1), [(11, 100), (12, 101), (13, 98)]],
    [(0, 2), [(11, 102), (12, 101), (13, 98)]],
    [(1, 3), [(11, 104), (12, 101), (13, 98)]],
    [(4, 5), [(11, 97), (12, 101), (13, 98)]],
    [(8, 6), [(11, 99), (12, 102), (13, 98)]],
]

for point in data:
    print(point[0], point[1])

#  numpy  (numeric arrays)
#  scipy?  (stats and other analysis)
#  pandas  (general data munging)
#  matplotlib  (visualization)
#    -- seaborn
#  scikit-learn (machine learning)
#  ipython/jupyter

























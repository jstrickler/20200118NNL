fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date"]

f1 = sorted(fruits)
print("f1: {}\n".format(f1))

def ignore_case(fruit):
    return fruit.lower()

print(ignore_case('WOMBATS Forever!'), '\n')

f2 = sorted(fruits, key=ignore_case)
print("f2: {}\n".format(f2))

f3 = sorted(fruits, key=len)
print("f3: {}\n".format(f3))

def len_and_name(f):  # named function
    return len(f), f.lower()

f4 = sorted(fruits, key=len_and_name)
print("f4: {}\n".format(f4))

f4x = sorted(fruits, key=lambda f: (len(f), f.lower()))  # anonymous or inline function
print("f4x: {}\n".format(f4x))

# lambda params ...: return-value


def wacky(x):
    return x[-1], x[-2]

f5 = sorted(fruits, key=wacky)
print("f5: {}\n".format(f5))

nums = [800,80,1000,32,255,400,5,5000]

n1 = sorted(nums)
print("n1: {}\n".format(n1))

n2 = sorted(nums, key=str)
print("n2: {}\n".format(n2))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print()

def by_dob(p):
    return p[3]  # or p[-1]

for person in sorted(people, key=by_dob, reverse=True):
    print(person)
print()

def by_lname_product(p):
    return p[1], p[2]

for person in sorted(people, key=by_lname_product):
    print(person)
print()

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

for code, name in sorted(airports.items()):
    print(code, name)
print()

print(airports.items())

def by_value(item):
    return item[1], item[0]

for code, name in sorted(airports.items(), key=by_value):
    print(code, name)
print()

for code, name in sorted(airports.items(), key=lambda a: (a[1], a[0])):
    print(code, name)
print()

def visible_sorted(iterable, pastafazool):
    sortable_list = []
    for original_item in iterable:
        result = pastafazool(original_item)
        sortable_list.append((result, original_item))

    sorted_list = sorted(sortable_list)
    print(sortable_list)
    print(sorted_list)
    return [x[1] for x in sorted_list]

def my_key(item):
    print("In my_key(): item is", item)
    return item.lower()

data = ["RED", "Blue", "GREEN", 'yellow', 'Pink']

print(visible_sorted(data, my_key))

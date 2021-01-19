
"""
struct person {
    char *first_name;
    char *last_name;
    int age;
}
"""

person = 'Bill', 'Gates', 'Microsoft', '1955-10-24'

print(person[0], person[1])

# iterable unpacking
#  var1, var2, ... = iterable

first_name, last_name, product, dob = person

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
    ('John', 'Strickler', '1956-10-31'),
]
print(people[0])
print(people[0][0])
print()

for person in people:
    print(person[0], person[1])
print()

# for person in people:
#     first_name, last_name, product, dob = person
#     print(first_name, last_name)
# print()

for first_name, *last_name, product, dob in people:
    print(first_name, last_name, product, dob)
print()

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)


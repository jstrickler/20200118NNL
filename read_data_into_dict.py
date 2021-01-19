from pprint import pprint
knight_data = {}
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data)
print()

#    key   value
#    name  tuple of data
for name, info in knight_data.items():
    print(info[0], name)
print()

print(knight_data['Lancelot'])
print(knight_data['Lancelot'][1])
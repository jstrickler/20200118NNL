d1 = dict()  # empty dict
d2 = {'red': 5, 'purple': 2, 'orange': 9}
d3 = {}  # empty dict

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

print(airports['RDU'])
print(airports['ABQ'])
print(airports.get('ALB'))
print(airports.get('ALB', "NOT FOUND"))
print(())

for code in 'RDU', 'PIT', 'ALB', 'LAX', 'IAD':
    print(code, end=' ')
    if code in airports:
        print('YES')
    else:
        print('NO')

del airports['MCO']
print(airports)

more_airports = {
    'MCO': 'Disney World',
    'PIT': 'Pittsburgh',
    'ALB': 'Albany',
}

airports.update(more_airports)
print(airports)

airports['LAX'] = 'Los Angeles'
print(airports)

print(airports.items(), '\n')
for code, name in sorted(airports.items()):
    print(code, name)
print()

for thing in sorted(airports.items()):
    print(thing)
print()
print("thing:", thing)

for code in airports:
    print(code)
print()



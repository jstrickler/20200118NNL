file_obj = open('DATA/mary.txt')
file_obj.close()

file_obj = open('c:/users/administrator/desktop/py3intro/DATA/mary.txt')
file_obj.close()

# with EXPR:
# with EXPR as VAR:
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print("Normal:")
    print(contents)
    print("Raw:")
    print(repr(contents))
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    all_lines_without_nl = contents.splitlines()   # contents.split(',')
    print(all_lines_without_nl)
print('-' * 60)

with open('DATA/knights.txt') as knights_in:
    with open('titlename.txt', 'w') as titlename_out:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            print('{} {} "{}"'.format(title, name, color))
            titlename_out.write("{}\t{}\n".format(title, name))

with open('cities.txt', 'w') as cities_out:
    for city in 'Albany', 'Rotterdam', 'Colonie', 'Munhall', 'Homestead', 'Pittsburg':
        cities_out.write(city + '\n')

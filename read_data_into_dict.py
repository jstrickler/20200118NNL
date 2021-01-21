from pprint import pprint

FILE_NAME = 'DATA/knights.txt'

def main():
    data = read_data(FILE_NAME)
    pretty_print(data)
    print_names_and_titles(data)

    print(get_field(data, 'Lancelot', 3))
    print(get_field(data, 'Arthur', 1))

def read_data(file_name):
    knight_data = {}
    with open(file_name) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight_data[name] = title, color, quest, comment

    return knight_data

def pretty_print(data):
    pprint(data)
    print()

#    key   value
#    name  tuple of data
def print_names_and_titles(data):
    for name, info in data.items():
        print(info[0], name)

def get_field(data, knight, field_number):
    return data[knight][field_number]

main()
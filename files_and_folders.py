import os   # includes os.path
from datetime import datetime

FOLDER = "DATA"

for name in 'alice.txt', 'parrot.txt', 'betty.txt', 'wombat.txt', 'pastafazool.txt', 'words.txt':
    file_path = os.path.join(FOLDER, name)
    print(file_path, os.path.exists(file_path))
print()

FILE_NAME = 'alice.txt'

file_path = os.path.join(FOLDER, FILE_NAME)
print("file_path: {}\n".format(file_path))

file_size = os.path.getsize(file_path)
print("file_size: {}\n".format(file_size))

base_name = os.path.basename(file_path)
print("base_name: {}\n".format(base_name))

dir_name = os.path.dirname(file_path)
print("dir_name: {}\n".format(dir_name))

abs_path = os.path.abspath(file_path)
print("abs_path: {}\n".format(abs_path))

for item in os.listdir(FOLDER):
    if item.endswith('txt'):
        file_path = os.path.join(FOLDER, item)
        file_size = os.path.getsize(file_path)
        raw_file_time = os.path.getmtime(file_path)
        file_time = datetime.fromtimestamp(raw_file_time)
        print("{:8d} {} {}".format(file_size, file_time, file_path))
print('-' * 60)

file_name = "c:/spam/ham/toast/wombats.dat"
print(os.path.splitext(file_name))

print(dir(os.path))

print(os.getcwd())





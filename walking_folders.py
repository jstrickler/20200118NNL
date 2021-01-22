import os

target = '.'

for curr_dir, dirs, files in os.walk(target):
    if '.git' in dirs:
        dirs.remove('.git')
    print(curr_dir)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            print("{:8d} {}".format(file_size, file_name))
print()

x = os.walk(target)
print(x)


file_name = 'DATA/pastafazool.txt'

try:
    with open(file_name) as pf_in:
        pass
except (FileNotFoundError, PermissionError) as err:
    print(err)
    print(type(err))
    # log error, print message, etc.
except Exception as err:
    print(err)

values = [1, 5, 19, 8, 7, 3]
print(len(values))
print(values[2], values[5])

index = 10

try:
    print(values[index])
except IndexError as err:
    print(err)

values = [0, 7.2, 9.6, 4.8, 0.0, 3.7]

for v in values:
    try:
        result = 22 / v
    except ZeroDivisionError as err:
        print(err)
    else:
        print(result)
    finally:
        print("FINALLY")











print("End of program")

s1 = "spam\n"   # \n newline
s2 = 'spam\n'   # same as s1
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"  # RAW string

print("Guido's the BDFL of Python")
print('Guido is the "BDFL" of Python')
print("Guido is the \"BDFL\" of Python")
print("""Guido's the "BDFL" of Python""")
print('''Guido's the "BDFL" of Python''')

query = """
select *
from test_run
where date == '2020-01-11'
"""

def spam():
    """
    Spread evil in the world
    :return: Ha ha HA HA HA HA
    """
    pass  # successfully do nothing


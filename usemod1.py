import sys

from wombat.calc import utils

utils.spam()
utils.ham()

# utils._eggs()   very bad juju -- don't do it

# PYTHONPATH

# current_dir + PYTHONPATH dirs + builtin

for path in sys.path:
    print(path)

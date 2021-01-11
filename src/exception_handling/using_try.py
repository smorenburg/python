import sys
import random

try:
    print(f'Received argument {sys.argv[1]}')
    args = sys.argv
    random.shuffle(args)
    print(f'Random argument {args[0]}')
except (IndexError, KeyError) as err:
    print(f'Error: no arguments, please provide at least one ({err})')
except NameError as err:
    print(f'Error: random module not loaded ({err})')
else:
    print('else is running')
finally:
    print('finally is running')

import sys

try:
    name = sys.argv[1]
except IndexError:
    print(f'Error: please provide a name and a repeat count to the script')
    sys.exit(1)

try:
    repeat_count = int(sys.argv[2])
except IndexError:
    print(f'Error: please provide a name and a repeat count to the script')
    sys.exit(1)
except ValueError:
    print(f'The repeat count needs to be an integer')
    sys.exit(1)

try:
    f = open('root_files/name_repeated.txt', 'w')
except (OSError, IOError) as err:
    print(f"Error: unable to write file ({err})")
    for i in range(1, repeat_count + 1):
        print(f'{i} - {name}')
else:
    names = [name + '\n' for i in range(1, repeat_count + 1)]
    f.writelines(names)
    f.close()

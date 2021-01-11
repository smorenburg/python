import sys

from .errors import ArgumentError


def main():
    if len(sys.argv) < 2:
        raise ArgumentError('not enough arguments')
    # assert len(sys.argv) >= 2, 'not enough arguments'
    print(f'Name is {sys.argv[1]}')

#!/usr/bin/env python3

name = input('What is your name? ')

if len(name) >= 6:
    print('Your name is long')
elif len(name) == 5:
    print('Your name is five characters')
elif len(name) >= 4:
    print('Your name is four characters')
else:
    print('Your name is short')

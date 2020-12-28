#!/usr/bin/env python3

def split_name(name):
    first_name, last_name = name.split(maxsplit=1)
    return {
        'first_name': first_name,
        'last_name': last_name
    }


assert split_name('Robin Smorenburg') == {
    'first_name': 'Robin',
    'last_name': 'Smorenburg'
}

assert split_name('Victor de Haas') == {
    'first_name': 'Victor',
    'last_name': 'de Haas'
}


def is_palindrome(item):
    item = str(item)
    return item == item[::-1]


assert is_palindrome('radar') == True
assert is_palindrome('stop') == False

assert is_palindrome(101) == True
assert is_palindrome(10) == False


def build_list(item, count=1):
    items = []
    for _ in range(count):
        items.append(item)
    return items


assert build_list('Apple', 3) == [
    'Apple',
    'Apple',
    'Apple'
]

assert build_list('Orange') == [
    'Orange'
]

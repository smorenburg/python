def has_even_number(lst):
    """
    >>> has_even_number([1, 3, 5])
    False
    >>> has_even_number([1, 2, 3])
    True
    """
    has_even = False

    for num in lst:
        if num % 2 == 0:
            has_even = True
            break

    return has_even

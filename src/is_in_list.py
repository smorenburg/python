def is_in_list(num, lst):
    """
    >>> is_in_list(5, [1, 2, 3, 4])
    False
    >>> is_in_list(5, [1, 5, 6])
    True
    """
    in_list = False

    for item in lst:
        if num == item:
            in_list = True
            break

    return in_list

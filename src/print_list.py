def print_list_for_loop(lst):
    """
    >>> print_list_for_loop([1, 2, 3, 4])
    1
    2
    3
    4
    """
    for item in lst:
        print(item)


def print_list_while_loop(lst):
    """
    >>> print_list_while_loop([1, 2, 3, 4])
    1
    2
    3
    4
    """
    index = 0

    while index < len(lst):
        print(lst[index])
        index += 1

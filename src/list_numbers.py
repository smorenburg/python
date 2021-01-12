def list_numbers(num):
    """
    >>> list_numbers(5)
    [0, 1, 2, 3, 4, 5]
    >>> list_numbers(0)
    [0]
    """
    index = 0
    lst = []

    while index <= num:
        lst.append(index)
        index += 1

    return lst

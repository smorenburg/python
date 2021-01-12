def generate_list(start, end, step):
    """
    >>> generate_list(0, 5, 1)
    [0, 1, 2, 3, 4]
    >>> generate_list(0, 0, 1)
    []
    >>> generate_list(5, 10, 2)
    [5, 7, 9]
    >>> generate_list(10, 5, -2)
    [10, 8, 6]
    """
    index = start
    lst = []

    if index < end:
        while index < end:
            lst.append(index)
            index += step
    else:
        while index > end:
            lst.append(index)
            index += step

    return lst

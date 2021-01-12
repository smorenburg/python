def generate_list(start, stop, step):
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
    idx = start
    lst = []

    if idx < stop:
        while idx < stop:
            lst.append(idx)
            idx += step
    else:
        while idx > stop:
            lst.append(idx)
            idx += step

    return lst


def generate_list_range(start, stop, step):
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
    return list(range(start, stop, step))

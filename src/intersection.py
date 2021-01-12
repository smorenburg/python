def intersection(lst1, lst2):
    """
    >>> intersection([1, 2, 3], [2, 4, 6])
    [2]
    >>> intersection([1, 2, 3], [4, 5, 6])
    []
    >>> intersection([2, 3, 2, 4], [2, 2, 4])
    [2, 4]
    """
    in_both = []

    for item1 in lst1:
        for item2 in lst2:
            if item1 == item2 and item2 not in in_both:
                in_both.append(item2)

    return in_both

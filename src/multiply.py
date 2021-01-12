def multiply(a, b):
    """
    >>> multiply(3, 5)
    15
    >>> multiply(-4, 5)
    -20
    >>> multiply(-4, -2)
    8
    """
    iterator = 0
    value = 0

    if iterator < a:
        while iterator < a:
            value += b
            iterator += 1
    else:
        while iterator > a:
            value -= b
            iterator -= 1

    return value

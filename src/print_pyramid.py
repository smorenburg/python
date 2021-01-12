def print_pyramid(num):
    """
    >>> print_pyramid(5)
    o
    oo
    ooo
    oooo
    ooooo
    >>> print_pyramid(3)
    o
    oo
    ooo
    """
    for num in range(num):
        line = 'o'

        for num in range(num):
            line += 'o'

        print(line)

def is_prime(number):
    """
    >>> is_prime(3)
    True
    >>> is_prime(90)
    False
    >>> is_prime(67)
    True
    """
    if number <= 1:
        return False

    for i in range(2, number - 1):
        if number % i == 0:
            return False

    return True


def prime_numbers(number):
    """
    >>> prime_numbers(5)
    2
    3
    5
    7
    11
    >>> prime_numbers(7)
    2
    3
    5
    7
    11
    13
    17
    """
    pointer = 0
    moving_pointer = 0

    while pointer < number:
        if is_prime(moving_pointer):
            print(moving_pointer)
            pointer += 1
        moving_pointer += 1

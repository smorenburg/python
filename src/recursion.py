def func_r(a):
    print(f'Start: {str(a)}')
    res = 0
    if a == 0:
        res = 0
    else:
        res = func_r(a - 1) + 1
    print(f'End: {str(a)}')
    return res


# f(0) = f(1) = f(n) = f(n - 1) + F(n - 2)
def fib(num):
    """
    >>> fib(5)
    5
    >>> fib(0)
    0
    >>> fib(10)
    55
    >>> fib(20)
    6765
    """
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


def reverse(string):
    """
    >>> reverse('Robin')
    'niboR'
    """
    if len(string) < 2:
        return string
    else:
        return reverse(string[1:]) + string[0]


def print_list(lst):
    """
    >>> print_list([1, 2, 3, 4, 5])
    1
    2
    3
    4
    5
    """
    if not lst:
        return
    else:
        print(lst[0])
        print_list(lst[1:])


def is_increasing(lst):
    """
    >>> is_increasing([1, 2, 3, 4])
    True
    >>> is_increasing([1, 3, 2, 4])
    False
    """
    if not lst:
        return False
    elif len(lst) == 1:
        return True
    elif lst[1] > lst[0]:
        return is_increasing(lst[1:])
    else:
        return False


def filter_gt_num(lst, num):
    """
    >>> filter_gt_num([1, 2, 3, 4], 2)
    [3, 4]
    >>> filter_gt_num([2, 2, 3, 3], 1)
    [2, 2, 3, 3]
    >>> filter_gt_num([2, 2, 3, 3], 4)
    []
    """
    if not lst:
        return []
    elif lst[0] > num:
        return [lst[0]] + filter_gt_num(lst[1:], num)
    else:
        return filter_gt_num(lst[1:], num)


def is_in_list(num, lst):
    """
    >>> is_in_list(4, [1, 2, 3, 4, 5])
    True
    >>> is_in_list(6, [1, 2, 3, 4, 5])
    False
    >>> is_in_list(5, [5, 4, 3, 2, 1])
    True
    """
    if not lst:
        return False
    else:
        return lst[0] == num or is_in_list(num, lst[1:])


def intersection(lst1, lst2):
    """
    >>> intersection([1, 2, 3], [2, 4, 6])
    [2]
    >>> intersection([1, 2, 3], [4, 5, 6])
    []
    >>> intersection([2, 3, 2, 4], [2, 2, 4])
    [2, 4]
    """
    if lst1 == []:
        return []
    if is_in_list(lst1[0], intersection(lst1[1:], lst2)):
        return intersection(lst1[1:], lst2)
    if is_in_list(lst1[0], lst2):
        return [lst1[0]] + intersection(lst1[1:], lst2)
    else:
        return intersection(lst1[1:], lst2)

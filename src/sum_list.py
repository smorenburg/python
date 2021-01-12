def sum_list(nums):
    """
    >>> sum_list([1, 2, 3])
    6
    >>> sum_list([10, 200, 33, 55])
    298
    """
    idx = 0
    total = 0

    while idx < len(nums):
        total += nums[idx]
        idx += 1

    return total

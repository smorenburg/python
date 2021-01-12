def sum_list(nums):
    """
    >>> sum_list([1, 2, 3])
    6
    >>> sum_list([10, 200, 33, 55])
    298
    """
    index = 0
    total = 0

    while index < len(nums):
        total += nums[index]
        index += 1

    return total

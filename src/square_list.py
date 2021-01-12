def square_list(nums):
    """
    >>> square_list([1, 2, 3])
    [1, 4, 9]
    """
    idx = 0

    while idx < len(nums):
        nums[idx] = nums[idx] * nums[idx]
        idx += 1

    return nums

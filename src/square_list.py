def square_list(nums):
    """
    >>> square_list([1, 2, 3])
    [1, 4, 9]
    """
    index = 0

    while index < len(nums):
        nums[index] = nums[index] * nums[index]
        index += 1

    return nums

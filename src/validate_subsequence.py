def validate_subsequence_for_loop(array, sequence):
    """
    >>> array = [5, 1, 22, 25, 6, -1, 8, 10]
    >>> sequence = [1, 6, -1, 10]
    >>> validate_subsequence_for_loop(array, sequence)
    True
    >>> array = [5, 1, 22, 25, 6, -1, 8, 10]
    >>> sequence = [1, 6, 2, 10]
    >>> validate_subsequence_for_loop(array, sequence)
    False
    """
    seq_point = 0

    for value in array:
        if seq_point == len(sequence):
            break
        if sequence[seq_point] == value:
            seq_point += 1

    return seq_point == len(sequence)


def validate_subsequence_while_loop(array, sequence):
    """
    >>> array = [5, 1, 22, 25, 6, -1, 8, 10]
    >>> sequence = [1, 6, -1, 10]
    >>> validate_subsequence_for_loop(array, sequence)
    True
    >>> array = [5, 1, 22, 25, 6, -1, 8, 10]
    >>> sequence = [1, 6, 2, 10]
    >>> validate_subsequence_for_loop(array, sequence)
    False
    """
    arr_point = 0
    seq_point = 0

    while arr_point < len(array) and seq_point < len(sequence):
        if array[arr_point] == sequence[seq_point]:
            seq_point += 1
        arr_point += 1

    return seq_point == len(sequence)

def validate_subsequence_for_loop(arr, seq):
    """
    >>> arr = [5, 1, 22, 25, 6, -1, 8, 10]
    >>> seq = [1, 6, -1, 10]
    >>> validate_subsequence_for_loop(arr, seq)
    True
    >>> arr = [5, 1, 22, 25, 6, -1, 8, 10]
    >>> seq = [1, 6, 2, 10]
    >>> validate_subsequence_for_loop(arr, seq)
    False
    """
    seq_idx = 0

    for item in arr:
        if seq_idx == len(seq):
            break
        if seq[seq_idx] == item:
            seq_idx += 1

    return seq_idx == len(seq)


def validate_subsequence_while_loop(arr, seq):
    """
    >>> arr = [5, 1, 22, 25, 6, -1, 8, 10]
    >>> seq = [1, 6, -1, 10]
    >>> validate_subsequence_for_loop(arr, seq)
    True
    >>> arr = [5, 1, 22, 25, 6, -1, 8, 10]
    >>> seq = [1, 6, 2, 10]
    >>> validate_subsequence_for_loop(arr, seq)
    False
    """
    arr_idx = 0
    seq_idx = 0

    while arr_idx < len(arr) and seq_idx < len(seq):
        if arr[arr_idx] == seq[seq_idx]:
            seq_idx += 1
        arr_idx += 1

    return seq_idx == len(seq)

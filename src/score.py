def score(total, correct, wrong):
    """
    >>> score(20, 20, 0)
    100.0
    >>> score(20, 15, 0)
    75.0
    >>> score(20, 15, 5)
    87.5
    >>> score(20, 10, 5)
    62.5
    >>> score(20, 0, 20)
    50.0
    """
    correct_value = 2
    return (
        (correct * correct_value + wrong) /
        (total * correct_value)
    ) * 100


def score75(total, correct, wrong):
    """
    >>> score75(20, 20, 0)
    100.0
    >>> score75(20, 15, 0)
    100.0
    >>> score75(20, 15, 5)
    100.0
    >>> score75(20, 10, 5)
    83.33333333333334
    >>> score75(20, 0, 20)
    50.0
    """
    return (
        min(max(total * 0.75 - correct, 0), wrong) +
        (2 * min(total * 0.75, correct))
    ) / (2 * total * 0.75) * 100

__all__ = ['extract_upper']


def extract_upper(phrase):
    """
    extract_upper takes a string and returns a list containing
    only the uppercase characters from the string.

    >>> extract_upper('Hello there, Bob')
    ['H', 'B']
    """
    return list(filter(str.isupper, phrase))


def extract_lower(phrase):
    return list(filter(str.islower, phrase))

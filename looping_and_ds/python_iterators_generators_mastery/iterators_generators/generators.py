"""
Generator function utilities.
"""


def generate_numbers(limit: int):
    """
    Yields numbers from 1 up to the given limit.

    Parameters
    ----------
    limit : int
        Maximum number to generate.

    Yields
    ------
    int
        Numbers from 1 to limit.
    """
    for number in range(1, limit + 1):
        yield number


def generate_even_numbers(limit: int):
    """
    Yields even numbers from 1 up to the given limit.

    Parameters
    ----------
    limit : int
        Maximum number to check.

    Yields
    ------
    int
        Even numbers up to the limit.
    """
    for number in range(1, limit + 1):
        if number % 2 == 0:
            yield number
"""
Generator expression utilities.
"""


def build_square_generator(numbers: list[int]):
    """
    Returns a generator expression that yields squared values.

    Parameters
    ----------
    numbers : list[int]
        Input numbers.

    Returns
    -------
    generator
        Generator expression of squared numbers.
    """
    return (number ** 2 for number in numbers)


def build_even_generator(numbers: list[int]):
    """
    Returns a generator expression that yields only even numbers.

    Parameters
    ----------
    numbers : list[int]
        Input numbers.

    Returns
    -------
    generator
        Generator expression of even numbers.
    """
    return (number for number in numbers if number % 2 == 0)
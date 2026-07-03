"""
List comprehension utilities.
"""


def get_even_numbers(numbers: list[int]) -> list[int]:
    """
    Returns only even numbers using list comprehension.

    Parameters
    ----------
    numbers : list[int]
        Input list of integers.

    Returns
    -------
    list[int]
        Even numbers from the input list.
    """
    return [number for number in numbers if number % 2 == 0]


def get_squared_numbers(numbers: list[int]) -> list[int]:
    """
    Returns squared values using list comprehension.

    Parameters
    ----------
    numbers : list[int]
        Input list of integers.

    Returns
    -------
    list[int]
        Squared numbers.
    """
    return [number ** 2 for number in numbers]
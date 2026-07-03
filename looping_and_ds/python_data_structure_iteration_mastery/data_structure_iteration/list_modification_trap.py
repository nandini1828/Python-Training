"""
List modification trap demonstration.
"""


def remove_even_numbers_unsafely(numbers: list[int]) -> list[int]:
    """
    Demonstrates the list modification trap by removing even numbers
    while iterating over the same list.

    Note:
    This function is intentionally unsafe for learning purposes.

    Parameters
    ----------
    numbers : list[int]
        Input list.

    Returns
    -------
    list[int]
        Mutated list after unsafe removal.
    """
    for number in numbers:
        if number % 2 == 0:
            numbers.remove(number)

    return numbers


def remove_even_numbers_safely(numbers: list[int]) -> list[int]:
    """
    Safely removes even numbers using list comprehension.

    Parameters
    ----------
    numbers : list[int]
        Input list.

    Returns
    -------
    list[int]
        List containing only odd numbers.
    """
    return [number for number in numbers if number % 2 != 0]
"""
utils.py

Utility functions demonstrating pass statement usage.
"""


def process_positive_numbers(numbers: list[int]) -> list[int]:
    """
    Return only positive numbers.
    Negative numbers are ignored using pass.
    """
    result = []

    for num in numbers:
        if num < 0:
            pass
        else:
            result.append(num)

    return result


def find_first_positive(numbers: list[int]) -> int | None:
    """
    Return first positive number.
    Uses pass for non-positive values.
    """
    for num in numbers:
        if num <= 0:
            pass
        else:
            return num

    return None


def placeholder_function() -> str:
    """
    Example of pass used as placeholder.
    """
    pass
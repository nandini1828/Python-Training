"""
break and continue examples.
"""


def find_first_even(numbers: list[int]) -> int | None:
    """
    Returns the first even number using break logic.
    Returns None if no even number is found.
    """
    for number in numbers:
        if number % 2 == 0:
            return number

    return None


def skip_even_numbers(numbers: list[int]) -> list[int]:
    """
    Returns only odd numbers by skipping even numbers using continue.
    """
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            continue

        odd_numbers.append(number)

    return odd_numbers
"""
utils.py

Reusable utility functions demonstrating Python's range() function.
"""


def create_range(stop: int) -> list[int]:
    """
    Return numbers from 0 to stop - 1.
    """
    return list(range(stop))


def create_range_with_start(start: int, stop: int) -> list[int]:
    """
    Return numbers from start to stop - 1.
    """
    return list(range(start, stop))


def create_range_with_step(start: int, stop: int, step: int) -> list[int]:
    """
    Return numbers using a custom step value.
    """
    if step == 0:
        raise ValueError("Step cannot be zero.")

    return list(range(start, stop, step))


def reverse_range(start: int, stop: int) -> list[int]:
    """
    Return a reverse range sequence.
    """
    return list(range(start, stop, -1))


def even_numbers(limit: int) -> list[int]:
    """
    Return all even numbers up to the given limit.
    """
    return list(range(2, limit + 1, 2))


def odd_numbers(limit: int) -> list[int]:
    """
    Return all odd numbers up to the given limit.
    """
    return list(range(1, limit + 1, 2))


def multiplication_table(number: int) -> list[str]:
    """
    Return the multiplication table of a number.
    """
    return [
        f"{number} x {value} = {number * value}"
        for value in range(1, 11)
    ]


def sum_first_n(n: int) -> int:
    """
    Return the sum of the first n natural numbers.
    """
    return sum(range(1, n + 1))


def square_numbers(limit: int) -> list[int]:
    """
    Return squares from 1² to limit².
    """
    return [number ** 2 for number in range(1, limit + 1)]


def alphabet_positions() -> dict[int, str]:
    """
    Return alphabet positions mapped to uppercase letters.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return {
        index: alphabet[index]
        for index in range(len(alphabet))
    }
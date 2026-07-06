"""
Examples demonstrating Python list comprehensions.

Topics covered:

- Basic list comprehensions
- Conditional comprehensions
- Multiple transformations
- Nested comprehensions
- Matrix flattening

Author: Python Training
"""

from __future__ import annotations


def square_numbers(numbers: list[int]) -> list[int]:
    """
    Return the square of every number.

    Args:
        numbers:
            Input numbers.

    Returns:
        Squared numbers.
    """
    return [number**2 for number in numbers]


def even_numbers(numbers: list[int]) -> list[int]:
    """
    Return only even numbers.

    Args:
        numbers:
            Input numbers.

    Returns:
        Even numbers.
    """
    return [
        number
        for number in numbers
        if number % 2 == 0
    ]


def odd_numbers(numbers: list[int]) -> list[int]:
    """
    Return only odd numbers.

    Args:
        numbers:
            Input numbers.

    Returns:
        Odd numbers.
    """
    return [
        number
        for number in numbers
        if number % 2 != 0
    ]


def uppercase_words(words: list[str]) -> list[str]:
    """
    Convert every word to uppercase.

    Args:
        words:
            Input words.

    Returns:
        Uppercase words.
    """
    return [word.upper() for word in words]


def lowercase_words(words: list[str]) -> list[str]:
    """
    Convert every word to lowercase.

    Args:
        words:
            Input words.

    Returns:
        Lowercase words.
    """
    return [word.lower() for word in words]


def filter_long_words(
    words: list[str],
    minimum_length: int = 5,
) -> list[str]:
    """
    Keep words longer than the given length.

    Args:
        words:
            Input words.

        minimum_length:
            Minimum allowed length.

    Returns:
        Filtered words.
    """
    return [
        word
        for word in words
        if len(word) >= minimum_length
    ]


def word_lengths(words: list[str]) -> list[int]:
    """
    Return the length of every word.

    Args:
        words:
            Input words.

    Returns:
        Word lengths.
    """
    return [len(word) for word in words]


def remove_none(
    values: list[object | None],
) -> list[object]:
    """
    Remove None values.

    Args:
        values:
            Input values.

    Returns:
        Values without None.
    """
    return [
        value
        for value in values
        if value is not None
    ]


def flatten_matrix(
    matrix: list[list[int]],
) -> list[int]:
    """
    Flatten a two-dimensional list.

    Args:
        matrix:
            Matrix.

    Returns:
        Flattened list.
    """
    return [
        value
        for row in matrix
        for value in row
    ]


def multiplication_table(number: int) -> list[int]:
    """
    Build a multiplication table.

    Args:
        number:
            Input number.

    Returns:
        Multiplication results.
    """
    return [
        number * value
        for value in range(1, 11)
    ]


__all__ = [
    "square_numbers",
    "even_numbers",
    "odd_numbers",
    "uppercase_words",
    "lowercase_words",
    "filter_long_words",
    "word_lengths",
    "remove_none",
    "flatten_matrix",
    "multiplication_table",
]
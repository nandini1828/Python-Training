"""Examples of list comprehensions."""

from typing import List


def even_numbers(values: List[int]) -> List[int]:
    """Return the even values from a list."""
    return [value for value in values if value % 2 == 0]


def uppercase_words(words: List[str]) -> List[str]:
    """Return uppercase versions of the words."""
    return [word.upper() for word in words]

"""List iteration helpers."""

from typing import List, Tuple


def first_and_last(items: List[int]) -> Tuple[int, int]:
    """Return the first and last values from a list."""
    return items[0], items[-1]


def middle_slice(items: List[int], start: int, end: int) -> List[int]:
    """Return a slice of the list."""
    return items[start:end]


def iterate_with_index(items: List[str]) -> List[Tuple[int, str]]:
    """Return index/value pairs while iterating."""
    return [(index, value) for index, value in enumerate(items)]

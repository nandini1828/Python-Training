"""Helpers for working with range objects."""

from typing import List


def generate_range(start: int, stop: int | None = None, step: int = 1) -> List[int]:
    """Return a list from a range expression."""
    if stop is None:
        stop = start
        start = 0
    return list(range(start, stop, step))

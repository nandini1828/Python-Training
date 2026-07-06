"""Examples that demonstrate generator functions."""

from __future__ import annotations


def count_up_to(limit: int) -> object:
    """Yield values from 0 up to but not including the limit.

    Args:
        limit: The exclusive upper bound.

    Yields:
        Increasing integers.
    """
    current = 0
    while current < limit:
        yield current
        current += 1

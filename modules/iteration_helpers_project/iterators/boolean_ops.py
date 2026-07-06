"""Boolean helpers using any() and all()."""

from typing import Iterable


def has_any_true(values: Iterable[bool]) -> bool:
    """Return True if any value is truthy."""
    return any(values)


def has_all_true(values: Iterable[bool]) -> bool:
    """Return True if all values are truthy."""
    return all(values)

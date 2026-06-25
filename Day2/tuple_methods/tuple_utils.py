"""
==================================================
Module: Tuple Utilities
Topic: Tuple Methods

Description:
Provides utility functions for manipulating
tuple objects.
==================================================
"""

from __future__ import annotations

from typing import Dict, Generic, Hashable, Sequence, Tuple, TypeVar

K = TypeVar("K", bound=Hashable)
V = TypeVar("V", bound=Hashable)
T = TypeVar("T")


class TupleMethods(Generic[T]):
    """A beginner-friendly wrapper around common tuple operations."""

    def __init__(self, items: Sequence[T] | None = None) -> None:
        self.items = tuple(items or ())

    def first_item(self) -> T | None:
        return self.items[0] if self.items else None

    def last_item(self) -> T | None:
        return self.items[-1] if self.items else None

    def count_value(self, value: T) -> int:
        return self.items.count(value)

    def as_list(self) -> list[T]:
        return list(self.items)


def access_first_item(values: Tuple[T, ...]) -> T | None:
    """Return the first item in a tuple."""
    return values[0] if values else None


def access_last_item(values: Tuple[T, ...]) -> T | None:
    """Return the last item in a tuple."""
    return values[-1] if values else None


def count_occurrences(values: Tuple[int, ...], target: int) -> int:
    """Count how many times a value appears in a tuple."""
    return values.count(target)


def convert_to_list(values: Tuple[T, ...]) -> list[T]:
    """Convert a tuple to a list."""
    return list(values)


def count_items(values: Tuple[T, ...], target: T) -> int:
    """Count how many times a value appears in a tuple."""
    return values.count(target)


def index_of(values: Tuple[T, ...], target: T) -> int:
    """Return the position of a value in a tuple."""
    return values.index(target)


def tuple_to_dict(keys: Tuple[K, ...], values: Tuple[V, ...]) -> Dict[K, V]:
    """Build a dictionary from aligned key and value tuples."""

    if len(keys) != len(values):
        raise ValueError("keys and values must have the same length")
    return dict(zip(keys, values))

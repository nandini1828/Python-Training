"""
==================================================
Module: Set Utilities
Topic: Set Methods

Description:
Provides utility functions for manipulating
set objects.
==================================================
"""

from __future__ import annotations

from typing import Generic, Iterable, Set, TypeVar

T = TypeVar("T")


class SetMethods(Generic[T]):
    """A beginner-friendly wrapper around common set operations."""

    def __init__(self, items: Iterable[T] | None = None) -> None:
        self.items = set(items or [])

    def add_item(self, item: T) -> set[T]:
        self.items.add(item)
        return set(self.items)

    def remove_item(self, item: T) -> set[T]:
        self.items.discard(item)
        return set(self.items)

    def union_with(self, other: Iterable[T]) -> set[T]:
        return self.items.union(other)

    def intersection_with(self, other: Iterable[T]) -> set[T]:
        return self.items.intersection(other)


def add_item(values: Set[T], item: T) -> None:
    """Add an item to a set."""
    values.add(item)


def remove_item(values: Set[T], item: T) -> None:
    """Remove an item from a set."""
    values.discard(item)


def union_sets(left: Set[T], right: Set[T]) -> Set[T]:
    """Return a set containing all unique values from both sets."""
    return left.union(right)


def intersection_sets(left: Set[T], right: Set[T]) -> Set[T]:
    """Return values that appear in both sets."""
    return left.intersection(right)


def difference_sets(left: Set[T], right: Set[T]) -> Set[T]:
    """Return values in the first set but not in the second."""
    return left.difference(right)


def is_subset(left: Set[T], right: Set[T]) -> bool:
    """Return True if the first set is a subset of the second."""
    return left.issubset(right)


def is_superset(left: Set[T], right: Set[T]) -> bool:
    """Return True if the first set is a superset of the second."""
    return left.issuperset(right)


def unique_items(values: Iterable[T]) -> Set[T]:
    """Return unique values from an iterable."""

    return set(values)


def common_elements(left: Set[T], right: Set[T]) -> Set[T]:
    """Return the shared values between two sets."""

    return left.intersection(right)


def symmetric_difference(left: Set[T], right: Set[T]) -> Set[T]:
    """Return values that appear in exactly one of the two sets."""

    return left.symmetric_difference(right)

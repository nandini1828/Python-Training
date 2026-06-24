from __future__ import annotations

from typing import Iterable, Set, TypeVar

T = TypeVar("T")


def unique_items(values: Iterable[T]) -> Set[T]:
    """Return unique values from an iterable."""

    return set(values)


def common_elements(left: Set[T], right: Set[T]) -> Set[T]:
    """Return the shared values between two sets."""

    return left.intersection(right)


def symmetric_difference(left: Set[T], right: Set[T]) -> Set[T]:
    """Return values that appear in exactly one of the two sets."""

    return left.symmetric_difference(right)

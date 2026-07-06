"""Helpers for reversing iterables."""

from typing import Iterable, List, TypeVar

T = TypeVar("T")


def reverse_items(items: Iterable[T]) -> List[T]:
    """Return a reversed list of items."""
    return list(reversed(list(items)))

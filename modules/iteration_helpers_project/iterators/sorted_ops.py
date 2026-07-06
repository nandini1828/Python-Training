"""Helpers for sorting iterables."""

from typing import Iterable, List, TypeVar

T = TypeVar("T")


def sort_items(items: Iterable[T]) -> List[T]:
    """Return a sorted list of items."""
    return sorted(items)

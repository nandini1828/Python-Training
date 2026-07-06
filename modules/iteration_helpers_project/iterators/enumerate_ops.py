"""Helpers for enumerating iterables."""

from typing import Iterable, List, Tuple, TypeVar

T = TypeVar("T")


def enumerate_items(items: Iterable[T]) -> List[Tuple[int, T]]:
    """Return a list of index/value pairs."""
    return list(enumerate(items))

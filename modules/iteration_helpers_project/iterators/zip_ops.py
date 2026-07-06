"""Helpers for zipping iterables together."""

from typing import Iterable, List, Tuple, TypeVar

T = TypeVar("T")
U = TypeVar("U")


def zip_items(left: Iterable[T], right: Iterable[U]) -> List[Tuple[T, U]]:
    """Combine two iterables element-wise."""
    return list(zip(left, right))

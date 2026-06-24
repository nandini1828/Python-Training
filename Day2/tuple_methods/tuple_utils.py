from __future__ import annotations

from typing import Dict, Hashable, Tuple, TypeVar

K = TypeVar("K", bound=Hashable)
V = TypeVar("V", bound=Hashable)


def tuple_to_dict(keys: Tuple[K, ...], values: Tuple[V, ...]) -> Dict[K, V]:
    """Build a dictionary from aligned key and value tuples."""

    if len(keys) != len(values):
        raise ValueError("keys and values must have the same length")
    return dict(zip(keys, values))


def count_occurrences(values: Tuple[int, ...], target: int) -> int:
    """Count how many times a value appears in a tuple."""

    return values.count(target)

"""
Tuple utilities and explanation of immutability.
"""
from __future__ import annotations

from typing import Any, Tuple


def tuple_count(t: Tuple[Any, ...], item: Any) -> int:
    """Return the count of `item` in the tuple."""
    return t.count(item)


def tuple_index(t: Tuple[Any, ...], item: Any) -> int:
    """Return the index of `item` in the tuple or raise `ValueError`."""
    return t.index(item)


def demo_tuple_methods(t: Tuple[Any, ...]) -> dict:
    """Return a small demo summary explaining immutability and methods."""
    return {
        "count": tuple_count(t, t[0]) if t else 0,
        "index": tuple_index(t, t[0]) if t else -1,
        "note": "Tuples are immutable: methods don't modify in-place",
    }

"""
Utilities showcasing common list methods.
"""
from __future__ import annotations

from typing import Any, List, Sequence


def append_item(original: List[Any], item: Any) -> List[Any]:
    """
    Append an item to a copy of `original` and return the new list.

    Args:
        original: Source list.
        item: Item to append.

    Returns:
        A new list with `item` appended.
    """
    result = original.copy()
    result.append(item)
    return result


def extend_list(original: List[Any], extra: Sequence[Any]) -> List[Any]:
    """Return a new list after extending with `extra`."""
    result = original.copy()
    result.extend(extra)
    return result


def insert_item(original: List[Any], index: int, item: Any) -> List[Any]:
    """Insert `item` at `index` and return the modified copy."""
    result = original.copy()
    result.insert(index, item)
    return result


def remove_item(original: List[Any], item: Any) -> List[Any]:
    """Remove first occurrence of `item` from a copy and return it."""
    result = original.copy()
    result.remove(item)
    return result


def pop_item(original: List[Any], index: int = -1) -> Any:
    """Pop and return item at `index` from a copy of the list."""
    result = original.copy()
    return result.pop(index)


def clear_list() -> List[Any]:
    """Return an empty list (demonstrates `clear`)."""
    temp = [1, 2, 3]
    temp.clear()
    return temp


def index_of(original: List[Any], item: Any) -> int:
    """Return index of `item` in list or raise `ValueError`."""
    return original.index(item)


def count_of(original: List[Any], item: Any) -> int:
    """Return count of `item` in the list."""
    return original.count(item)


def sort_copy(original: List[Any]) -> List[Any]:
    """Return a sorted copy of `original`."""
    result = original.copy()
    result.sort()
    return result


def reverse_copy(original: List[Any]) -> List[Any]:
    """Return a reversed copy of `original`."""
    result = original.copy()
    result.reverse()
    return result


def copy_list(original: List[Any]) -> List[Any]:
    """Return a shallow copy of the list."""
    return original.copy()


def demo_list_methods(base: List[Any], extra: Sequence[Any]) -> dict:
    """Run a small demo of list methods returning a summary dict."""
    return {
        "append": append_item(base, "X"),
        "extend": extend_list(base, extra),
        "insert": insert_item(base, 0, "Y"),
        "pop": pop_item(base),
        "clear": clear_list(),
        "count": count_of(base, base[0]) if base else 0,
        "sorted": sort_copy(base),
        "reversed": reverse_copy(base),
        "copy": copy_list(base),
    }

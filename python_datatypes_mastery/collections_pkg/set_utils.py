"""
Set utilities demonstrating set operations.
"""
from __future__ import annotations

from typing import Any, Iterable, Set, Tuple, Dict


def add_item(original: Set[Any], item: Any) -> Set[Any]:
    """Return a copy with `item` added."""
    s = set(original)
    s.add(item)
    return s


def remove_item(original: Set[Any], item: Any) -> Set[Any]:
    """Remove `item` using `remove` on copy (raises if missing)."""
    s = set(original)
    s.remove(item)
    return s


def discard_item(original: Set[Any], item: Any) -> Set[Any]:
    """Discard `item` (no error if missing) and return copy."""
    s = set(original)
    s.discard(item)
    return s


def pop_any(original: Set[Any]) -> Tuple[Any, Set[Any]]:
    """Pop and return the popped element and the remaining set."""
    s = set(original)
    popped = s.pop()
    return popped, s


def clear_set(original: Set[Any]) -> Set[Any]:
    """Return an empty set to demonstrate `clear`."""
    s = set(original)
    s.clear()
    return s


def binary_ops(a: Set[Any], b: Set[Any]) -> Dict[str, Set[Any]]:
    """Return union, intersection, difference, symmetric_difference."""
    return {
        "union": a.union(b),
        "intersection": a.intersection(b),
        "difference": a.difference(b),
        "symmetric_difference": a.symmetric_difference(b),
    }


def relations(a: Set[Any], b: Set[Any]) -> Dict[str, bool]:
    """Return subset/superset/disjoint relations."""
    return {
        "issubset": a.issubset(b),
        "issuperset": a.issuperset(b),
        "isdisjoint": a.isdisjoint(b),
    }


def demo_set_methods(a: Set[Any], b: Set[Any]) -> Dict[str, Any]:
    """Return a small summary of set operations."""
    return {
        "add": add_item(a, "new"),
        "discard": discard_item(a, "missing"),
        "pop": pop_any(a)[0] if a else None,
        "binary": binary_ops(a, b),
        "relations": relations(a, b),
    }

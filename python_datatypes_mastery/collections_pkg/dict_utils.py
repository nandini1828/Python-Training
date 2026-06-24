"""
Dictionary utilities demonstrating common dict methods.
"""
from __future__ import annotations

from typing import Any, Dict, Iterable, Tuple


def get_with_default(mapping: Dict[Any, Any], key: Any, default: Any = None) -> Any:
    """Return `mapping.get(key, default)` and demonstrate `get`."""
    return mapping.get(key, default)


def set_default(mapping: Dict[Any, Any], key: Any, default: Any = None) -> Any:
    """Call `setdefault` and return the updated mapping value."""
    return mapping.setdefault(key, default)


def keys_values_items(mapping: Dict[Any, Any]) -> Tuple[Iterable[Any], Iterable[Any], Iterable[Tuple[Any, Any]]]:
    """Return keys, values, and items iterables from the mapping."""
    return mapping.keys(), mapping.values(), mapping.items()


def update_mapping(mapping: Dict[Any, Any], other: Dict[Any, Any]) -> Dict[Any, Any]:
    """Return a new mapping that is the update of `mapping` with `other`."""
    new_map = mapping.copy()
    new_map.update(other)
    return new_map


def pop_key(mapping: Dict[Any, Any], key: Any, default: Any = None) -> Any:
    """Pop `key` from a copy of mapping and return the popped value."""
    new_map = mapping.copy()
    return new_map.pop(key, default)


def pop_any_item(mapping: Dict[Any, Any]) -> Tuple[Any, Any]:
    """Pop an arbitrary item from a copy and return it."""
    new_map = mapping.copy()
    return new_map.popitem()


def clear_copy(mapping: Dict[Any, Any]) -> Dict[Any, Any]:
    """Return an empty mapping (demonstrates clear)."""
    temp = mapping.copy()
    temp.clear()
    return temp


def from_keys(iterable, value=None) -> Dict[Any, Any]:
    """Create a dict from keys with the same `value` using `fromkeys`."""
    return dict.fromkeys(iterable, value)


def demo_dict_methods(a: Dict[Any, Any], b: Dict[Any, Any]) -> Dict[str, Any]:
    """Return a demo summary of dict operations."""
    return {
        "get": get_with_default(a, "missing", "default"),
        "setdefault": set_default(a.copy(), "z", 0),
        "keys": list(keys_values_items(a)[0]),
        "update": update_mapping(a, b),
        "pop": pop_key(a, next(iter(a)) if a else None),
        "popitem": pop_any_item({"x": 1}),
        "fromkeys": from_keys(["a", "b"], 0),
    }

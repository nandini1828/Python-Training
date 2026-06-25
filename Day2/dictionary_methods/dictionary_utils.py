"""
==================================================
Module: Dictionary Utilities
Topic: Dictionary Methods

Description:
Provides utility functions for manipulating
dictionary objects.
==================================================
"""

from __future__ import annotations

from collections import defaultdict
from typing import Callable, Dict, Generic, Hashable, Mapping, TypeVar

K = TypeVar("K", bound=Hashable)
V = TypeVar("V")


class DictionaryMethods(Generic[K, V]):
    """A beginner-friendly wrapper around common dictionary operations."""

    def __init__(self, data: Mapping[K, V] | None = None) -> None:
        self.data = dict(data or {})

    def get_value(self, key: K, default: V | None = None) -> V | None:
        return self.data.get(key, default)

    def add_item(self, key: K, value: V) -> dict[K, V]:
        self.data[key] = value
        return self.data

    def keys(self) -> list[K]:
        return list(self.data.keys())

    def values(self) -> list[V]:
        return list(self.data.values())

    def items(self) -> list[tuple[K, V]]:
        return list(self.data.items())


def add_item(mapping: Dict[K, V], key: K, value: V) -> None:
    """Add a key-value pair to a dictionary."""
    mapping[key] = value


def get_value(mapping: Dict[K, V], key: K, default: V | None = None) -> V | None:
    """Return the value for a key, or a default if the key is missing."""
    return mapping.get(key, default)


def remove_item(mapping: Dict[K, V], key: K) -> None:
    """Remove a key from a dictionary."""
    mapping.pop(key, None)


def update_dictionary(mapping: Dict[K, V], new_items: Mapping[K, V]) -> None:
    """Add several new key-value pairs."""
    mapping.update(new_items)


def get_keys(mapping: Dict[K, V]) -> list[K]:
    """Return all keys as a list."""
    return list(mapping.keys())


def get_values(mapping: Dict[K, V]) -> list[V]:
    """Return all values as a list."""
    return list(mapping.values())


def get_items(mapping: Dict[K, V]) -> list[tuple[K, V]]:
    """Return all items as a list of tuples."""
    return list(mapping.items())


def has_key(mapping: Dict[K, V], key: K) -> bool:
    """Check whether a key exists in the dictionary."""
    return key in mapping


def clear_mapping(mapping: Dict[K, V]) -> None:
    """Remove all items from the dictionary."""
    mapping.clear()


def merge_dictionaries(left: Mapping[K, V], right: Mapping[K, V]) -> Dict[K, V]:
    """Merge two dictionaries into a new dictionary."""

    merged: Dict[K, V] = dict(left)
    merged.update(right)
    return merged


def invert_mapping(mapping: Mapping[K, V]) -> Dict[V, list[K]]:
    """Invert a mapping so values map to lists of keys."""

    inverted: Dict[V, list[K]] = defaultdict(list)
    for key, value in mapping.items():
        inverted[value].append(key)
    return dict(inverted)


def filter_by_value(mapping: Mapping[K, V], predicate: Callable[[V], bool]) -> Dict[K, V]:
    """Return the subset of mapping values that satisfy the predicate."""

    return {key: value for key, value in mapping.items() if predicate(value)}

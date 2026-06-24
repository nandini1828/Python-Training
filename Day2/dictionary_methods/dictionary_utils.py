from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable, Dict, Hashable, Mapping, TypeVar

K = TypeVar("K", bound=Hashable)
V = TypeVar("V")


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

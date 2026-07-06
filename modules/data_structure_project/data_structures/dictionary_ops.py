"""Dictionary iteration helpers."""

from typing import Dict, List, Tuple, TypeVar

K = TypeVar("K")
V = TypeVar("V")


def collect_keys(mapping: Dict[K, V]) -> List[K]:
    """Return all keys from a dictionary."""
    return list(mapping.keys())


def collect_values(mapping: Dict[K, V]) -> List[V]:
    """Return all values from a dictionary."""
    return list(mapping.values())


def collect_items(mapping: Dict[K, V]) -> List[Tuple[K, V]]:
    """Return all key/value pairs from a dictionary."""
    return list(mapping.items())

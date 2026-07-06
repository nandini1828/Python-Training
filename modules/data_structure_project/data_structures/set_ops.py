"""Set helpers demonstrating membership and uniqueness."""

from typing import List, Set, TypeVar

T = TypeVar("T")


def create_unique_collection(values: List[T]) -> Set[T]:
    """Return a set containing only unique values."""
    return set(values)


def contains_value(values: Set[T], target: T) -> bool:
    """Check if a target exists in the set quickly."""
    return target in values

from __future__ import annotations

from typing import List, Sequence, TypeVar

T = TypeVar("T")


def find_duplicates(values: Sequence[T]) -> List[T]:
    """Return duplicate values in a deterministic order."""

    seen: set[T] = set()
    duplicates: list[T] = []
    for value in values:
        if value in seen:
            if value not in duplicates:
                duplicates.append(value)
        else:
            seen.add(value)
    return duplicates


def chunk_list(values: Sequence[T], size: int) -> List[list[T]]:
    """Split a sequence into evenly sized chunks."""

    if size <= 0:
        raise ValueError("size must be greater than zero")
    return [list(values[index:index + size]) for index in range(0, len(values), size)]


def average_values(values: Sequence[float]) -> float:
    """Calculate the arithmetic mean of a numeric sequence."""

    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)

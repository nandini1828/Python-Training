"""
==================================================
Module: List Utilities
Topic: List Methods

Description:
Provides utility functions for manipulating
list objects.
==================================================
"""

from __future__ import annotations

from typing import Generic, List, Sequence, TypeVar

T = TypeVar("T")


class ListMethods(Generic[T]):
    """A beginner-friendly wrapper around common list operations."""

    def __init__(self, items: Sequence[T] | None = None) -> None:
        self.items = list(items or [])

    def add_item(self, item: T) -> list[T]:
        self.items.append(item)
        return self.items

    def remove_item(self, item: T) -> list[T]:
        if item in self.items:
            self.items.remove(item)
        return self.items

    def sort_items(self) -> list[T]:
        return sorted(self.items)

    def get_length(self) -> int:
        return len(self.items)

    def get_first(self) -> T | None:
        return self.items[0] if self.items else None

    def get_last(self) -> T | None:
        return self.items[-1] if self.items else None


def add_destination(items: List[str], city: str) -> None:
    """Add a city to the end of the list."""
    items.append(city)


def add_multiple_destinations(items: List[str], cities: List[str]) -> None:
    """Add multiple cities to the list."""
    items.extend(cities)


def insert_destination(items: List[str], position: int, city: str) -> None:
    """Insert a city at a specified position."""
    items.insert(position, city)


def remove_destination(items: List[str], city: str) -> None:
    """Remove a city from the list."""
    items.remove(city)


def remove_last_destination(items: List[str]) -> str:
    """Remove and return the last city."""
    return items.pop()


def reverse_destinations(items: List[str]) -> None:
    """Reverse the list."""
    items.reverse()


def sort_destinations(items: List[str]) -> None:
    """Sort destinations alphabetically."""
    items.sort()


def copy_list(items: List[T]) -> List[T]:
    """Return a copy of the list."""
    return items.copy()


def count_items(items: List[T], value: T) -> int:
    """Count how many times a value appears in a list."""
    return items.count(value)


def clear_list(items: List[T]) -> None:
    """Remove all items from the list."""
    items.clear()


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

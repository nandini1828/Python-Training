"""
storage.py

Reusable helper functions for working with
our in-memory dictionaries.
"""

from typing import TypeVar

# Generic type.
# Allows these functions to work with Product,
# User, Cart, Order, or any other object.
T = TypeVar("T")


def add(storage: dict[str, T], key: str, value: T) -> None:
    """
    Adds an object to storage.
    """
    storage[key] = value


def get(storage: dict[str, T], key: str) -> T | None:
    """
    Returns an object if it exists.
    Otherwise returns None.
    """
    return storage.get(key)


def get_all(storage: dict[str, T]) -> list[T]:
    """
    Returns every stored object.
    """
    return list(storage.values())


def remove(storage: dict[str, T], key: str) -> bool:
    """
    Removes an object from storage.
    """

    if key not in storage:
        return False

    del storage[key]
    return True


def exists(storage: dict[str, T], key: str) -> bool:
    """
    Checks whether an object exists.
    """
    return key in storage
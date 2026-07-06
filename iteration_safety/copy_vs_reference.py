"""
Examples demonstrating copy vs reference.

Topics covered:

- Assignment
- References
- Shallow copy
- Deep copy
- Object identity

Author: Python Training
"""

from __future__ import annotations

import copy
from typing import Any


def demonstrate_reference(
    values: list[int],
) -> tuple[list[int], list[int]]:
    """
    Demonstrate reference assignment.

    Args:
        values:
            Input list.

    Returns:
        Original and referenced list.
    """
    reference = values

    return values, reference


def create_shallow_copy(
    values: list[Any],
) -> list[Any]:
    """
    Create a shallow copy.

    Args:
        values:
            Input list.

    Returns:
        Shallow copy.
    """
    return copy.copy(values)


def create_deep_copy(
    values: list[Any],
) -> list[Any]:
    """
    Create a deep copy.

    Args:
        values:
            Input list.

    Returns:
        Deep copy.
    """
    return copy.deepcopy(values)


def copy_using_slice(
    values: list[Any],
) -> list[Any]:
    """
    Copy using slicing.

    Args:
        values:
            Input list.

    Returns:
        Copied list.
    """
    return values[:]


def copy_using_list(
    values: list[Any],
) -> list[Any]:
    """
    Copy using list().

    Args:
        values:
            Input list.

    Returns:
        Copied list.
    """
    return list(values)


def copy_using_method(
    values: list[Any],
) -> list[Any]:
    """
    Copy using copy().

    Args:
        values:
            Input list.

    Returns:
        Copied list.
    """
    return values.copy()


def object_identity(
    first: Any,
    second: Any,
) -> bool:
    """
    Check object identity.

    Args:
        first:
            First object.

        second:
            Second object.

    Returns:
        True if both refer to the same object.
    """
    return first is second


def object_equality(
    first: Any,
    second: Any,
) -> bool:
    """
    Check object equality.

    Args:
        first:
            First object.

        second:
            Second object.

    Returns:
        Equality result.
    """
    return first == second


__all__ = [
    "demonstrate_reference",
    "create_shallow_copy",
    "create_deep_copy",
    "copy_using_slice",
    "copy_using_list",
    "copy_using_method",
    "object_identity",
    "object_equality",
]
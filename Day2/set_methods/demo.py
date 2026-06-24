from __future__ import annotations

from set_methods.set_utils import common_elements, symmetric_difference, unique_items


def run_set_demo() -> None:
    """Show simple set operations for beginners."""

    fruits = {"apple", "banana"}
    fruits.add("orange")
    fruits.remove("banana")

    print("Set:", fruits)
    print("Unique:", unique_items([1, 1, 2, 3, 3]))
    print("Shared:", common_elements({1, 2, 3}, {2, 3, 4}))
    print("Difference:", symmetric_difference({1, 2, 3}, {3, 4, 5}))

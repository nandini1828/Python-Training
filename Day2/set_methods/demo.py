from __future__ import annotations

from set_methods.set_utils import (
    add_item,
    common_elements,
    difference_sets,
    intersection_sets,
    is_subset,
    is_superset,
    remove_item,
    symmetric_difference,
    unique_items,
    union_sets,
)


def run_set_demo() -> None:
    """Show simple set operations for beginners."""

    fruits = {"apple", "banana"}
    add_item(fruits, "orange")
    remove_item(fruits, "banana")

    print("Set:", fruits)
    print("Unique:", unique_items([1, 1, 2, 3, 3]))
    print("Shared:", common_elements({1, 2, 3}, {2, 3, 4}))
    print("Difference:", symmetric_difference({1, 2, 3}, {3, 4, 5}))
    print("Union:", union_sets({1, 2}, {2, 3}))
    print("Intersection:", intersection_sets({1, 2}, {2, 3}))
    print("Difference set:", difference_sets({1, 2, 3}, {2}))
    print("Is subset:", is_subset({1, 2}, {1, 2, 3}))
    print("Is superset:", is_superset({1, 2, 3}, {1, 2}))

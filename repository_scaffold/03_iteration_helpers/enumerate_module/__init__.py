"""
enumerate_helper

Reusable utilities demonstrating Python's built-in enumerate() function.

Modules
-------
demo
    Practical demonstrations of enumerate().

utils
    Reusable helper functions built using enumerate().
"""

from .utils import (
    create_index_dictionary,
    create_student_records,
    enumerate_characters,
    enumerate_items,
    enumerate_tuple,
    enumerate_with_start,
    even_index_items,
    find_item_index,
    number_lines,
    odd_index_items,
)

__all__ = [
    "enumerate_items",
    "enumerate_with_start",
    "create_index_dictionary",
    "find_item_index",
    "number_lines",
    "enumerate_characters",
    "enumerate_tuple",
    "create_student_records",
    "even_index_items",
    "odd_index_items",
]
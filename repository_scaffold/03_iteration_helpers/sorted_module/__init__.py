"""
sorted_module

Reusable utilities demonstrating Python's built-in sorted() function.

Modules
-------
demo
    Practical demonstrations of sorted().

utils
    Reusable helper functions built using sorted().
"""

from .utils import (
    case_insensitive_sort,
    sort_by_length,
    sort_dictionary_items,
    sort_dictionary_keys,
    sort_numbers,
    sort_numbers_descending,
    sort_set,
    sort_strings,
    sort_students_by_marks,
    sort_tuples,
)

__all__ = [
    "sort_numbers",
    "sort_numbers_descending",
    "sort_strings",
    "sort_by_length",
    "sort_dictionary_keys",
    "sort_dictionary_items",
    "sort_tuples",
    "sort_students_by_marks",
    "case_insensitive_sort",
    "sort_set",
]
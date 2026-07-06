"""
for_loop

A collection of reusable utilities and demonstrations for
Python's for loop.

Modules
-------
demo
    Practical examples demonstrating Python for loops.

utils
    Reusable helper functions built using for loops.
"""

from .utils import (
    count_vowels,
    create_student_dictionary,
    filter_even_numbers,
    find_max,
    find_min,
    multiplication_table,
    print_list,
    reverse_string,
    square_numbers,
    sum_numbers,
)

__all__ = [
    "print_list",
    "sum_numbers",
    "find_max",
    "find_min",
    "count_vowels",
    "multiplication_table",
    "reverse_string",
    "square_numbers",
    "filter_even_numbers",
    "create_student_dictionary",
]
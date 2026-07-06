"""
while_loop

A collection of reusable utilities and demonstrations for
Python's while loop.

Modules
-------
demo
    Practical examples demonstrating while loops.

utils
    Reusable helper functions built using while loops.
"""

from .utils import (
    count_digits,
    count_down,
    count_up,
    countdown,
    factorial,
    find_first_even,
    is_palindrome,
    multiplication_table,
    reverse_string,
    sum_numbers,
)

__all__ = [
    "count_up",
    "count_down",
    "sum_numbers",
    "factorial",
    "multiplication_table",
    "countdown",
    "find_first_even",
    "reverse_string",
    "count_digits",
    "is_palindrome",
]
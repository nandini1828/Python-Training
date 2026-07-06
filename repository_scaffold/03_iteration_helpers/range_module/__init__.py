"""
range_helper

Reusable utilities demonstrating Python's built-in range() function.

Modules
-------
demo
    Practical demonstrations of the range() function.

utils
    Reusable helper functions built using range().
"""

from .utils import (
    cube_numbers,
    even_numbers,
    generate_range,
    generate_range_with_start,
    generate_range_with_step,
    multiplication_table,
    odd_numbers,
    reverse_range,
    squares,
    sum_first_n,
)

__all__ = [
    "generate_range",
    "generate_range_with_start",
    "generate_range_with_step",
    "reverse_range",
    "even_numbers",
    "odd_numbers",
    "multiplication_table",
    "sum_first_n",
    "squares",
    "cube_numbers",
]
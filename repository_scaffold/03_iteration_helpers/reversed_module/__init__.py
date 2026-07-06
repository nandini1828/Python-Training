"""
reversed_module

Reusable utilities demonstrating Python's built-in reversed() function.

Modules
-------
demo
    Practical demonstrations of reversed().

utils
    Reusable helper functions built using reversed().
"""

from .utils import (
    browser_history,
    countdown,
    is_palindrome,
    reverse_keys,
    reverse_lines,
    reverse_list,
    reverse_range,
    reverse_string,
    reverse_tuple,
    reverse_values,
)

__all__ = [
    "reverse_list",
    "reverse_tuple",
    "reverse_string",
    "reverse_range",
    "reverse_lines",
    "reverse_keys",
    "reverse_values",
    "countdown",
    "browser_history",
    "is_palindrome",
]
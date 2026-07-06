"""
any_all

Reusable utilities demonstrating Python's built-in any() and all() functions.

Modules
-------
demo
    Practical demonstrations of any() and all().

utils
    Reusable helper functions built using any() and all().
"""

from .utils import (
    all_even,
    all_passwords_valid,
    all_positive,
    all_truthy,
    any_empty_string,
    any_positive,
    any_text_file,
    any_truthy,
    has_permissions,
    has_required_fields,
)

__all__ = [
    "any_truthy",
    "all_truthy",
    "any_positive",
    "all_positive",
    "all_even",
    "any_empty_string",
    "all_passwords_valid",
    "any_text_file",
    "has_required_fields",
    "has_permissions",
]
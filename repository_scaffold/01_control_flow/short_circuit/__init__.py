"""
short_circuit

A collection of reusable utilities and demonstrations for
Python's Short-Circuit Evaluation.

Modules
-------
demo
    Practical examples demonstrating short-circuit evaluation.

utils
    Reusable helper functions implementing short-circuit logic.
"""

from .utils import (
    authenticate,
    can_access_system,
    cart_has_items,
    get_cached_value,
    get_display_name,
    get_file_content,
    get_user_name,
    load_configuration,
    safe_division,
    validate_age,
)

__all__ = [
    "safe_division",
    "get_display_name",
    "authenticate",
    "get_user_name",
    "load_configuration",
    "cart_has_items",
    "get_file_content",
    "can_access_system",
    "get_cached_value",
    "validate_age",
]
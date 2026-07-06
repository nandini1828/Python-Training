"""
truthy_falsy

A collection of reusable utilities and demonstrations for
Python's Truthy and Falsy concepts.

Modules
-------
demo
    Practical examples demonstrating Truthy and Falsy values.

utils
    Reusable helper functions for boolean evaluation.
"""

from .utils import (
    can_process_file,
    cart_has_items,
    has_content,
    has_records,
    is_empty_dictionary,
    is_empty_list,
    is_empty_set,
    is_empty_string,
    is_falsy,
    is_none,
    is_non_empty_dictionary,
    is_non_empty_list,
    is_non_empty_string,
    is_truthy,
    is_valid_api_response,
    is_valid_password,
    is_valid_username,
    is_zero,
    should_load_default,
)

__all__ = [
    "is_truthy",
    "is_falsy",
    "is_empty_string",
    "is_non_empty_string",
    "is_empty_list",
    "is_non_empty_list",
    "is_empty_dictionary",
    "is_non_empty_dictionary",
    "is_empty_set",
    "is_none",
    "has_content",
    "is_zero",
    "has_records",
    "is_valid_username",
    "is_valid_password",
    "is_valid_api_response",
    "should_load_default",
    "cart_has_items",
    "can_process_file",
]
"""
dictionary_key_protection

Reusable utilities and demonstrations for safe dictionary key access.
"""

from .utils import (
    clear_dictionary,
    filter_by_key,
    get_value_safe,
    key_exists,
    merge_with_override,
    remove_key_safely,
    set_default_value,
    update_dictionary,
)

__all__ = [
    "get_value_safe",
    "set_default_value",
    "update_dictionary",
    "merge_with_override",
    "remove_key_safely",
    "key_exists",
    "filter_by_key",
    "clear_dictionary",
]

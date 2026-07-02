"""
Truthy and Falsy examples.
"""

from typing import Any


def is_truthy(value: Any) -> bool:
    """
    Returns the boolean evaluation of a value.
    """
    return bool(value)


def evaluate_truthy_falsy() -> dict[str, bool]:
    """
    Demonstrates truthy and falsy values in Python.
    """
    return {
        "empty_list": bool([]),
        "empty_dict": bool({}),
        "empty_set": bool(set()),
        "empty_string": bool(""),
        "none_value": bool(None),
        "zero": bool(0),
        "non_empty_list": bool([1, 2]),
        "non_zero_integer": bool(10),
    }
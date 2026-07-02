"""
Short-circuit evaluation examples.
"""

from typing import Any


def get_first_truthy_value(first_value: Any, second_value: Any) -> Any:
    """
    Returns the first truthy value using short-circuit OR logic.
    """
    return first_value or second_value


def safe_division(numerator: int, denominator: int) -> str:
    """
    Demonstrates guarding against invalid conditions before division.
    """
    if denominator != 0 and numerator / denominator >= 0:
        return "Valid division"
    return "Invalid division"
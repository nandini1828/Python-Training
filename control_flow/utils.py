"""
Utility functions for the control_flow module.

This module contains reusable helper functions used throughout the
control_flow package. Keeping these utilities in one place avoids code
duplication and makes the examples easier to read.

Author: Python Training
"""

from __future__ import annotations

from typing import Any, Optional


SECTION_WIDTH = 70


def divider(character: str = "-") -> str:
    """
    Create a horizontal divider.

    Args:
        character:
            Character used to build the divider.

    Returns:
        A divider string.
    """
    return character * SECTION_WIDTH


def banner(title: str) -> str:
    """
    Create a formatted banner.

    Args:
        title:
            Title to display.

    Returns:
        A formatted banner string.
    """
    return (
        f"\n{divider('=')}\n"
        f"{title.upper():^{SECTION_WIDTH}}\n"
        f"{divider('=')}"
    )


def subsection(title: str) -> str:
    """
    Create a formatted subsection heading.

    Args:
        title:
            Subsection title.

    Returns:
        A formatted subsection string.
    """
    return (
        f"\n{divider()}\n"
        f"{title}\n"
        f"{divider()}"
    )


def safe_int(value: str, default: Optional[int] = None) -> Optional[int]:
    """
    Safely convert a string into an integer.

    Args:
        value:
            Value to convert.

        default:
            Value returned if conversion fails.

    Returns:
        Converted integer or default value.
    """
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def safe_float(
    value: str,
    default: Optional[float] = None,
) -> Optional[float]:
    """
    Safely convert a string into a float.

    Args:
        value:
            Value to convert.

        default:
            Value returned if conversion fails.

    Returns:
        Converted float or default value.
    """
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def is_positive(number: int | float) -> bool:
    """
    Determine whether a number is positive.

    Args:
        number:
            Number to evaluate.

    Returns:
        True if the number is positive.
    """
    return number > 0


def is_negative(number: int | float) -> bool:
    """
    Determine whether a number is negative.

    Args:
        number:
            Number to evaluate.

    Returns:
        True if the number is negative.
    """
    return number < 0


def is_zero(number: int | float) -> bool:
    """
    Determine whether a number is zero.

    Args:
        number:
            Number to evaluate.

    Returns:
        True if the number is zero.
    """
    return number == 0


def validate_age(age: int) -> bool:
    """
    Validate a realistic human age.

    Args:
        age:
            Age to validate.

    Returns:
        True if the age is valid.
    """
    return 0 <= age <= 150


def validate_percentage(value: float) -> bool:
    """
    Validate a percentage.

    Args:
        value:
            Percentage value.

    Returns:
        True if between 0 and 100.
    """
    return 0.0 <= value <= 100.0


def stringify(value: Any) -> str:
    """
    Convert any object into a readable string.

    Args:
        value:
            Object to convert.

    Returns:
        String representation.
    """
    return str(value)


def print_banner(title: str) -> None:
    """
    Print a formatted banner.

    Args:
        title:
            Banner title.
    """
    print(banner(title))


def print_subsection(title: str) -> None:
    """
    Print a formatted subsection.

    Args:
        title:
            Subsection title.
    """
    print(subsection(title))


def print_result(description: str, value: Any) -> None:
    """
    Print a formatted key-value result.

    Args:
        description:
            Description label.

        value:
            Result value.
    """
    print(f"{description:<35}: {value}")


def pause() -> None:
    """
    Pause execution until the user presses Enter.

    Useful while demonstrating examples interactively.
    """
    input("\nPress Enter to continue...")


def example_header(example_name: str) -> None:
    """
    Display an example heading.

    Args:
        example_name:
            Name of the example.
    """
    print()
    print(divider())
    print(f"Example: {example_name}")
    print(divider())


def display_collection(title: str, collection: Any) -> None:
    """
    Display a collection in a readable format.

    Args:
        title:
            Collection title.

        collection:
            Collection object.
    """
    print_result(title, collection)


if __name__ == "__main__":
    print_banner("Control Flow Utilities")

    print_result("Divider Length", len(divider()))
    print_result("Safe Integer", safe_int("100"))
    print_result("Invalid Integer", safe_int("abc", default=-1))
    print_result("Safe Float", safe_float("45.8"))
    print_result("Positive", is_positive(10))
    print_result("Negative", is_negative(-5))
    print_result("Zero", is_zero(0))
    print_result("Valid Age", validate_age(25))
    print_result("Percentage", validate_percentage(88.5))
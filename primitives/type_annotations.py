"""
Type Annotation Examples
"""

from typing import Any


def add_numbers(
    first_number: int,
    second_number: int
) -> int:

    return (
        first_number
        + second_number
    )


def get_employee_name(
    employee_id: int
) -> str:

    return (
        f"Employee-{employee_id}"
    )


def safe_cast(
    value: Any,
    target_type: type,
    default: Any = None
) -> Any:

    try:
        return target_type(value)

    except (
        ValueError,
        TypeError
    ):
        return default
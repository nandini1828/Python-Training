"""
Examples demonstrating Python's ternary (conditional) operator.

The ternary operator provides a concise way to choose between two values
based on a condition.

Syntax:
    value_if_true if condition else value_if_false

Topics covered:
- Basic ternary operator
- Nested ternary operator
- Conditional assignments
- Function return values
- Practical enterprise examples

Author: Python Training
"""

from __future__ import annotations


def determine_status(age: int) -> str:
    """
    Determine whether a person is an adult or minor.

    Args:
        age:
            Person's age.

    Returns:
        "Adult" if age is 18 or above, otherwise "Minor".
    """
    return "Adult" if age >= 18 else "Minor"


def absolute_value(number: int | float) -> int | float:
    """
    Return the absolute value of a number.

    Args:
        number:
            Numeric value.

    Returns:
        Absolute value.
    """
    return number if number >= 0 else -number


def maximum(first: int, second: int) -> int:
    """
    Return the larger of two numbers.

    Args:
        first:
            First number.

        second:
            Second number.

    Returns:
        Larger value.
    """
    return first if first > second else second


def minimum(first: int, second: int) -> int:
    """
    Return the smaller of two numbers.

    Args:
        first:
            First number.

        second:
            Second number.

    Returns:
        Smaller value.
    """
    return first if first < second else second


def even_or_odd(number: int) -> str:
    """
    Determine whether a number is even or odd.

    Args:
        number:
            Integer value.

    Returns:
        "Even" or "Odd".
    """
    return "Even" if number % 2 == 0 else "Odd"


def pass_or_fail(score: float) -> str:
    """
    Determine whether a student passes.

    Args:
        score:
            Student score.

    Returns:
        "Pass" or "Fail".
    """
    return "Pass" if score >= 40 else "Fail"


def login_message(is_logged_in: bool) -> str:
    """
    Generate a login message.

    Args:
        is_logged_in:
            Authentication status.

    Returns:
        Appropriate message.
    """
    return "Welcome back!" if is_logged_in else "Please log in."


def shipping_charge(order_amount: float) -> float:
    """
    Calculate shipping charge.

    Orders worth ₹1000 or more qualify for free shipping.

    Args:
        order_amount:
            Order value.

    Returns:
        Shipping charge.
    """
    return 0.0 if order_amount >= 1000 else 99.0


def salary_category(salary: float) -> str:
    """
    Categorize a salary using nested ternary operators.

    Args:
        salary:
            Monthly salary.

    Returns:
        Salary category.
    """
    return (
        "High"
        if salary >= 100_000
        else "Medium"
        if salary >= 50_000
        else "Low"
    )


def grade(score: float) -> str:
    """
    Determine a student's grade.

    Args:
        score:
            Student marks.

    Returns:
        Grade.
    """
    return (
        "A"
        if score >= 90
        else "B"
        if score >= 80
        else "C"
        if score >= 70
        else "D"
        if score >= 60
        else "F"
    )


def discount_percentage(
    is_premium: bool,
) -> int:
    """
    Return customer discount percentage.

    Args:
        is_premium:
            Premium membership status.

    Returns:
        Discount percentage.
    """
    return 20 if is_premium else 5


def safe_username(username: str | None) -> str:
    """
    Return a default username when None or empty.

    Args:
        username:
            Username.

    Returns:
        Username or Guest.
    """
    return username if username else "Guest"


def employee_status(is_active: bool) -> str:
    """
    Determine employee status.

    Args:
        is_active:
            Employee activity status.

    Returns:
        Employee status.
    """
    return "Active" if is_active else "Inactive"


def file_permission(is_admin: bool) -> str:
    """
    Determine file permission.

    Args:
        is_admin:
            Administrative privilege.

    Returns:
        Access level.
    """
    return "Read/Write" if is_admin else "Read Only"


def traffic_signal(color: str) -> str:
    """
    Return the action for a traffic signal.

    Args:
        color:
            Traffic light color.

    Returns:
        Driver action.
    """
    return (
        "Stop"
        if color.lower() == "red"
        else "Go"
        if color.lower() == "green"
        else "Slow Down"
    )


__all__ = [
    "determine_status",
    "absolute_value",
    "maximum",
    "minimum",
    "even_or_odd",
    "pass_or_fail",
    "login_message",
    "shipping_charge",
    "salary_category",
    "grade",
    "discount_percentage",
    "safe_username",
    "employee_status",
    "file_permission",
    "traffic_signal",
]
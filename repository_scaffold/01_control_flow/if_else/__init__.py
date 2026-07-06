"""
if_else

A collection of reusable utilities and demonstrations for
Python's if-elif-else decision-making constructs.

Modules
-------
demo
    Practical examples demonstrating conditional statements.

utils
    Reusable utility functions implementing common decision-making logic.
"""

from .utils import (
    calculate_discount,
    calculate_grade,
    can_vote,
    check_leap_year,
    check_number,
    employee_bonus,
    even_or_odd,
    is_adult,
    largest_number,
    pass_or_fail,
    smallest_number,
    traffic_signal,
    validate_login,
    weather_advice,
)

__all__ = [
    "is_adult",
    "can_vote",
    "calculate_grade",
    "largest_number",
    "smallest_number",
    "check_leap_year",
    "validate_login",
    "calculate_discount",
    "employee_bonus",
    "traffic_signal",
    "weather_advice",
    "check_number",
    "even_or_odd",
    "pass_or_fail",
]
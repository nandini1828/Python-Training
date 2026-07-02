"""
match_case

A collection of reusable utilities and demonstrations for
Python's Structural Pattern Matching (match-case).

Modules
-------
demo
    Practical examples demonstrating match-case.

utils
    Reusable helper functions implementing structural
    pattern matching.
"""

from .utils import (
    age_group,
    calculate,
    classify_point,
    execute_command,
    get_day,
    get_grade_remark,
    get_http_status,
    get_role_permissions,
    list_information,
    student_information,
)

__all__ = [
    "get_day",
    "calculate",
    "get_http_status",
    "get_role_permissions",
    "get_grade_remark",
    "classify_point",
    "list_information",
    "student_information",
    "age_group",
    "execute_command",
]
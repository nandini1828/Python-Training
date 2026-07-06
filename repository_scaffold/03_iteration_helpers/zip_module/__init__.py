"""
zip_helper

Reusable utilities demonstrating Python's built-in zip() function.

Modules
-------
demo
    Practical demonstrations of zip().

utils
    Reusable helper functions built using zip().
"""

from .utils import (
    compare_lists,
    create_dictionary,
    create_employee_records,
    pair_coordinates,
    student_report,
    total_prices,
    unzip_pairs,
    zip_lists,
    zip_three_lists,
    zip_to_indexed_dict,
)

__all__ = [
    "zip_lists",
    "zip_three_lists",
    "create_dictionary",
    "unzip_pairs",
    "compare_lists",
    "create_employee_records",
    "pair_coordinates",
    "student_report",
    "total_prices",
    "zip_to_indexed_dict",
]
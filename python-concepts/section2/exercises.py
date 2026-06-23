"""
Exercise Solutions - Section 2
"""

from .type_casting import safe_cast


def count_truthy_falsy(items):
    """
    Counts truthy and falsy values in a list.
    """

    truthy_count = 0
    falsy_count = 0

    for item in items:

        if item:
            truthy_count += 1

        else:
            falsy_count += 1

    return {
        "truthy": truthy_count,
        "falsy": falsy_count
    }


def safe_conversion_examples():
    """
    Exercise 2.1 test examples.
    """

    return {
        "float_conversion":
            safe_cast("12.5", float),

        "failed_int_conversion":
            safe_cast("12.5", int),

        "default_value":
            safe_cast("abc", int, default=0)
    }
"""
Truthiness module:
Demonstrates how Python evaluates values as True or False.
"""


def is_truthy(value):
    """
    Returns True if value is truthy, otherwise False.
    """
    return bool(value)


def is_falsy(value):
    """
    Returns True if value is falsy, otherwise False.
    """
    return not bool(value)


def count_truthy_falsy(items):
    """
    Counts truthy and falsy values in a list.

    Args:
        items (list): List of values

    Returns:
        dict: {"truthy": int, "falsy": int}
    """

    truthy_count = 0
    falsy_count = 0

    for item in items:
        if bool(item):
            truthy_count += 1
        else:
            falsy_count += 1

    return {
        "truthy": truthy_count,
        "falsy": falsy_count
    }
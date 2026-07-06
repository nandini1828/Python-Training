"""
Utilities for any() and all() operations
"""


def check_any_true(data):
    """
    Returns True if at least one element is True
    """
    return any(data)


def check_all_true(data):
    """
    Returns True if all elements are True
    """
    return all(data)


def any_greater_than(data, value):
    """
    Check if any element is greater than given value
    """
    return any(x > value for x in data)


def all_greater_than(data, value):
    """
    Check if all elements are greater than given value
    """
    return all(x > value for x in data)


def any_even(data):
    """
    Check if any number is even
    """
    return any(x % 2 == 0 for x in data)


def all_even(data):
    """
    Check if all numbers are even
    """
    return all(x % 2 == 0 for x in data)


def any_non_empty(strings):
    """
    Check if any string is non-empty
    """
    return any(strings)


def all_non_empty(strings):
    """
    Check if all strings are non-empty
    """
    return all(strings)


def any_match(data, condition):
    """
    Generic any() using condition function
    """
    return any(condition(x) for x in data)


def all_match(data, condition):
    """
    Generic all() using condition function
    """
    return all(condition(x) for x in data)
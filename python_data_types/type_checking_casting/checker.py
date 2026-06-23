"""
Type Checking Module
- type()
- isinstance()
"""


def check_type(obj, expected_type):
    """
    Strict type check using type()
    """
    return type(obj) == expected_type


def strict_type_check(obj, expected_type):
    """
    Flexible type check using isinstance()
    (supports inheritance)
    """
    return isinstance(obj, expected_type)
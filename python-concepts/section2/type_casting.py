"""
Section 2: Type Checking & Casting
"""


class Animal:
    pass


class Dog(Animal):
    pass


def check_exact_type(obj, expected_type):
    """
    Checks whether object is exactly the specified type.
    """

    return type(obj) == expected_type


def check_instance(obj, expected_type):
    """
    Checks whether object is an instance of a class
    or one of its subclasses.
    """

    return isinstance(obj, expected_type)


def is_truthy(value):
    """
    Returns True if value is truthy.
    """

    return bool(value)


def is_falsy(value):
    """
    Returns not bool(value).
    """

    return not bool(value)


def safe_cast(value, target_type, default=None):
    """
    Safely converts a value to target_type.
    Returns default if conversion fails.
    """

    try:
        return target_type(value)

    except (ValueError, TypeError):
        return default


def demonstrate_casting_examples():
    """
    Demonstrates casting examples mentioned
    in the notes.
    """

    return {
        "int_from_float": int(9.999),
        "int_from_negative_string": int("-5"),
        "float_infinity": float("inf"),
        "float_negative_infinity": float("-inf")
    }
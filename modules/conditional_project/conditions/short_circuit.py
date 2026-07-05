"""
Examples of short-circuit evaluation.
"""


def safe_division(a: int, b: int) -> bool:
    """Avoid ZeroDivisionError."""
    return b != 0 and a / b > 2


def expensive_function() -> bool:
    print("Expensive Function Executed")
    return True


def logical_or(flag: bool) -> bool:
    """Demonstrate OR short-circuit."""
    return flag or expensive_function()


def logical_and(flag: bool) -> bool:
    """Demonstrate AND short-circuit."""
    return flag and expensive_function()
"""
Examples of the ternary operator.
"""


def even_or_odd(number: int) -> str:
    """Return whether the number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"


def maximum(a: int, b: int) -> int:
    """Return the larger number."""
    return a if a > b else b


def discount(member: bool) -> int:
    """Return discount percentage."""
    return 20 if member else 0


def pass_fail(mark: int) -> str:
    """Return Pass or Fail."""
    return "Pass" if mark >= 40 else "Fail"


def age_category(age: int) -> str:
    """Categorize age."""
    return "Adult" if age >= 18 else "Minor"
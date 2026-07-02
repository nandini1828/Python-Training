"""Examples of short-circuit evaluation."""

from __future__ import annotations


def safe_divide(dividend: float, divisor: float) -> tuple[float | None, str]:
    """Divide safely while avoiding a ZeroDivisionError.

    Args:
        dividend: The number to divide.
        divisor: The number to divide by.

    Returns:
        A tuple containing the quotient and an explanation message.
    """
    if divisor == 0:
        return None, "Cannot divide by zero."
    return dividend / divisor, "Division successful."

"""Examples of the ternary operator."""

from __future__ import annotations


def choose_discount(is_member: bool) -> int:
    """Return a discount percentage based on membership.

    Args:
        is_member: Whether the customer has a membership.

    Returns:
        The discount percentage.
    """
    return 20 if is_member else 5

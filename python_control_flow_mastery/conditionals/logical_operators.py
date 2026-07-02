"""Examples that demonstrate logical operators."""

from __future__ import annotations


def check_access(role: str, is_active: bool, has_permission: bool) -> str:
    """Check whether a user should get access.

    Args:
        role: The user's role such as admin or guest.
        is_active: Whether the account is active.
        has_permission: Whether the user has permission.

    Returns:
        An access message.
    """
    if role == "admin" and is_active and has_permission:
        return "Full access granted."
    if role == "guest" or not is_active:
        return "Limited access."
    return "Access denied."

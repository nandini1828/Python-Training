"""Examples that explain truthy and falsy values."""

from __future__ import annotations


def describe_truthiness(value: object) -> str:
    """Return whether an object is truthy or falsy.

    Args:
        value: Any Python object.

    Returns:
        The word ``truthy`` or ``falsy``.
    """
    return "truthy" if value else "falsy"

"""
Type Casting Module
- safe conversion using try/except
"""


def safe_cast(value, target_type, default=None):
    """
    Safely converts value to target_type.

    If conversion fails → returns default.
    """

    try:
        return target_type(value)
    except (ValueError, TypeError):
        return default
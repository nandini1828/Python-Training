"""
Safe casting utilities.

Provides `safe_cast` which attempts conversions with graceful fallbacks.
"""
from __future__ import annotations

from typing import Any, Callable, Optional, Type
import collections.abc


def safe_cast(value: Any, target_type: Type, default: Optional[Any] = None) -> Any:
    """
    Attempt to cast `value` to `target_type` and return `default` on failure.

    Args:
        value: The value to cast.
        target_type: A Python type (e.g., int, float, str, list).
        default: Value to return if casting fails.

    Returns:
        The casted value or `default`.
    """
    try:
        if target_type is bool:
            # Special-case boolean conversions for common string values
            if isinstance(value, str):
                lowered = value.strip().lower()
                if lowered in ("true", "1", "yes", "y", "t"):
                    return True
                if lowered in ("false", "0", "no", "n", "f"):
                    return False
                raise ValueError("Cannot interpret string as bool")
            return bool(value)

        if target_type in (list, tuple, set):
            # Ensure iterables are converted element-wise when appropriate
            if isinstance(value, str):
                # Strings to sequences: split on whitespace
                parts = value.split()
                return target_type(parts)
            if isinstance(value, collections.abc.Iterable):
                return target_type(value)
            # Single non-iterable -> wrap
            return target_type((value,))

        # Generic constructor-style cast (int, float, str, etc.)
        return target_type(value)
    except Exception:
        return default

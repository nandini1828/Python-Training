"""Examples that prevent KeyError when reading dictionaries."""

from __future__ import annotations


def safe_lookup(data: dict[str, object], key: str, default: object) -> object:
    """Look up a dictionary value using get().

    Args:
        data: The source dictionary.
        key: The desired key.
        default: The fallback value when the key is missing.

    Returns:
        The stored value or the fallback default.
    """
    return data.get(key, default)

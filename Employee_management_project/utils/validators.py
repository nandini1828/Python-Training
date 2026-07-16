"""Input validation helpers."""


def is_non_empty_string(value: str) -> bool:
    """Return True when the value is a non-empty string."""
    return isinstance(value, str) and bool(value.strip())

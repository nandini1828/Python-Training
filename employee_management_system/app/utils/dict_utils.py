"""Simple dictionary helper functions for training demonstrations."""


def add_or_update(mapping: dict[str, object], key: str, value: object) -> dict[str, object]:
    """Set a key value pair and return the mapping."""
    mapping[key] = value
    return mapping


def get_value(mapping: dict[str, object], key: str, default: object | None = None) -> object | None:
    """Safely read a value from a mapping."""
    return mapping.get(key, default)

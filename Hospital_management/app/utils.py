"""Shared helper utilities for the hospital management app."""


def get_next_id(collection) -> int:
    """Return the next integer id for a dict-like or list-like collection."""
    if isinstance(collection, dict):
        return max(collection.keys(), default=0) + 1
    return max((item.id for item in collection), default=0) + 1


def validate_age(age: int) -> bool:
    """Validate patient age."""
    return isinstance(age, int) and age > 0


def appointment_generator(items):
    """Yield appointment items from a collection."""
    for item in items:
        yield item

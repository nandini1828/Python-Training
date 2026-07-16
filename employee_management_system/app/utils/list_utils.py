"""Simple list helper functions for training demonstrations."""


def append_item(items: list[object], value: object) -> list[object]:
    """Append a value to a list and return the list."""
    items.append(value)
    return items


def remove_item(items: list[object], value: object) -> list[object]:
    """Remove the first matching value from a list."""
    items.remove(value)
    return items


def sort_items(items: list[object]) -> list[object]:
    """Return a sorted copy of the list."""
    return sorted(items)

"""Simple set helper functions for training demonstrations."""


def add_to_set(values: set[object], value: object) -> set[object]:
    """Add a value to the set and return the set."""
    values.add(value)
    return values


def union_sets(left: set[object], right: set[object]) -> set[object]:
    """Return the union of two sets."""
    return left.union(right)

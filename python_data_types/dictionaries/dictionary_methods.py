"""
Dictionary core methods demonstration.
"""


def safe_get(d, key, default=None):
    """Safely get value from dictionary."""
    return d.get(key, default)


def set_default_example(d, key, default):
    """
    Demonstrates setdefault behavior.
    """
    return d.setdefault(key, default)


def merge_dicts(d1, d2):
    """Merge two dictionaries."""
    merged = d1.copy()
    merged.update(d2)
    return merged
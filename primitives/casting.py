def safe_cast(value, target_type, default=None):
    """Attempt to cast value to target_type, returning default on failure."""
    try:
        return target_type(value)
    except (TypeError, ValueError):
        return default


def count_truthy_falsy(items):
    """Return counts of truthy and falsy values in a list."""
    counts = {"truthy": 0, "falsy": 0}
    for item in items:
        if item:
            counts["truthy"] += 1
        else:
            counts["falsy"] += 1
    return counts

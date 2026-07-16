from utilities.constants import AVAILABLE, BORROWED


def classify_status(status: int) -> str:
    # Conditional control flow: if-elif-else is used to map values to labels.
    if status == AVAILABLE:
        return "available"
    if status == BORROWED:
        return "borrowed"
    return "unknown"


def is_non_empty(value) -> bool:
    # Truthy and falsy values are central to Python conditionals.
    return bool(value)


def describe_collection(items) -> str:
    # any() and all() are handy iteration helpers for quick checks.
    if any(items):
        return "has-items"
    if all(not item for item in items):
        return "empty"
    return "mixed"


def normalize_title(title: str) -> str:
    # Ternary operator for compact single-line decisions.
    return title.strip().title() if title else ""

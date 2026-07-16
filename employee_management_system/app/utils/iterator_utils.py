"""Iterator helpers for beginner-friendly collection demonstrations."""


def iterate_with_enumerate(items: list[object]) -> list[tuple[int, object]]:
    """Return items with indexes using enumerate."""
    return list(enumerate(items))


def iterate_with_zip(left: list[object], right: list[object]) -> list[tuple[object, object]]:
    """Return zipped tuples from two lists."""
    return list(zip(left, right))

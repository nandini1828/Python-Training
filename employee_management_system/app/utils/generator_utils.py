"""Generator helper functions used for simple iteration examples."""


def number_generator(limit: int) -> list[int]:
    """Return a list of numbers from 0 to limit-1 using a generator expression."""
    return [number for number in range(limit)]


def yield_names(names: list[str]) -> list[str]:
    """Yield each name from a list and return them as a list."""
    return [name for name in names]

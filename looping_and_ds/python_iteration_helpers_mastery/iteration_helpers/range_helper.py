"""
range() helper functions.
"""


def generate_range(start: int, stop: int, step: int = 1) -> list[int]:
    """
    Generates a list of numbers using range().

    Parameters
    ----------
    start : int
        Starting value.
    stop : int
        Ending value (exclusive).
    step : int
        Step size.

    Returns
    -------
    list[int]
        Generated range values.
    """
    return list(range(start, stop, step))
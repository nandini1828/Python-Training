"""
any() and all() helper functions.
"""


def check_any(values: list[bool]) -> bool:
    """
    Returns True if at least one value is truthy.

    Parameters
    ----------
    values : list[bool]
        Boolean values.

    Returns
    -------
    bool
        Result of any().
    """
    return any(values)


def check_all(values: list[bool]) -> bool:
    """
    Returns True only if all values are truthy.

    Parameters
    ----------
    values : list[bool]
        Boolean values.

    Returns
    -------
    bool
        Result of all().
    """
    return all(values)
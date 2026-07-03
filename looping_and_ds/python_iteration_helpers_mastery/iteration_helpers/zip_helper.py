"""
zip() and zip_longest() helper functions.
"""

from itertools import zip_longest
from typing import Any


def zip_items(first: list[Any], second: list[Any]) -> list[tuple[Any, Any]]:
    """
    Zips two lists together.

    Parameters
    ----------
    first : list[Any]
        First list.
    second : list[Any]
        Second list.

    Returns
    -------
    list[tuple[Any, Any]]
        Paired values from both lists.
    """
    return list(zip(first, second))


def zip_longest_items(
    first: list[Any],
    second: list[Any],
    fill_value: Any = None,
) -> list[tuple[Any, Any]]:
    """
    Zips two lists of unequal length using zip_longest().

    Parameters
    ----------
    first : list[Any]
        First list.
    second : list[Any]
        Second list.
    fill_value : Any
        Value used for missing elements.

    Returns
    -------
    list[tuple[Any, Any]]
        Paired values including fill values for missing items.
    """
    return list(zip_longest(first, second, fillvalue=fill_value))
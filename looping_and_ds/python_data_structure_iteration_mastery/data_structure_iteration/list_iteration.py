"""
List iteration utilities.
"""

from typing import Any


def get_items_by_index(items: list[Any]) -> list[tuple[int, Any]]:
    """
    Returns index-item pairs from a list.

    Parameters
    ----------
    items : list[Any]
        Input list.

    Returns
    -------
    list[tuple[int, Any]]
        List of index-item pairs.
    """
    indexed_items = []

    for index in range(len(items)):
        indexed_items.append((index, items[index]))

    return indexed_items


def get_list_slices(items: list[Any]) -> dict[str, list[Any]]:
    """
    Returns common list slices.

    Parameters
    ----------
    items : list[Any]
        Input list.

    Returns
    -------
    dict[str, list[Any]]
        Dictionary containing different slices.
    """
    return {
        "first_three": items[:3],
        "last_two": items[-2:],
        "every_second": items[::2],
    }


def iterate_list_items(items: list[Any]) -> list[Any]:
    """
    Iterates through list items and returns them in order.

    Parameters
    ----------
    items : list[Any]
        Input list.

    Returns
    -------
    list[Any]
        Visited list items.
    """
    visited_items = []

    for item in items:
        visited_items.append(item)

    return visited_items
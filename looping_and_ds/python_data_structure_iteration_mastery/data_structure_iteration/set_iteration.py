"""
Set iteration and membership utilities.
"""


def check_membership_in_list(items: list[int], target: int) -> bool:
    """
    Checks membership in a list.

    Parameters
    ----------
    items : list[int]
        Input list.
    target : int
        Value to search.

    Returns
    -------
    bool
        True if found, else False.
    """
    return target in items


def check_membership_in_set(items: set[int], target: int) -> bool:
    """
    Checks membership in a set.

    Parameters
    ----------
    items : set[int]
        Input set.
    target : int
        Value to search.

    Returns
    -------
    bool
        True if found, else False.
    """
    return target in items


def iterate_set_items(items: set[str]) -> list[str]:
    """
    Iterates over a set and returns items as a list.

    Parameters
    ----------
    items : set[str]
        Input set.

    Returns
    -------
    list[str]
        List of set items.
    """
    collected_items = []

    for item in items:
        collected_items.append(item)

    return collected_items
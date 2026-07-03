"""
enumerate() helper functions.
"""


def enumerate_items(items: list[str]) -> list[tuple[int, str]]:
    """
    Returns index-value pairs using enumerate().

    Parameters
    ----------
    items : list[str]
        Input items.

    Returns
    -------
    list[tuple[int, str]]
        Enumerated index-value pairs.
    """
    return list(enumerate(items))
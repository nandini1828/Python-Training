"""
Dictionary iteration utilities.
"""

from typing import Any


def get_dictionary_keys(data: dict[str, Any]) -> list[str]:
    """
    Returns dictionary keys as a list.
    """
    return list(data.keys())


def get_dictionary_values(data: dict[str, Any]) -> list[Any]:
    """
    Returns dictionary values as a list.
    """
    return list(data.values())


def get_dictionary_items(data: dict[str, Any]) -> list[tuple[str, Any]]:
    """
    Returns dictionary items as a list of key-value pairs.
    """
    return list(data.items())
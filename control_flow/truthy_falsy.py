"""
Examples demonstrating Python's truthy and falsy values.

In Python, every object has an associated truth value. By default,
objects are considered True unless they define __bool__() returning
False or __len__() returning zero.

Topics covered:
- bool()
- Truthy values
- Falsy values
- Empty collections
- None
- Custom __bool__()
- Custom __len__()

Author: Python Training
"""

from __future__ import annotations

from typing import Any


class ShoppingCart:
    """
    Represents a shopping cart.

    A shopping cart is considered truthy if it contains items.
    """

    def __init__(self, items: list[str] | None = None) -> None:
        self.items = items or []

    def __bool__(self) -> bool:
        """
        Determine the truth value of the shopping cart.

        Returns:
            True if the cart contains at least one item.
        """
        return len(self.items) > 0


class Playlist:
    """
    Represents a playlist.

    Python automatically uses __len__() to determine truthiness
    when __bool__() is not implemented.
    """

    def __init__(self, songs: list[str] | None = None) -> None:
        self.songs = songs or []

    def __len__(self) -> int:
        """
        Return the number of songs.

        Returns:
            Total songs in the playlist.
        """
        return len(self.songs)


def is_truthy(value: Any) -> bool:
    """
    Return the truth value of any Python object.

    Args:
        value:
            Any Python object.

    Returns:
        True if the object is truthy.
    """
    return bool(value)


def is_falsy(value: Any) -> bool:
    """
    Determine whether a value is falsy.

    Args:
        value:
            Any Python object.

    Returns:
        True if the value is falsy.
    """
    return not bool(value)


def get_truthiness(value: Any) -> str:
    """
    Return a human-readable truthiness description.

    Args:
        value:
            Any Python object.

    Returns:
        "Truthy" or "Falsy".
    """
    return "Truthy" if value else "Falsy"


def default_username(username: str | None) -> str:
    """
    Return a default username if one is not provided.

    Args:
        username:
            Username supplied by the user.

    Returns:
        Valid username.
    """
    return username or "Guest"


def first_available_value(*values: Any) -> Any:
    """
    Return the first truthy value.

    Demonstrates Python's 'or' operator.

    Args:
        *values:
            Any number of values.

    Returns:
        First truthy value or None.
    """
    for value in values:
        if value:
            return value

    return None


def all_values_truthy(values: list[Any]) -> bool:
    """
    Check whether every value is truthy.

    Args:
        values:
            List of values.

    Returns:
        True if all values are truthy.
    """
    return all(values)


def any_value_truthy(values: list[Any]) -> bool:
    """
    Check whether at least one value is truthy.

    Args:
        values:
            List of values.

    Returns:
        True if any value is truthy.
    """
    return any(values)


def safe_display_name(name: str | None) -> str:
    """
    Return a display name.

    Uses truthiness to provide a default value.

    Args:
        name:
            User's name.

    Returns:
        Display name.
    """
    if name:
        return name

    return "Anonymous"


def has_items(collection: list[Any]) -> bool:
    """
    Determine whether a list contains elements.

    Args:
        collection:
            Input list.

    Returns:
        True if not empty.
    """
    return bool(collection)


def has_content(text: str) -> bool:
    """
    Determine whether a string contains characters.

    Args:
        text:
            Input string.

    Returns:
        True if the string is not empty.
    """
    return bool(text)


def is_valid_response(response: Any) -> bool:
    """
    Validate an API response.

    Args:
        response:
            API response object.

    Returns:
        True if the response is not empty.
    """
    return bool(response)


def remove_falsy_values(values: list[Any]) -> list[Any]:
    """
    Remove all falsy values from a list.

    Args:
        values:
            Input values.

    Returns:
        List containing only truthy values.
    """
    return [value for value in values if value]


def truthy_examples() -> list[Any]:
    """
    Return common truthy values.

    Returns:
        List of truthy examples.
    """
    return [
        1,
        -10,
        3.14,
        "Python",
        [1, 2],
        {"name": "Alice"},
        {1, 2},
        (1,),
        True,
    ]


def falsy_examples() -> list[Any]:
    """
    Return common falsy values.

    Returns:
        List of falsy examples.
    """
    return [
        0,
        0.0,
        "",
        [],
        {},
        (),
        set(),
        None,
        False,
    ]


__all__ = [
    "ShoppingCart",
    "Playlist",
    "is_truthy",
    "is_falsy",
    "get_truthiness",
    "default_username",
    "first_available_value",
    "all_values_truthy",
    "any_value_truthy",
    "safe_display_name",
    "has_items",
    "has_content",
    "is_valid_response",
    "remove_falsy_values",
    "truthy_examples",
    "falsy_examples",
]
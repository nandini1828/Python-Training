"""
utils.py

Reusable utility functions demonstrating Python's built-in reversed() function.
"""

from typing import Any


def reverse_list(items: list[Any]) -> list[Any]:
    """
    Return a reversed copy of a list.
    """
    return list(reversed(items))


def reverse_tuple(items: tuple[Any, ...]) -> tuple[Any, ...]:
    """
    Return a reversed tuple.
    """
    return tuple(reversed(items))


def reverse_string(text: str) -> str:
    """
    Return the reversed string.
    """
    return "".join(reversed(text))


def reverse_range(start: int, stop: int) -> list[int]:
    """
    Return a reversed range from start to stop.
    """
    return list(reversed(range(start, stop)))


def reverse_lines(lines: list[str]) -> list[str]:
    """
    Return lines in reverse order.
    """
    return list(reversed(lines))


def reverse_keys(data: dict[Any, Any]) -> list[Any]:
    """
    Return dictionary keys in reverse insertion order.
    """
    return list(reversed(data.keys()))


def reverse_values(data: dict[Any, Any]) -> list[Any]:
    """
    Return dictionary values in reverse insertion order.
    """
    return list(reversed(data.values()))


def countdown(start: int) -> list[int]:
    """
    Return a countdown from start to 1.
    """
    return list(reversed(range(1, start + 1)))


def browser_history(history: list[str]) -> list[str]:
    """
    Return browser history from newest to oldest.
    """
    return list(reversed(history))


def is_palindrome(text: str) -> bool:
    """
    Check whether a string is a palindrome.
    """
    cleaned = text.lower()
    return cleaned == "".join(reversed(cleaned))
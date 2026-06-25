"""
==================================================
Module: String Utilities
Topic: String Methods

Description:
Provides utility functions for manipulating
string objects.
==================================================
"""

from __future__ import annotations


class StringMethods:
    """A beginner-friendly wrapper around common string operations."""

    def __init__(self, text: str) -> None:
        self.text = text

    def upper_case(self) -> str:
        return self.text.upper()

    def lower_case(self) -> str:
        return self.text.lower()

    def count_letters(self, letter: str) -> int:
        return self.text.count(letter)

    def split_words(self) -> list[str]:
        return self.text.split()

    def replace_word(self, old: str, new: str) -> str:
        return self.text.replace(old, new)


def uppercase_text(text: str) -> str:
    """Convert a string to uppercase."""
    return text.upper()


def lowercase_text(text: str) -> str:
    """Convert a string to lowercase."""
    return text.lower()


def count_character(text: str, character: str) -> int:
    """Count how many times a character appears in a string."""
    return text.count(character)


def split_text(text: str) -> list[str]:
    """Split a string into words."""
    return text.split()


def replace_text(text: str, old: str, new: str) -> str:
    """Replace one piece of text with another."""
    return text.replace(old, new)


def strip_text(text: str) -> str:
    """Remove extra spaces from the beginning and end of a string."""
    return text.strip()


def starts_with(text: str, prefix: str) -> bool:
    """Check whether a string starts with a given prefix."""
    return text.startswith(prefix)


def ends_with(text: str, suffix: str) -> bool:
    """Check whether a string ends with a given suffix."""
    return text.endswith(suffix)

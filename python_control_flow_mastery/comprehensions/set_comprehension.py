"""Examples showing set comprehensions."""

from __future__ import annotations


def unique_lengths(words: list[str]) -> set[int]:
    """Return the lengths of words as a set of unique values.

    Args:
        words: The words to examine.

    Returns:
        A set containing each word length.
    """
    return {len(word) for word in words}

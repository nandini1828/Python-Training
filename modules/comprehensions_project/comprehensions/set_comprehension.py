"""Examples of set comprehensions."""

from typing import List, Set


def unique_lowercase_words(words: List[str]) -> Set[str]:
    """Return the unique lowercase words from a list."""
    return {word.lower() for word in words}

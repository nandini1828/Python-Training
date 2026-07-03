"""
Dictionary key protection utilities.
"""

from collections import defaultdict
from typing import Any


def safe_get_value(data: dict[str, Any], key: str, default: Any = None) -> Any:
    """
    Safely retrieves a value using dict.get().

    Parameters
    ----------
    data : dict[str, Any]
        Input dictionary.
    key : str
        Key to retrieve.
    default : Any
        Default value if key is missing.

    Returns
    -------
    Any
        Retrieved value or default.
    """
    return data.get(key, default)


def count_words_with_defaultdict(words: list[str]) -> dict[str, int]:
    """
    Counts word frequencies using defaultdict.

    Parameters
    ----------
    words : list[str]
        Input words.

    Returns
    -------
    dict[str, int]
        Word frequency mapping.
    """
    word_counts: defaultdict[str, int] = defaultdict(int)

    for word in words:
        word_counts[word] += 1

    return dict(word_counts)
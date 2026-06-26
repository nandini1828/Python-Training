"""
Exercise Solutions - Section 4
"""

from typing import Any, Dict, Optional


def query_json(
    data_dict: Dict[str, Any],
    path_str: str,
    default: Optional[Any] = None
) -> Any:
    """
    Exercise 4.1
    Query nested dictionaries using dot notation.
    """

    current: Any = data_dict

    for key in path_str.split("."):

        if isinstance(current, dict) and key in current:
            current = current[key]

        else:
            return default

    return current


def word_count(text: str) -> Dict[str, int]:
    """
    Exercise 4.2
    Count word frequency.
    """

    text = text.lower()

    punctuation: str = ".,!?"

    for symbol in punctuation:
        text = text.replace(symbol, "")

    words: list[str] = text.split()

    frequency: Dict[str, int] = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency
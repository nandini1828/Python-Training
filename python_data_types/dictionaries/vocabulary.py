"""
Word frequency counter.
"""

from typing import Dict


def word_count(text: str) -> Dict[str, int]:
    """
    Counts frequency of words in a sentence.

    Rules:
    - Case insensitive
    - Ignores punctuation: . , ! ?
    """

    # Normalize text
    text = text.lower()

    for ch in ".,!?":
        text = text.replace(ch, "")

    words: list[str] = text.split()

    freq: Dict[str, int] = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


# Example
text = "Hello, hello! Indiana Jones. Hello?"
print(word_count(text))
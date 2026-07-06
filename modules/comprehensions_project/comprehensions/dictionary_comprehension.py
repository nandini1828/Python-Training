"""Examples of dictionary comprehensions."""

from typing import Dict


def square_mapping(limit: int) -> Dict[int, int]:
    """Create a mapping of numbers to their squares."""
    return {value: value**2 for value in range(limit)}


def vowel_count(text: str) -> Dict[str, int]:
    """Count vowels in a string."""
    vowels = "aeiou"
    lowered_text = text.lower()
    return {vowel: lowered_text.count(vowel) for vowel in vowels}

"""
Examples demonstrating Python set comprehensions.

Topics covered:

- Basic set comprehensions
- Filtering
- Transformations
- Removing duplicates

Author: Python Training
"""

from __future__ import annotations


def unique_lowercase_words(
    words: list[str],
) -> set[str]:
    """
    Convert words to lowercase and remove duplicates.

    Args:
        words:
            Input words.

    Returns:
        Unique lowercase words.
    """
    return {
        word.lower()
        for word in words
    }


def unique_first_letters(
    words: list[str],
) -> set[str]:
    """
    Return unique first letters.

    Args:
        words:
            Input words.

    Returns:
        Set of first letters.
    """
    return {
        word[0].lower()
        for word in words
        if word
    }


def unique_word_lengths(
    words: list[str],
) -> set[int]:
    """
    Return unique word lengths.

    Args:
        words:
            Input words.

    Returns:
        Set of lengths.
    """
    return {
        len(word)
        for word in words
    }


def unique_even_numbers(
    numbers: list[int],
) -> set[int]:
    """
    Return unique even numbers.

    Args:
        numbers:
            Input numbers.

    Returns:
        Set of even numbers.
    """
    return {
        number
        for number in numbers
        if number % 2 == 0
    }


def unique_remainders(
    numbers: list[int],
    divisor: int,
) -> set[int]:
    """
    Return unique remainders.

    Args:
        numbers:
            Input numbers.

        divisor:
            Divisor.

    Returns:
        Set of remainders.

    Raises:
        ValueError:
            If divisor is zero.
    """
    if divisor == 0:
        raise ValueError(
            "divisor cannot be zero."
        )

    return {
        number % divisor
        for number in numbers
    }


def positive_numbers(
    numbers: list[int],
) -> set[int]:
    """
    Return unique positive numbers.

    Args:
        numbers:
            Input numbers.

    Returns:
        Positive numbers.
    """
    return {
        number
        for number in numbers
        if number > 0
    }


def unique_characters(
    text: str,
) -> set[str]:
    """
    Return unique characters.

    Args:
        text:
            Input text.

    Returns:
        Character set.
    """
    return {
        character
        for character in text
    }


def vowels(
    text: str,
) -> set[str]:
    """
    Return unique vowels.

    Args:
        text:
            Input text.

    Returns:
        Vowel set.
    """
    vowels_set = {"a", "e", "i", "o", "u"}

    return {
        character.lower()
        for character in text
        if character.lower() in vowels_set
    }


__all__ = [
    "unique_lowercase_words",
    "unique_first_letters",
    "unique_word_lengths",
    "unique_even_numbers",
    "unique_remainders",
    "positive_numbers",
    "unique_characters",
    "vowels",
]
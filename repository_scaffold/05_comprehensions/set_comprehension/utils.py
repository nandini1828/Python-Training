from typing import Iterable


def unique_uppercase(values: Iterable[str]) -> set[str]:
    """Return unique uppercase strings."""
    return {item.upper() for item in values}


def square_set(numbers: Iterable[int]) -> set[int]:
    """Return unique squared numbers."""
    return {number * number for number in numbers}


def even_numbers(numbers: Iterable[int]) -> set[int]:
    """Return unique even numbers."""
    return {number for number in numbers if number % 2 == 0}


def char_set(words: Iterable[str]) -> set[str]:
    """Return unique characters from all words."""
    return {char for word in words for char in word}


def filter_letters(words: Iterable[str]) -> set[str]:
    """Return words longer than three characters."""
    return {word for word in words if len(word) > 3}


def common_characters(first: str, second: str) -> set[str]:
    """Return characters that appear in both strings."""
    return {char for char in first if char in second}

from typing import Any, Iterable, Sequence


def square_numbers(numbers: Iterable[int]) -> list[int]:
    """Return the square of each number."""
    return [number * number for number in numbers]


def words_lengths(words: Iterable[str]) -> list[int]:
    """Return the length of each word."""
    return [len(word) for word in words]


def even_numbers(numbers: Iterable[int]) -> list[int]:
    """Return only even numbers, preserving input order."""
    return [number for number in numbers if number % 2 == 0]


def uppercase_words(words: Iterable[str]) -> list[str]:
    """Return uppercase versions of each word."""
    return [word.upper() for word in words]


def nested_flatten(matrix: Iterable[Iterable[Any]]) -> list[Any]:
    """Flatten one level of nested iterables."""
    return [item for row in matrix for item in row]


def combine_words(first: Iterable[str], second: Iterable[str]) -> list[str]:
    """Return all phrase combinations from two word collections."""
    second_words = list(second)
    return [f"{a} {b}" for a in first for b in second_words]


def filter_short_words(words: Iterable[str], max_length: int) -> list[str]:
    """Return words whose length is less than or equal to max_length."""
    if max_length < 0:
        return []

    return [word for word in words if len(word) <= max_length]


def strings_to_chars(words: Iterable[str]) -> list[str]:
    """Return every character from each word in order."""
    return [char for word in words for char in word]


def indexed_words(words: Sequence[str], start: int = 0) -> list[str]:
    """Return display labels that include index and word."""
    return [f"{index}: {word}" for index, word in enumerate(words, start=start)]

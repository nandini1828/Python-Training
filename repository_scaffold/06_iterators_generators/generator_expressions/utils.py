from typing import Iterable, Iterator


def square_generator(numbers: Iterable[int]) -> Iterator[int]:
    """Yield the square of each number lazily."""
    return (number * number for number in numbers)


def even_generator(numbers: Iterable[int]) -> Iterator[int]:
    """Yield even numbers lazily."""
    return (number for number in numbers if number % 2 == 0)


def char_generator(words: Iterable[str]) -> Iterator[str]:
    """Yield characters from each word lazily."""
    return (char for word in words for char in word)


def word_lengths_generator(words: Iterable[str]) -> Iterator[int]:
    """Yield word lengths lazily."""
    return (len(word) for word in words)


def running_total_generator(numbers: Iterable[int]) -> Iterator[int]:
    """Yield running totals lazily."""
    total = 0
    for number in numbers:
        total += number
        yield total

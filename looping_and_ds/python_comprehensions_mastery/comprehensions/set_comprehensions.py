"""
Set comprehension utilities.
"""


def get_unique_lowercase_words(words: list[str]) -> set[str]:
    """
    Converts all words to lowercase and returns unique values.

    Parameters
    ----------
    words : list[str]
        Input words.

    Returns
    -------
    set[str]
        Unique lowercase words.
    """
    return {word.lower() for word in words}


def get_even_number_set(numbers: list[int]) -> set[int]:
    """
    Returns a set of even numbers using set comprehension.

    Parameters
    ----------
    numbers : list[int]
        Input list of integers.

    Returns
    -------
    set[int]
        Unique even numbers.
    """
    return {number for number in numbers if number % 2 == 0}
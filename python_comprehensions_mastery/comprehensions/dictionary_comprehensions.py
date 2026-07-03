"""
Dictionary comprehension utilities.
"""


def build_square_dictionary(limit: int) -> dict[int, int]:
    """
    Builds a dictionary of numbers mapped to their squares.

    Parameters
    ----------
    limit : int
        Upper limit for range generation.

    Returns
    -------
    dict[int, int]
        Dictionary where key is a number and value is its square.
    """
    return {number: number ** 2 for number in range(limit)}


def map_words_to_lengths(words: list[str]) -> dict[str, int]:
    """
    Maps each word to its length using dictionary comprehension.

    Parameters
    ----------
    words : list[str]
        Input list of words.

    Returns
    -------
    dict[str, int]
        Dictionary of word-length mappings.
    """
    return {word: len(word) for word in words}
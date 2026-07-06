from collections import Counter


def count_characters(text: str) -> Counter:
    """
    Count occurrences of each character.

    Example:
        Input:
            "banana"

        Output:
            Counter({'a':3,'n':2,'b':1})
    """
    return Counter(text)


def count_words(sentence: str) -> Counter:
    """
    Count word frequencies.
    """
    return Counter(sentence.split())
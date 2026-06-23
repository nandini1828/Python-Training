"""
Word frequency counter.
"""


def word_count(text):
    """
    Counts frequency of words in a sentence.

    Rules:
    - case insensitive
    - ignores punctuation . , ! ?
    """

    # Normalize text
    text = text.lower()

    for ch in ".,!?":
        text = text.replace(ch, "")

    words = text.split()

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq
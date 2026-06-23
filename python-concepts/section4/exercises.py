"""
Exercise Solutions - Section 4
"""


def query_json(data_dict, path_str, default=None):
    """
    Exercise 4.1
    Query nested dictionaries using dot notation.
    """

    current = data_dict

    for key in path_str.split("."):

        if isinstance(current, dict) and key in current:
            current = current[key]

        else:
            return default

    return current


def word_count(text):
    """
    Exercise 4.2
    Count word frequency.
    """

    text = text.lower()

    punctuation = ".,!?"

    for symbol in punctuation:
        text = text.replace(symbol, "")

    words = text.split()

    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency
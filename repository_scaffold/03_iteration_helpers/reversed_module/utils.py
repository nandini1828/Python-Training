"""
Utilities for reversed operations
"""

def reverse_list(data):
    return list(reversed(data))


def reverse_string(text):
    return text[::-1]


def reverse_tuple(data):
    return tuple(reversed(data))


def reverse_range(start, end):
    return list(reversed(range(start, end)))


def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])


def reverse_each_word(sentence):
    return " ".join(word[::-1] for word in sentence.split())


def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]


def reverse_with_slice(data):
    return data[::-1]
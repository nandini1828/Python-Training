"""Tests for word_count utility."""
from python_datatypes_mastery.exercises.word_counter import word_count


def test_word_count_basic():
    text = "Hello, hello! world."
    freqs = word_count(text)
    assert freqs.get("hello") == 2
    assert freqs.get("world") == 1


def test_word_count_empty():
    assert word_count("") == {}

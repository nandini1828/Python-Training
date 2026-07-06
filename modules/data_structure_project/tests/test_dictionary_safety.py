from collections import defaultdict

from data_structures.dictionary_safety import count_words, safe_lookup


def test_safe_lookup():
    assert safe_lookup({"name": "Ada"}, "age", "unknown") == "unknown"


def test_count_words():
    counts = count_words(["one", "two", "one"])
    assert isinstance(counts, defaultdict)
    assert counts["one"] == 2
    assert counts["two"] == 1

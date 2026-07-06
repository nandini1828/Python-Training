"""
test_dictionary_key_protection.py

Unit tests for dictionary key protection topics.
"""

from data_structure_iteration.dictionary_key_protection import dictionary_key_protection


def test_dictionary_key_protection_returns_default_values():
    protection = dictionary_key_protection()
    assert protection["get_headphones"] == 0
    assert protection["defaultdict_headphones"] == 0

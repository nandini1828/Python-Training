"""
Tests for zip_examples.py
"""

from iterations import ZipExamples


def test_zip_lists():
    assert ZipExamples.zip_lists(
        ["A", "B"],
        [90, 80]
    ) == [
        ("A", 90),
        ("B", 80)
    ]


def test_zip_longest_lists():
    assert ZipExamples.zip_longest_lists(
        ["A"],
        [90, 80]
    ) == [
        ("A", 90),
        ("-", 80)
    ]
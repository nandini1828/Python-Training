"""
Unit tests for nested_comprehension.py
"""

from nested_comprehension import flatten_office
from nested_comprehension import seating_layout


def test_flatten_office(capsys):
    """
    Verify nested lists are flattened correctly.
    """

    flatten_office()

    captured = capsys.readouterr()

    assert "John" in captured.out
    assert "Alice" in captured.out
    assert "David" in captured.out
    assert "Emma" in captured.out
    assert "Mike" in captured.out
    assert "Sophia" in captured.out


def test_seating_layout(capsys):
    """
    Verify seating layout grid generation.
    """

    seating_layout()

    captured = capsys.readouterr()

    assert "Office Seating Layout" in captured.out

    # There should be 12 empty seats (3 rows × 4 columns)
    assert captured.out.count("Empty") == 12


def test_flatten_office_heading(capsys):
    """
    Verify heading is displayed.
    """

    flatten_office()

    captured = capsys.readouterr()

    assert "Flatten Office Floors" in captured.out
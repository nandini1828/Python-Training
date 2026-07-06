"""
Unit tests for range_helper.py
"""

from range_helper import generate_roll_numbers


def test_generate_roll_numbers(capsys):
    """
    Verify that roll numbers are generated correctly.
    """

    generate_roll_numbers(5)

    captured = capsys.readouterr()

    assert "Generated Roll Numbers" in captured.out

    for roll in range(1, 6):
        assert f"Roll No : {roll}" in captured.out


def test_generate_single_roll_number(capsys):
    """
    Verify generation of a single roll number.
    """

    generate_roll_numbers(1)

    captured = capsys.readouterr()

    assert "Roll No : 1" in captured.out


def test_generate_zero_roll_numbers(capsys):
    """
    Verify handling of zero students.
    """

    generate_roll_numbers(0)

    captured = capsys.readouterr()

    assert "Generated Roll Numbers" in captured.out
    assert "Roll No :" not in captured.out
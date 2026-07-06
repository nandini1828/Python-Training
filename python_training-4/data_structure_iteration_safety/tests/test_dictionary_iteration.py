"""
Unit tests for dictionary_iteration.py
"""

from dictionary_iteration import display_inventory


def test_display_inventory(capsys):
    """
    Verify keys, values and items are displayed.
    """

    inventory = {
        "Laptop": 15,
        "Mouse": 40,
        "Keyboard": 25
    }

    display_inventory(inventory)

    captured = capsys.readouterr()

    assert "Dictionary Keys" in captured.out
    assert "Laptop" in captured.out
    assert "Mouse" in captured.out
    assert "Keyboard" in captured.out

    assert "15" in captured.out
    assert "40" in captured.out
    assert "25" in captured.out


def test_empty_inventory(capsys):

    display_inventory({})

    captured = capsys.readouterr()

    assert "Dictionary Keys" in captured.out
    assert "Dictionary Values" in captured.out
    assert "Dictionary Items" in captured.out
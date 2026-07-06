"""
Unit tests for dictionary_safety.py
"""

from dictionary_safety import safe_lookup
from dictionary_safety import sales_counter


def test_safe_lookup(capsys):
    """
    Verify .get() safely retrieves values.
    """

    inventory = {
        "Laptop": 15,
        "Mouse": 40
    }

    safe_lookup(inventory)

    captured = capsys.readouterr()

    assert "15" in captured.out
    assert "0" in captured.out


def test_empty_inventory_lookup(capsys):

    safe_lookup({})

    captured = capsys.readouterr()

    assert "0" in captured.out


def test_sales_counter(capsys):
    """
    Verify defaultdict counts correctly.
    """

    sales_counter()

    captured = capsys.readouterr()

    assert "Laptop" in captured.out
    assert "2" in captured.out
    assert "Mouse" in captured.out
    assert "1" in captured.out
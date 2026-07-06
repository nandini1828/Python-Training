"""
test_list_iteration.py

Unit tests for list iteration topics.
"""

from data_structure_iteration.list_iteration import list_iteration_and_slicing


def test_list_iteration_and_slicing_returns_expected_slice():
    products = ["Laptop", "Mouse", "Monitor", "Keyboard"]
    assert products[:2] == ["Laptop", "Mouse"]
    assert products[-1] == "Keyboard"
    assert products[::2] == ["Laptop", "Monitor"]


def test_list_iteration_and_slicing_prints_expected_output(capsys):
    products = ["Laptop", "Mouse", "Monitor", "Keyboard"]
    list_iteration_and_slicing(products)
    captured = capsys.readouterr()
    assert "Full inventory" in captured.out
    assert "First two products" in captured.out
    assert "Last product" in captured.out
    assert "Every second product" in captured.out

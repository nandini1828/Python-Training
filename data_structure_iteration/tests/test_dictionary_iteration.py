"""
test_dictionary_iteration.py

Unit tests for dictionary iteration topics.
"""

from data_structure_iteration.dictionary_iteration import dictionary_iteration


def test_dictionary_iteration_returns_inventory_mapping():
    keys = ["Laptop", "Mouse"]
    values = [15, 0]
    inventory = dictionary_iteration(keys, values)

    assert list(inventory.keys()) == ["Laptop", "Mouse"]
    assert list(inventory.values()) == [15, 0]
    assert list(inventory.items()) == [("Laptop", 15), ("Mouse", 0)]

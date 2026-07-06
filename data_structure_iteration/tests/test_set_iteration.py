"""
test_set_iteration.py

Unit tests for set iteration topics.
"""

from data_structure_iteration.set_iteration import set_membership_and_looping


def test_set_iteration_creates_unique_set():
    products = ["Laptop", "Mouse", "Monitor", "Keyboard"]
    product_set = set_membership_and_looping(products)

    assert isinstance(product_set, set)
    assert "Laptop" in product_set
    assert "Tablet" not in product_set
    assert all(item in product_set for item in products)

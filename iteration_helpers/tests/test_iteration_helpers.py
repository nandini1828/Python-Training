"""
test_iteration_helpers.py

Unit tests for iteration_helpers module.

Run:
    pytest test_iteration_helpers.py -v
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import iteration_helpers


def test_generate_daily_batches_range():
    count = 0
    for _ in range(1, 6, 2):
        count += 1
    assert count == 3


def test_enumerate_inventory_items():
    products = ["A", "B", "C"]
    result = [(index, product) for index, product in enumerate(products, start=1)]
    assert result == [(1, "A"), (2, "B"), (3, "C")]


def test_zip_parallel_iteration():
    products = ["A", "B"]
    quantities = [10, 20]
    result = list(zip(products, quantities))
    assert result == [("A", 10), ("B", 20)]


def test_zip_longest_unequal_lengths():
    products = ["A", "B"]
    quantities = [10]
    result = list(iteration_helpers.zip_longest(products, quantities, fillvalue=0))
    assert result == [("A", 10), ("B", 0)]


def test_reversed_iteration():
    values = [1, 2, 3]
    result = [value for value in reversed(values)]
    assert result == [3, 2, 1]


def test_sorted_custom_key():
    products = [{"name": "A", "price": 30}, {"name": "B", "price": 20}]
    sorted_products = sorted(products, key=lambda item: item["price"])
    assert [product["name"] for product in sorted_products] == ["B", "A"]


def test_any_low_stock():
    result = iteration_helpers.any_low_stock([
        {"name": "A", "stock": 5},
        {"name": "B", "stock": 2},
    ], threshold=3)
    assert result is True


def test_all_orders_ready():
    result = iteration_helpers.all_orders_ready([
        {"id": 1, "status": "ready"},
        {"id": 2, "status": "ready"},
    ])
    assert result is True

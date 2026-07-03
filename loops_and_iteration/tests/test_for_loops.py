"""
test_for_loops.py

Unit tests for for_loops module.

Topics tested:
- Iterating over lists
- Iterating over ranges
- Iterating with enumerate
- Iterating with zip
- Nested loops
- Dictionary iteration

Run:
    pytest test_for_loops.py -v
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import for_loops


def test_iterate_over_list():
    """Test basic list iteration."""
    products = ["Laptop", "Mouse", "Keyboard"]
    count = 0
    
    for product in products:
        count += 1
    
    assert count == 3, "Should iterate over 3 products"


def test_iterate_over_range():
    """Test range iteration."""
    count = 0
    
    for i in range(5):
        count += 1
    
    assert count == 5, "Range(5) should iterate 5 times"


def test_enumerate_with_list():
    """Test enumerate() functionality."""
    products = ["A", "B", "C"]
    indices = []
    
    for index, product in enumerate(products):
        indices.append(index)
    
    assert indices == [0, 1, 2], "enumerate() should provide indices"


def test_zip_two_lists():
    """Test zip() to iterate over parallel lists."""
    products = ["Laptop", "Mouse"]
    prices = [85000, 1500]
    
    pairs = list(zip(products, prices))
    
    assert len(pairs) == 2, "zip() should create 2 pairs"
    assert pairs[0] == ("Laptop", 85000), "First pair should match"


def test_nested_loop_iteration():
    """Test nested loops."""
    warehouse = {
        "A": ["Item1", "Item2"],
        "B": ["Item3"],
    }
    
    total_items = 0
    
    for section, items in warehouse.items():
        for item in items:
            total_items += 1
    
    assert total_items == 3, "Should count all items in nested loop"


def test_dictionary_iteration():
    """Test iterating over dictionary."""
    inventory = {"Laptop": 15, "Mouse": 120}
    
    items = []
    for product, quantity in inventory.items():
        items.append(product)
    
    assert len(items) == 2, "Should iterate over 2 items"
    assert "Laptop" in items, "Laptop should be in items"


def test_string_iteration():
    """Test iterating over string characters."""
    code = "ABC"
    chars = []
    
    for char in code:
        chars.append(char)
    
    assert len(chars) == 3, "Should iterate 3 characters"
    assert chars == ['A', 'B', 'C'], "Should match each character"


def test_inventory_report_calculation():
    """Test inventory report value calculation."""
    inventory = {
        "Laptop": {"quantity": 10, "price": 85000},
        "Mouse": {"quantity": 50, "price": 1500},
    }
    
    total_value = 0
    
    for product, details in inventory.items():
        total_value += details["quantity"] * details["price"]
    
    expected = (10 * 85000) + (50 * 1500)
    assert total_value == expected, "Total value calculation should be correct"


def test_list_of_dictionaries():
    """Test iterating over list of dictionaries."""
    items = [
        {"name": "A", "price": 100},
        {"name": "B", "price": 200},
    ]
    
    total_price = 0
    
    for item in items:
        total_price += item["price"]
    
    assert total_price == 300, "Should sum prices correctly"


def test_range_with_step():
    """Test range with step parameter."""
    numbers = []
    
    for i in range(0, 10, 2):
        numbers.append(i)
    
    assert numbers == [0, 2, 4, 6, 8], "range() with step should work correctly"

"""
test_while_loops.py

Unit tests for while_loops module.

Topics tested:
- Basic while loops
- Conditional iteration
- Counter-based loops
- State-based repetition
- Multiple conditions

Run:
    pytest test_while_loops.py -v
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_basic_countdown():
    """Test basic countdown while loop."""
    count = 5
    iterations = 0
    
    while count > 0:
        iterations += 1
        count -= 1
    
    assert iterations == 5, "Should iterate 5 times"
    assert count == 0, "Count should reach 0"


def test_while_with_counter():
    """Test while loop with counter increment."""
    counter = 0
    target = 10
    
    while counter < target:
        counter += 1
    
    assert counter == 10, "Counter should reach 10"


def test_while_string_length():
    """Test while loop checking string length."""
    text = "Python"
    index = 0
    
    while index < len(text):
        index += 1
    
    assert index == 6, "Should iterate through all characters"


def test_while_with_break_condition():
    """Test while loop with break."""
    count = 0
    result = None
    
    while True:
        count += 1
        if count > 5:
            result = count
            break
    
    assert result == 6, "Break should occur when count > 5"


def test_multiple_conditions():
    """Test while loop with multiple conditions."""
    x = 0
    y = 10
    iterations = 0
    
    while x < 5 and y > 0:
        x += 1
        y -= 1
        iterations += 1
    
    assert iterations == 5, "Should iterate 5 times"
    assert x == 5, "x should be 5"
    assert y == 5, "y should be 5"


def test_while_with_state_change():
    """Test while loop with state change."""
    active = True
    iterations = 0
    
    while active:
        iterations += 1
        if iterations >= 3:
            active = False
    
    assert iterations == 3, "Should iterate 3 times"
    assert not active, "active should be False"


def test_stock_depletion():
    """Test stock depletion simulation."""
    stock = 50
    daily_sales = 5
    days = 0
    
    while stock > 0:
        stock -= daily_sales
        days += 1
    
    assert days == 10, "Should deplete after 10 days"
    assert stock == 0, "Stock should reach 0"


def test_while_with_list():
    """Test while loop with list operations."""
    items = [1, 2, 3, 4, 5]
    index = 0
    total = 0
    
    while index < len(items):
        total += items[index]
        index += 1
    
    assert total == 15, "Sum should be 15"
    assert index == 5, "Index should reach length of list"


def test_input_validation_simulation():
    """Test input validation loop."""
    attempts = 0
    max_attempts = 3
    valid_input = False
    
    while attempts < max_attempts and not valid_input:
        attempts += 1
        # Simulate: valid on 2nd attempt
        if attempts == 2:
            valid_input = True
    
    assert attempts == 2, "Should be valid on 2nd attempt"
    assert valid_input, "Input should be valid"


def test_while_false():
    """Test while loop with False condition."""
    iterations = 0
    
    while False:
        iterations += 1
    
    assert iterations == 0, "While False should never execute"


def test_while_true_with_break():
    """Test while True with break condition."""
    iterations = 0
    
    while True:
        iterations += 1
        if iterations >= 5:
            break
    
    assert iterations == 5, "Should break at 5 iterations"

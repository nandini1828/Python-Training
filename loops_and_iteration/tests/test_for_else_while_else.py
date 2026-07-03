"""
test_for_else_while_else.py

Unit tests for for_else_while_else module.

Topics tested:
- for-else clause
- while-else clause
- Break effect on else
- Loop completion without break

Run:
    pytest test_for_else_while_else.py -v
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_for_else_no_break():
    """Test for-else executes when loop completes normally."""
    executed = False
    
    for i in range(3):
        pass
    else:
        executed = True
    
    assert executed, "else should execute when loop completes normally"


def test_for_else_with_break():
    """Test for-else doesn't execute if loop has break."""
    executed = False
    
    for i in range(3):
        break
    else:
        executed = True
    
    assert not executed, "else should NOT execute if break occurs"


def test_for_else_search_found():
    """Test for-else in search when item found."""
    items = ["A", "B", "C"]
    found = False
    
    for item in items:
        if item == "B":
            found = True
            break
    else:
        found = False  # Would only execute if no break
    
    # The else doesn't execute because of break
    # So 'found' remains True from the if block
    assert found, "Item should be found"


def test_for_else_search_not_found():
    """Test for-else in search when item not found."""
    items = ["A", "B", "C"]
    found = False
    
    for item in items:
        if item == "Z":
            found = True
            break
    else:
        # This executes because loop completed without break
        found = False
    
    assert not found, "Item should not be found"


def test_for_else_with_condition():
    """Test for-else checking if all items meet condition."""
    items = [2, 4, 6, 8]
    all_even = True
    
    for item in items:
        if item % 2 != 0:
            all_even = False
            break
    else:
        # Executes if no break (all items are even)
        pass
    
    assert all_even, "All items should be even"


def test_while_else_no_break():
    """Test while-else executes when loop completes normally."""
    executed = False
    count = 0
    
    while count < 3:
        count += 1
    else:
        executed = True
    
    assert executed, "else should execute when while completes normally"


def test_while_else_with_break():
    """Test while-else doesn't execute if loop has break."""
    executed = False
    
    while True:
        break
    else:
        executed = True
    
    assert not executed, "else should NOT execute if break occurs"


def test_while_else_counter_exhausted():
    """Test while-else when counter is exhausted."""
    count = 0
    result = "started"
    
    while count < 3:
        count += 1
    else:
        # Executes because loop condition becomes false naturally
        result = "completed"
    
    assert result == "completed", "else should execute"
    assert count == 3, "Count should be 3"


def test_while_else_with_early_break():
    """Test while-else with early break."""
    count = 0
    result = "started"
    
    while count < 10:
        count += 1
        if count == 3:
            break
    else:
        result = "completed"
    
    # else doesn't execute because of break
    assert result == "started", "else should not execute due to break"


def test_nested_for_else():
    """Test nested for-else."""
    found = False
    outer_completed = False
    
    for i in range(2):
        for j in range(2):
            if j == 1:
                found = True
                break
        else:
            # Executes if inner loop completes without break
            outer_completed = True
            break
    
    # Outer loop breaks, so else doesn't execute
    assert found, "Item should be found"


def test_for_else_with_range():
    """Test for-else with range."""
    count = 0
    else_executed = False
    
    for i in range(5):
        count += 1
    else:
        else_executed = True
    
    assert count == 5, "Should iterate 5 times"
    assert else_executed, "else should execute"


def test_validation_with_for_else():
    """Test validation loop with for-else."""
    items = [1, 2, 3, 4, 5]
    all_valid = True
    
    for item in items:
        if item > 10:
            all_valid = False
            break
    else:
        # Executes if all items are valid
        pass
    
    assert all_valid, "All items should be valid"


def test_search_pattern_for_else():
    """Test common search pattern with for-else."""
    database = ["user1", "user2", "admin", "user3"]
    search_user = "admin"
    found = False
    
    for user in database:
        if user == search_user:
            found = True
            break
    else:
        found = False
    
    # Break occurred, so else didn't execute
    # found remains True
    assert found, "User should be found"


def test_inventory_check_for_else():
    """Test inventory verification with for-else."""
    inventory = {"A": 10, "B": 20, "C": 30}
    min_stock = 5
    all_above_minimum = True
    
    for item, quantity in inventory.items():
        if quantity < min_stock:
            all_above_minimum = False
            break
    else:
        # Executes if all items above minimum
        pass
    
    assert all_above_minimum, "All items should be above minimum"


def test_multiple_break_conditions():
    """Test while-else with multiple break conditions."""
    value = 0
    result = "initial"
    
    while value < 10:
        value += 1
        if value == 5:
            result = "broken"
            break
    else:
        result = "completed"
    
    assert result == "broken", "Should break at value 5"


def test_else_clause_key_difference():
    """Test the key difference: else only runs if NO break."""
    # Scenario 1: Loop with break
    scenario1 = []
    for i in range(3):
        scenario1.append("loop")
        break
    else:
        scenario1.append("else")
    
    # Scenario 2: Loop without break
    scenario2 = []
    for i in range(1):
        scenario2.append("loop")
    else:
        scenario2.append("else")
    
    assert scenario1 == ["loop"], "Scenario 1 should not have else"
    assert scenario2 == ["loop", "else"], "Scenario 2 should have else"

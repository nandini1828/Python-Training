"""
test_break_continue_pass.py

Unit tests for break_continue_pass module.

Topics tested:
- Break statement
- Continue statement
- Pass statement
- Nested loop break
- Complex loop control

Run:
    pytest test_break_continue_pass.py -v
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_break_basic():
    """Test basic break statement."""
    result = None
    
    for i in range(10):
        if i == 5:
            result = i
            break
    
    assert result == 5, "Should break at 5"


def test_break_in_list_search():
    """Test break in list search."""
    items = ["A", "B", "C", "D"]
    found = False
    position = -1
    
    for index, item in enumerate(items):
        if item == "C":
            found = True
            position = index
            break
    
    assert found, "Item should be found"
    assert position == 2, "Position should be 2"


def test_break_early_exit():
    """Test break exits loop early."""
    iterations = 0
    
    for i in range(100):
        iterations += 1
        if i == 10:
            break
    
    assert iterations == 11, "Should stop after 11 iterations"


def test_continue_basic():
    """Test basic continue statement."""
    numbers = []
    
    for i in range(5):
        if i == 2:
            continue
        numbers.append(i)
    
    assert numbers == [0, 1, 3, 4], "Should skip 2"


def test_continue_skip_items():
    """Test continue to skip items."""
    items = [1, 2, 3, 4, 5]
    even_items = []
    
    for item in items:
        if item % 2 != 0:
            continue
        even_items.append(item)
    
    assert even_items == [2, 4], "Should contain only even items"


def test_continue_does_not_exit():
    """Test continue continues loop, doesn't exit."""
    iterations = 0
    
    for i in range(5):
        if i == 2:
            continue
        iterations += 1
    
    assert iterations == 4, "Should iterate 4 times (skipping 1 iteration)"


def test_pass_does_nothing():
    """Test pass statement does nothing."""
    items = [1, 2, 3]
    count = 0
    
    for item in items:
        pass
        count += 1
    
    assert count == 3, "Loop should still execute with pass"


def test_pass_placeholder():
    """Test pass as placeholder."""
    items = ["A", "B"]
    
    for item in items:
        # Placeholder: future implementation
        pass
    
    # Test should complete without error


def test_break_nested_loops():
    """Test break in nested loops."""
    outer_iterations = 0
    inner_iterations = 0
    
    for i in range(3):
        outer_iterations += 1
        for j in range(3):
            if j == 1:
                break
            inner_iterations += 1
    
    assert outer_iterations == 3, "Outer loop should complete"
    assert inner_iterations == 3, "Inner loop should break each time"


def test_continue_nested_loops():
    """Test continue in nested loops."""
    results = []
    
    for i in range(3):
        for j in range(3):
            if j == 1:
                continue
            results.append((i, j))
    
    assert len(results) == 6, "Should have 6 items"


def test_break_vs_continue_difference():
    """Test difference between break and continue."""
    # Break exits the loop
    break_results = []
    for i in range(5):
        if i == 2:
            break
        break_results.append(i)
    
    # Continue skips iteration
    continue_results = []
    for i in range(5):
        if i == 2:
            continue
        continue_results.append(i)
    
    assert len(break_results) == 2, "Break should exit early"
    assert len(continue_results) == 4, "Continue should skip but continue"


def test_complex_control_flow():
    """Test complex mix of break and continue."""
    valid_items = []
    
    for i in range(10):
        if i < 2:
            continue  # Skip first 2
        if i > 7:
            break     # Stop after 7
        if i % 2 == 0:  # Process only even
            valid_items.append(i)
    
    assert valid_items == [2, 4, 6], "Should have processed 2, 4, 6"


def test_break_stops_iteration():
    """Test that break stops all iteration."""
    items = list(range(10))
    count = 0
    
    for item in items:
        count += 1
        if count == 3:
            break
    
    assert count == 3, "Break should stop after 3 iterations"


def test_continue_with_multiple_conditions():
    """Test continue with multiple skip conditions."""
    results = []
    
    for i in range(10):
        if i < 3 or i > 7:
            continue
        results.append(i)
    
    assert results == [3, 4, 5, 6, 7], "Should include items 3-7"

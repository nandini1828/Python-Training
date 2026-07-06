"""
test_list_modification_trap.py

Unit tests for the list modification trap topic.
"""

from data_structure_iteration.list_modification_trap import list_modification_trap


def test_list_modification_trap_returns_filtered_orders():
    safe_list = list_modification_trap()
    assert safe_list == ["order-001", "order-003"]

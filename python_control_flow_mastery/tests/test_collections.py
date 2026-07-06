from python_control_flow_mastery.collections_iteration.list_iteration import flatten_nested_lists
from python_control_flow_mastery.collections_iteration.dictionary_iteration import summarize_inventory
from python_control_flow_mastery.collections_iteration.set_iteration import unique_names
from python_control_flow_mastery.collections_iteration.list_modification_trap import remove_even_numbers
from python_control_flow_mastery.collections_iteration.dictionary_safe_access import safe_lookup


def test_flatten_nested_lists_flattens_values():
    assert flatten_nested_lists([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_summarize_inventory_returns_counts():
    assert summarize_inventory({"apples": 3, "bananas": 2}) == "apples: 3, bananas: 2"


def test_unique_names_returns_distinct_values():
    assert unique_names(["Ada", "Ada", "Grace"]) == ["Ada", "Grace"]


def test_remove_even_numbers_leaves_odd_values():
    assert remove_even_numbers([1, 2, 3, 4]) == [1, 3]


def test_safe_lookup_returns_default_when_missing():
    assert safe_lookup({"name": "Ada"}, "age", 38) == 38

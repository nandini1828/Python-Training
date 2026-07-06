from python_control_flow_mastery.iteration.range_examples import describe_range, reverse_range
from python_control_flow_mastery.iteration.enumerate_examples import enumerate_with_index
from python_control_flow_mastery.iteration.zip_examples import zip_lists
from python_control_flow_mastery.iteration.reversed_sorted import sort_names
from python_control_flow_mastery.iteration.any_all_examples import check_inventory


def test_describe_range_outputs_summary():
    assert describe_range(3) == "range(0, 3)"


def test_reverse_range_returns_reversed_values():
    assert reverse_range(5) == [4, 3, 2, 1, 0]


def test_enumerate_with_index_handles_custom_start():
    assert enumerate_with_index(["a", "b"], start=1) == [(1, "a"), (2, "b")]


def test_zip_lists_pairs_values():
    assert zip_lists([1, 2], ["x", "y"]) == [(1, "x"), (2, "y")]


def test_sort_names_uses_case_insensitive_sort():
    assert sort_names(["bob", "Alice", "charlie"]) == ["Alice", "bob", "charlie"]


def test_check_inventory_requires_all_items():
    assert check_inventory([True, True, False]) is False

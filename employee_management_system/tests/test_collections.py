"""Tests for collection helper functions."""

from app.utils.dict_utils import add_or_update, get_value
from app.utils.list_utils import append_item, remove_item, sort_items
from app.utils.set_utils import add_to_set, union_sets


def test_list_helpers_behave_as_expected() -> None:
    """The helper functions should work on lists."""
    items = [3, 1, 2]
    append_item(items, 4)
    remove_item(items, 1)
    assert sort_items(items) == [2, 3, 4]


def test_dictionary_helpers_behave_as_expected() -> None:
    """Dictionary helpers should update and read values."""
    mapping = {"name": "Alice"}
    add_or_update(mapping, "age", 30)
    assert get_value(mapping, "age") == 30


def test_set_helpers_behave_as_expected() -> None:
    """Set helper functions should form unions."""
    left = {1, 2}
    right = {2, 3}
    add_to_set(left, 4)
    assert union_sets(left, right) == {1, 2, 3, 4}

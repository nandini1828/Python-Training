from enumerate_module.utils import *

def test_index_items():
    assert index_items(["a", "b"]) == [(0, "a"), (1, "b")]


def test_index_with_start():
    assert index_with_start(["a", "b"], 1) == [(1, "a"), (2, "b")]


def test_find_item_positions():
    assert find_item_positions(["a", "b", "a"], "a") == [0, 2]


def test_create_index_mapping():
    assert create_index_mapping(["a", "b"]) == {0: "a", 1: "b"}
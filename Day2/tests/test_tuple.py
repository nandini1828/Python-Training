from __future__ import annotations

from tuple_methods.tuple_utils import TupleMethods, count_occurrences, tuple_to_dict


def test_tuple_to_dict() -> None:
    assert tuple_to_dict(("a", "b"), (1, 2)) == {"a": 1, "b": 2}


def test_count_occurrences() -> None:
    assert count_occurrences((1, 2, 2, 3), 2) == 2


def test_tuple_methods_helper() -> None:
    helper = TupleMethods((1, 2, 2, 3))
    assert helper.first_item() == 1
    assert helper.count_value(2) == 2
    assert helper.as_list() == [1, 2, 2, 3]

from __future__ import annotations

from set_methods.set_utils import common_elements, symmetric_difference, unique_items


def test_unique_items() -> None:
    assert unique_items([1, 1, 2, 3, 3]) == {1, 2, 3}


def test_common_elements() -> None:
    assert common_elements({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_symmetric_difference() -> None:
    assert symmetric_difference({1, 2, 3}, {3, 4, 5}) == {1, 2, 4, 5}

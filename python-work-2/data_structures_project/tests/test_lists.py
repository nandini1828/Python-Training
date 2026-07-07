from data_structures.lists import (
    get_first_element,
    get_last_element,
    slice_list,
)


def test_get_first_element():
    assert get_first_element([10, 20, 30]) == 10


def test_get_last_element():
    assert get_last_element([10, 20, 30]) == 30


def test_slice_list_middle():
    assert slice_list(
        [10, 20, 30, 40, 50],
        1,
        4,
    ) == [20, 30, 40]


def test_slice_list_beginning():
    assert slice_list(
        [10, 20, 30, 40],
        0,
        2,
    ) == [10, 20]


def test_slice_list_empty():
    assert slice_list([], 0, 2) == []
from data_structures.lists import (
    get_first_element,
    get_last_element,
    slice_list,
)


def test_first_element():
    assert get_first_element([10, 20, 30]) == 10


def test_last_element():
    assert get_last_element([10, 20, 30]) == 30


def test_slice_list():
    assert slice_list([10, 20, 30, 40, 50], 1, 4) == [20, 30, 40]
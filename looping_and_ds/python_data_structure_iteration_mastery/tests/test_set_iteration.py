from looping_and_ds.python_data_structure_iteration_mastery.data_structure_iteration.set_iteration import (
    check_membership_in_list,
    check_membership_in_set,
    iterate_set_items,
)


def test_check_membership_in_list():
    assert check_membership_in_list([1, 2, 3], 2) is True
    assert check_membership_in_list([1, 2, 3], 5) is False


def test_check_membership_in_set():
    assert check_membership_in_set({1, 2, 3}, 2) is True
    assert check_membership_in_set({1, 2, 3}, 5) is False


def test_iterate_set_items():
    result = iterate_set_items({"Python", "Java", "C++"})
    assert set(result) == {"Python", "Java", "C++"}
from looping_and_ds.python_data_structure_iteration_mastery.data_structure_iteration.list_modification_trap import (
    remove_even_numbers_unsafely,
    remove_even_numbers_safely,
)


def test_remove_even_numbers_unsafely():
    result = remove_even_numbers_unsafely([1, 2, 3, 4, 5, 6])
    assert result != [1, 3, 5]


def test_remove_even_numbers_safely():
    assert remove_even_numbers_safely([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
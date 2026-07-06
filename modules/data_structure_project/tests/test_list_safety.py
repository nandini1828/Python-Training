from data_structures.list_safety import remove_even_numbers_bug, remove_even_numbers_safe


def test_remove_even_numbers_bug():
    assert remove_even_numbers_bug([1, 2, 2, 3]) == [1, 2, 3]


def test_remove_even_numbers_safe():
    assert remove_even_numbers_safe([1, 2, 2, 3]) == [1, 3]

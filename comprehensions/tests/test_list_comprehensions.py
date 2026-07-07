from comprehensions.list_comprehensions import list_comprehension_example


def test_list_comprehension_filters_even_values():
    assert list_comprehension_example([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

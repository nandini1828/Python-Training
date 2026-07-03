from data_structure_iteration.list_iteration import (
    get_items_by_index,
    get_list_slices,
    iterate_list_items,
)


def test_get_items_by_index():
    assert get_items_by_index([10, 20, 30]) == [(0, 10), (1, 20), (2, 30)]


def test_get_list_slices():
    result = get_list_slices([10, 20, 30, 40, 50])

    assert result["first_three"] == [10, 20, 30]
    assert result["last_two"] == [40, 50]
    assert result["every_second"] == [10, 30, 50]


def test_iterate_list_items():
    assert iterate_list_items(["a", "b", "c"]) == ["a", "b", "c"]
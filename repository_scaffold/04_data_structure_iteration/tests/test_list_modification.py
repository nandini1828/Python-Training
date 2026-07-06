from list_modification.utils import (
    append_item,
    clear_list,
    extend_list,
    insert_item,
    pop_item,
    remove_item,
    replace_item,
    sorted_copy,
    unique_list,
)


def test_list_modification_helpers():
    assert append_item([1], 2) == [1, 2]
    assert remove_item([1, 2], 1) == [2]
    assert insert_item([1, 3], 1, 2) == [1, 2, 3]
    assert pop_item([1, 2]) == [1]
    assert extend_list([1], [2, 3]) == [1, 2, 3]
    assert replace_item([1, 2], 2, 4) == [1, 4]
    assert clear_list([1, 2]) == []
    assert sorted_copy([3, 1, 2]) == [1, 2, 3]
    assert unique_list([1, 1, 2]) == [1, 2]

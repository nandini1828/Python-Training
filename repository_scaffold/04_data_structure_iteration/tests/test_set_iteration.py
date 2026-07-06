from set_iteration.utils import (
    add_item,
    difference_sets,
    intersect_sets,
    is_subset,
    iterate_set,
    pop_item,
    set_from_list,
    union_sets,
)


def test_set_iteration_helpers():
    a = {1, 2}
    b = {2, 3}
    assert set(iterate_set(a)) == a
    assert union_sets(a, b) == {1, 2, 3}
    assert intersect_sets(a, b) == {2}
    assert difference_sets(a, b) == {1}
    assert is_subset({1}, a)
    assert add_item(a, 3) == {1, 2, 3}
    assert pop_item({1}) == set()
    assert set_from_list([1, 1, 2]) == {1, 2}

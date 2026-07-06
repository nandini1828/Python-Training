from list_iteration.utils import (
    enumerate_list,
    filter_positive,
    find_index,
    flatten_list,
    iterate_list,
    list_summary,
    sum_items,
    unique_items,
    uppercase_items,
)


def test_list_iteration_helpers():
    assert iterate_list([1, 2, 3]) == [1, 2, 3]
    assert enumerate_list(['a', 'b']) == [(0, 'a'), (1, 'b')]
    assert find_index(['a', 'b', 'a'], 'a') == [0, 2]
    assert filter_positive([-1, 0, 1, 2]) == [1, 2]
    assert sum_items([1, 2, 3]) == 6
    assert flatten_list([[1], [2, 3]]) == [1, 2, 3]
    assert unique_items([1, 1, 2]) == [1, 2]
    assert list_summary([1, 2, 3]) == {'count': 3, 'first': 1, 'last': 3}
    assert uppercase_items(['a']) == ['A']

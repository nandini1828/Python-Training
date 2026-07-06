from dictionary_iteration.utils import (
    count_frequency,
    dictionary_to_list,
    find_key,
    get_keys,
    get_values,
    invert_dictionary,
    iterate_dictionary,
    merge_dictionaries,
)


def test_dictionary_iteration_helpers():
    data = {'x': 1, 'y': 2}
    assert iterate_dictionary(data) == [('x', 1), ('y', 2)]
    assert get_keys(data) == ['x', 'y']
    assert get_values(data) == [1, 2]
    assert merge_dictionaries(data, {'z': 3}) == {'x': 1, 'y': 2, 'z': 3}
    assert dictionary_to_list(data) == [('x', 1), ('y', 2)]
    assert invert_dictionary(data) == {1: 'x', 2: 'y'}
    assert find_key(data, 'x') == 1
    assert count_frequency(['x', 'x', 'y']) == {'x': 2, 'y': 1}

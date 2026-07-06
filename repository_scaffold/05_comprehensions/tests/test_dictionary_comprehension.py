from dictionary_comprehension.utils import (
    dict_from_lists,
    filter_dict,
    invert_unique,
    normalize_scores,
    square_dict,
    uppercase_keys,
    value_length_dict,
)


def test_dictionary_comprehension_helpers():
    assert square_dict([1, 2]) == {1: 1, 2: 4}
    assert dict_from_lists(['a'], [1]) == {'a': 1}
    assert uppercase_keys({'a': 1}) == {'A': 1}
    assert value_length_dict(['hi']) == {'hi': 2}
    assert filter_dict({'a': 1, 'b': 3}, 2) == {'b': 3}
    assert invert_unique({'low': 1, 'high': 2}) == {1: 'low', 2: 'high'}
    assert normalize_scores({'Asha': 45, 'Ravi': 40}, 50) == {
        'Asha': 90.0,
        'Ravi': 80.0,
    }

    try:
        normalize_scores({'Asha': 45}, 0)
    except ValueError as error:
        assert str(error) == 'max_score must be greater than zero'
    else:
        raise AssertionError('normalize_scores should reject max_score <= 0')

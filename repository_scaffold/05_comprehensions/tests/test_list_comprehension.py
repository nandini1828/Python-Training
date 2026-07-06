from list_comprehension.utils import (
    combine_words,
    even_numbers,
    filter_short_words,
    indexed_words,
    nested_flatten,
    square_numbers,
    strings_to_chars,
    uppercase_words,
    words_lengths,
)


def test_list_comprehension_helpers():
    assert square_numbers([1, 2]) == [1, 4]
    assert words_lengths(['a', 'bb']) == [1, 2]
    assert even_numbers([1, 2, 3]) == [2]
    assert uppercase_words(['a']) == ['A']
    assert nested_flatten([[1], [2]]) == [1, 2]
    assert combine_words(['x'], ['y']) == ['x y']
    assert filter_short_words(['one', 'four'], 3) == ['one']
    assert filter_short_words(['one'], -1) == []
    assert strings_to_chars(['ab']) == ['a', 'b']
    assert indexed_words(['a', 'b'], start=1) == ['1: a', '2: b']
    assert square_numbers(number for number in [2, 3]) == [4, 9]

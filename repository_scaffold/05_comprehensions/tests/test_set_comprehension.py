from set_comprehension.utils import (
    char_set,
    common_characters,
    even_numbers,
    filter_letters,
    square_set,
    unique_uppercase,
)


def test_set_comprehension_helpers():
    assert unique_uppercase(['a', 'b']) == {'A', 'B'}
    assert square_set([1, 2]) == {1, 4}
    assert even_numbers([1, 2, 3]) == {2}
    assert char_set(['ab']) == {'a', 'b'}
    assert filter_letters(['one', 'four']) == {'four'}
    assert common_characters('iteration', 'generator') == {
        'a',
        'e',
        'n',
        'o',
        'r',
        't',
    }

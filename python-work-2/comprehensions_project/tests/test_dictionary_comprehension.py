from comprehensions.dictionary_comprehension import (
    create_square_dictionary,
)


def test_create_square_dictionary():

    expected = {
        0: 0,
        1: 1,
        2: 4,
        3: 9,
        4: 16,
    }

    assert create_square_dictionary(5) == expected
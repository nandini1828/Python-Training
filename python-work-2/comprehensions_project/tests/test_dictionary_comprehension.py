from comprehensions.dictionary_comprehension import create_square_dictionary


def test_square_dictionary_empty():
    assert create_square_dictionary(0) == {}


def test_square_dictionary_three():
    assert create_square_dictionary(3) == {
        0: 0,
        1: 1,
        2: 4,
    }


def test_square_dictionary_five():
    assert create_square_dictionary(5)[4] == 16
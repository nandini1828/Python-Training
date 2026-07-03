from comprehensions.dictionary_comprehensions import (
    build_square_dictionary,
    map_words_to_lengths,
)


def test_build_square_dictionary():
    assert build_square_dictionary(5) == {
        0: 0,
        1: 1,
        2: 4,
        3: 9,
        4: 16,
    }


def test_map_words_to_lengths():
    assert map_words_to_lengths(["apple", "kiwi"]) == {
        "apple": 5,
        "kiwi": 4,
    }
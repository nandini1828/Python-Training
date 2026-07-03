from comprehensions.set_comprehensions import (
    get_unique_lowercase_words,
    get_even_number_set,
)


def test_get_unique_lowercase_words():
    assert get_unique_lowercase_words(["Python", "python", "JAVA"]) == {
        "python",
        "java",
    }


def test_get_even_number_set():
    assert get_even_number_set([1, 2, 2, 3, 4, 4, 5]) == {2, 4}
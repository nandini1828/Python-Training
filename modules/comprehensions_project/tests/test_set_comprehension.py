from comprehensions.set_comprehension import unique_lowercase_words


def test_unique_lowercase_words():
    assert unique_lowercase_words(["Apple", "apple", "BANANA", "banana"]) == {"apple", "banana"}

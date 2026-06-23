from exercises.word_counter import word_count


def test_word_count_basic():
    text = "Hello, world! Hello python."
    assert word_count(text) == {"hello": 2, "world": 1, "python": 1}

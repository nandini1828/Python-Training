import pytest

from exercises.word_counter import word_count

@pytest.fixture
def sample_text():
    return "Hello, world! Hello python."


def test_word_count_basic(sample_text):
    assert word_count(sample_text) == {
        "hello": 2,
        "world": 1,
        "python": 1,
    }
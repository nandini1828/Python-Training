from collections.abc import Iterator

from generator_expressions.utils import (
    char_generator,
    even_generator,
    running_total_generator,
    square_generator,
    word_lengths_generator,
)


def test_generator_expressions_helpers():
    assert list(square_generator([1, 2])) == [1, 4]
    assert list(even_generator([1, 2, 3, 4])) == [2, 4]
    assert list(char_generator(['ab'])) == ['a', 'b']
    assert list(word_lengths_generator(['hi', 'code'])) == [2, 4]
    assert list(running_total_generator([2, 4, 6])) == [2, 6, 12]
    assert isinstance(square_generator([1]), Iterator)

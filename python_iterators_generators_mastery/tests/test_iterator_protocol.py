from iterators_generators.iterator_protocol import NumberIterator


def test_number_iterator_returns_expected_values():
    assert list(NumberIterator(5)) == [1, 2, 3, 4, 5]


def test_number_iterator_empty_when_limit_zero():
    assert list(NumberIterator(0)) == []
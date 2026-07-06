from generators.iterator_protocol import IterableCounter, next_value


def test_next_value():
    assert next_value([10, 20, 30]) == 10


def test_iterable_counter():
    assert list(IterableCounter(3)) == [0, 1, 2]
